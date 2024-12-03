from django.db import models


class LocomotionPresets(models.Model):

    name = models.CharField(max_length=255)

    movementSpeed = models.FloatField()

    allowHandDirection = models.BooleanField()

    handChoice = models.IntegerField(null=True)

    allowScreenShaking = models.BooleanField()

    screenShakingAmplitude = models.FloatField(null=True)

    screenShakingSpeed = models.FloatField(null=True)

    allowScreenFading = models.BooleanField()

    screenFadingMask = models.IntegerField(null=True)

    screenFadingSpeed = models.FloatField(null=True)

    screenFadingAlpha = models.FloatField(null=True)


class TeleportationPresets(models.Model):

    name = models.CharField(max_length=255)

    teleportationDelay = models.FloatField()

    allowDashTeleportation = models.BooleanField()

    shiftType = models.IntegerField(null=True)

    linearShiftSpeed = models.FloatField(null=True)

    smoothDampShiftSpeed = models.FloatField(null=True)

    allowScreenFading = models.BooleanField()

    screenFadingMask = models.IntegerField(null=True)

    screenFadingSpeed = models.FloatField(null=True)

    screenFadingAlpha = models.FloatField(null=True)


class RotationPresets(models.Model):

    name = models.CharField(max_length=255)

    rotationType = models.IntegerField()

    smoothRotationSpeed = models.FloatField(null=True)

    snapRotationAngle = models.FloatField(null=True)

    snapRotationDelay = models.FloatField(null=True)

    allowDashRotation = models.BooleanField(null=True)

    shiftType = models.IntegerField(null=True)

    linearShiftSpeed = models.FloatField(null=True)

    smoothDampShiftSpeed = models.FloatField(null=True)

    allowScreenFading = models.BooleanField()

    screenFadingMask = models.IntegerField(null=True)

    screenFadingSpeed = models.FloatField(null=True)

    screenFadingAlpha = models.FloatField(null=True)


class PresetUsers(models.Model):

    name = models.CharField(max_length=255)

    locomotionPresets = models.ForeignKey(LocomotionPresets,
                                          on_delete=models.CASCADE)

    teleportationPresets = models.ForeignKey(TeleportationPresets,
                                             on_delete=models.CASCADE)

    rotationPresets = models.ForeignKey(RotationPresets,
                                        on_delete=models.CASCADE)
