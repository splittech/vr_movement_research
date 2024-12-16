from django.db import models


class LocomotionPreset(models.Model):

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


class TeleportationPreset(models.Model):

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


class RotationPreset(models.Model):

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

    locomotionPreset = models.ForeignKey(LocomotionPreset,
                                         on_delete=models.CASCADE)

    teleportationPreset = models.ForeignKey(TeleportationPreset,
                                            on_delete=models.CASCADE)

    rotationPreset = models.ForeignKey(RotationPreset,
                                       on_delete=models.CASCADE)
