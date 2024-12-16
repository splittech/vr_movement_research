from rest_framework import serializers
from . import models


class LocomotionPresetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LocomotionPreset
        fields = '__all__'


class TeleportationPresetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeleportationPreset
        fields = '__all__'


class RotationPresetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RotationPreset
        fields = '__all__'


class PresetUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PresetUsers
        fields = '__all__'


class PresetUserSerializer(serializers.ModelSerializer):
    locomotionPreset = LocomotionPresetSerializer()
    teleportationPreset = TeleportationPresetSerializer()
    rotationPreset = RotationPresetSerializer()

    class Meta:
        model = models.PresetUsers
        fields = '__all__'

    def create(self, validated_data):
        locomotionPreset_data = validated_data.pop('locomotionPreset')
        teleportationPreset_data = validated_data.pop('teleportationPreset')
        rotationPreset_data = validated_data.pop('rotationPreset')

        locomotionPreset = models.LocomotionPreset.objects.create(
            **locomotionPreset_data)
        teleportationPreset = models.TeleportationPreset.objects.create(
            **teleportationPreset_data)
        rotationPreset = models.RotationPreset.objects.create(
            **rotationPreset_data)

        presetUser = models.PresetUsers.objects.create(locomotionPreset=locomotionPreset,
                                                       teleportationPreset=teleportationPreset,
                                                       rotationPreset=rotationPreset,
                                                       **validated_data)
        return presetUser

    def update(self, instance, validated_data):
        locomotionPreset_data = validated_data.pop('locomotionPreset')
        teleportationPreset_data = validated_data.pop('teleportationPreset')
        rotationPreset_data = validated_data.pop('rotationPreset')

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        presetUsers = models.PresetUsers.objects.get(pk=self.context['pk'])
        if locomotionPreset_data:
            models.LocomotionPresets.objects.filter(
                id=presetUsers.locomotionPresets.id).update(**locomotionPreset_data)
        if teleportationPreset_data:
            models.TeleportationPresets.objects.filter(
                id=presetUsers.locomotionPresets.id).update(**teleportationPreset_data)
        if rotationPreset_data:
            models.RotationPresets.objects.filter(
                id=presetUsers.locomotionPresets.id).update(**rotationPreset_data)
            
        return instance
