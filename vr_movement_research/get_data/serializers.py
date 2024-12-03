from rest_framework import serializers
from . import models


class LocomotionPresetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LocomotionPresets
        fields = '__all__'


class TeleportationPresetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeleportationPresets
        fields = '__all__'


class RotationPresetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RotationPresets
        fields = '__all__'


class PresetUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PresetUsers
        fields = '__all__'


class PresetUserSerializer(serializers.ModelSerializer):
    locomotionPresets = LocomotionPresetSerializer()
    teleportationPresets = TeleportationPresetSerializer()
    rotationPresets = RotationPresetSerializer()

    class Meta:
        model = models.PresetUsers
        fields = '__all__'

    def create(self, validated_data):
        locomotionPresets_data = validated_data.pop('locomotionPresets')
        teleportationPresets_data = validated_data.pop('teleportationPresets')
        rotationPresets_data = validated_data.pop('rotationPresets')

        locomotionPresets = models.LocomotionPresets.objects.create(
            **locomotionPresets_data)
        teleportationPresets = models.TeleportationPresets.objects.create(
            **teleportationPresets_data)
        rotationPresets = models.RotationPresets.objects.create(
            **rotationPresets_data)

        presetUser = models.PresetUsers.objects.create(locomotionPresets=locomotionPresets,
                                                       teleportationPresets=teleportationPresets,
                                                       rotationPresets=rotationPresets,
                                                       **validated_data)
        return presetUser

    def update(self, instance, validated_data):
        locomotionPresets_data = validated_data.pop('locomotionPresets')
        teleportationPresets_data = validated_data.pop('teleportationPresets')
        rotationPresets_data = validated_data.pop('rotationPresets')

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        presetUsers = models.PresetUsers.objects.get(pk=self.context['pk'])
        if locomotionPresets_data:
            models.LocomotionPresets.objects.filter(
                id=presetUsers.locomotionPresets.id).update(**locomotionPresets_data)
        if teleportationPresets_data:
            models.TeleportationPresets.objects.filter(
                id=presetUsers.locomotionPresets.id).update(**teleportationPresets_data)
        if rotationPresets_data:
            models.RotationPresets.objects.filter(
                id=presetUsers.locomotionPresets.id).update(**rotationPresets_data)
            
        return instance
