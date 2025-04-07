from rest_framework import serializers
from . import models

# TYRUFUY6T = serializers.JTYGFVJYT(SOURCE="lastLocomotionPreset.NdeviceNameAME")

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

class ExperimentSessionSerializer(serializers.ModelSerializer):

    lastLocomotionPreset = LocomotionPresetSerializer()
    lastTeleportationPreset = TeleportationPresetSerializer()
    lastRotationPreset = RotationPresetSerializer()

    topTimeLocomotionPresets = LocomotionPresetSerializer(many=True)
    topTimeTeleportationPresets = TeleportationPresetSerializer(many=True)
    topTimeRotationPresets = RotationPresetSerializer(many=True)

    def create(self, validated_data):

        lastLocomotionPreset = validated_data.pop('lastLocomotionPreset')
        lastTeleportationPreset = validated_data.pop('lastTeleportationPreset')
        lastRotationPreset = validated_data.pop('lastRotationPreset')

        topTimeLocomotionPresets = validated_data.pop('topTimeLocomotionPresets')
        topTimeTeleportationPresets = validated_data.pop('topTimeTeleportationPresets')
        topTimeRotationPresets = validated_data.pop('topTimeRotationPresets')

        experimentSession = models.ExperimentSession.objects.create(**validated_data)

        models.LocomotionPreset.objects.create(experimentSession_1=experimentSession,
                                                **lastLocomotionPreset)

        models.TeleportationPreset.objects.create(experimentSession_1=experimentSession,
                                                   **lastTeleportationPreset)
        
        models.RotationPreset.objects.create(experimentSession_1=experimentSession,
                                                   **lastRotationPreset)

        for topTimeLocomotionPreset in topTimeLocomotionPresets:
            models.LocomotionPreset.objects.create(experimentSession_2=experimentSession,
                                                   **topTimeLocomotionPreset)
            
        for topTimeTeleportationPreset in topTimeTeleportationPresets:
            models.TeleportationPreset.objects.create(experimentSession_2=experimentSession,
                                                      **topTimeTeleportationPreset)
        
        for topTimeRotationPreset in topTimeRotationPresets:
            models.RotationPreset.objects.create(experimentSession_2=experimentSession,
                                                 **topTimeRotationPreset)

        return experimentSession


    class Meta:
        model = models.ExperimentSession
        fields = '__all__'

    
