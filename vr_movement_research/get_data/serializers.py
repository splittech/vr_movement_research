from rest_framework import serializers
from . import models


class BasePresetSerializer(serializers.ModelSerializer):
    """
    Базовый сериализатор для набора настроек.
    """
    experimentSession = serializers.PrimaryKeyRelatedField(
        queryset=models.ExperimentSession.objects.all(),
        required=False
    )

    class Meta:
        fields = '__all__'


class LocomotionPresetSerializer(BasePresetSerializer):
    """
    Базовый сериализатор для набора настроек плавного передвижения.
    """
    class Meta(BasePresetSerializer.Meta):
        model = models.LocomotionPreset


class TeleportationPresetSerializer(BasePresetSerializer):
    """
    Базовый сериализатор для набора настроек телепортации.
    """
    class Meta(BasePresetSerializer.Meta):
        model = models.TeleportationPreset


class RotationPresetSerializer(BasePresetSerializer):
    """
    Базовый сериализатор для набора настроек вращения.
    """
    class Meta(BasePresetSerializer.Meta):
        model = models.RotationPreset


class ExperimentSessionSerializer(serializers.ModelSerializer):
    """
    Основной сериализатор для обработки данных о сессии одного пользователя.
    """
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

        topTimeLocomotionPresets = validated_data.pop(
            'topTimeLocomotionPresets'
        )
        topTimeTeleportationPresets = validated_data.pop(
            'topTimeTeleportationPresets'
        )
        topTimeRotationPresets = validated_data.pop(
            'topTimeRotationPresets'
        )

        experimentSession = models.ExperimentSession.objects.create(
            **validated_data
        )

        lastLocomotionPreset.pop('time', None)
        models.LocomotionPreset.objects.create(
            experimentSession=experimentSession,
            **lastLocomotionPreset
        )

        lastTeleportationPreset.pop('time', None)
        models.TeleportationPreset.objects.create(
            experimentSession=experimentSession,
            **lastTeleportationPreset
        )

        lastRotationPreset.pop('time', None)
        models.RotationPreset.objects.create(
            experimentSession=experimentSession,
            **lastRotationPreset
        )

        for topTimeLocomotionPreset in topTimeLocomotionPresets:
            models.LocomotionPreset.objects.create(
                experimentSession=experimentSession,
                isTopTime=True,
                **topTimeLocomotionPreset
            )

        for topTimeTeleportationPreset in topTimeTeleportationPresets:
            models.TeleportationPreset.objects.create(
                experimentSession=experimentSession,
                isTopTime=True,
                **topTimeTeleportationPreset
            )

        for topTimeRotationPreset in topTimeRotationPresets:
            models.RotationPreset.objects.create(
                experimentSession=experimentSession,
                isTopTime=True,
                **topTimeRotationPreset
            )

        return experimentSession

    class Meta:
        model = models.ExperimentSession
        fields = '__all__'
