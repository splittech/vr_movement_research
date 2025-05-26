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
        lastLocomotionPreset = self.cast_unused_options_for_locomotion(
            lastLocomotionPreset)
        models.LocomotionPreset.objects.create(
            experimentSession=experimentSession,
            **lastLocomotionPreset
        )

        lastTeleportationPreset.pop('time', None)
        lastTeleportationPreset = self.cast_unused_options_for_teleportation(
            lastTeleportationPreset)
        models.TeleportationPreset.objects.create(
            experimentSession=experimentSession,
            **lastTeleportationPreset
        )

        lastRotationPreset.pop('time', None)
        lastRotationPreset = self.cast_unused_options_for_rotation(
            lastRotationPreset)
        models.RotationPreset.objects.create(
            experimentSession=experimentSession,
            **lastRotationPreset
        )

        for topTimeLocomotionPreset in topTimeLocomotionPresets:
            topTimeLocomotionPreset = self.cast_unused_options_for_locomotion(
                topTimeLocomotionPreset)
            models.LocomotionPreset.objects.create(
                experimentSession=experimentSession,
                isTopTime=True,
                **topTimeLocomotionPreset
            )

        for topTimeTeleportationPreset in topTimeTeleportationPresets:
            topTimeTeleportationPreset = self.cast_unused_options_for_teleportation(topTimeTeleportationPreset)
            models.TeleportationPreset.objects.create(
                experimentSession=experimentSession,
                isTopTime=True,
                **topTimeTeleportationPreset
            )

        for topTimeRotationPreset in topTimeRotationPresets:
            topTimeRotationPreset = self.cast_unused_options_for_rotation(topTimeRotationPreset)
            models.RotationPreset.objects.create(
                experimentSession=experimentSession,
                isTopTime=True,
                **topTimeRotationPreset
            )

        return experimentSession

    def cast_unused_options_for_locomotion(self, data):

        if data.get('allowHandDirection') is not True:
            data.pop('allowHandDirection', None)

        if data.get('allowScreenShaking') is not True:
            data.pop('screenShakingAmplitude', None)
            data.pop('screenShakingSpeed', None)

        if data.get('allowScreenFading') is not True:
            data.pop('screenFadingMask', None)
            data.pop('screenFadingSpeed', None)
            data.pop('screenFadingAlpha', None)

        return data

    def cast_unused_options_for_teleportation(self, data):

        if data.get('allowDashTeleportation') is not True:
            data.pop('shiftType', None)

        if data.get('shiftType') != 0:
            data.pop('linearShiftSpeed', None)

        if data.get('shiftType') != 1:
            data.pop('smoothDampShiftSpeed', None)

        if data.get('allowScreenFading') is not True:
            data.pop('screenFadingMask', None)
            data.pop('screenFadingSpeed', None)
            data.pop('screenFadingAlpha', None)

        return data

    def cast_unused_options_for_rotation(self, data):

        if data.get('rotationType') != 0:
            data.pop('smoothRotationSpeed', None)

        if data.get('rotationType') != 1:
            data.pop('snapRotationAngle', None)
            data.pop('snapRotationDelay', None)
            data.pop('allowDashRotation', None)

        if data.get('allowDashRotation') is not True:
            data.pop('shiftType', None)

        if data.get('shiftType') != 0:
            data.pop('linearShiftSpeed', None)

        if data.get('shiftType') != 1:
            data.pop('smoothDampShiftSpeed', None)

        if data.get('allowScreenFading') is not True:
            data.pop('screenFadingMask', None)
            data.pop('screenFadingSpeed', None)
            data.pop('screenFadingAlpha', None)

        return data

    class Meta:
        model = models.ExperimentSession
        fields = '__all__'
