from django.db import models


class ExperimentSession(models.Model):

    deviceName = models.CharField(max_length=255)
    comment = models.TextField(null=True, blank=True)
    

class LocomotionPreset(models.Model):

    experimentSession_1 = models.ForeignKey(ExperimentSession,
                                            related_name='lastLocomotionPreset',
                                            on_delete=models.CASCADE,
                                            blank=True,
                                            null=True)
    
    experimentSession_2 = models.ForeignKey(ExperimentSession,
                                            related_name='topTimeLocomotionPresets',
                                            on_delete=models.CASCADE,
                                            blank=True,
                                            null=True)
    
    name = models.CharField(max_length=255, null=True, blank=True)
    time = models.FloatField(null=True)
    movementSpeed = models.FloatField(null=True)
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

    experimentSession_1 = models.ForeignKey(ExperimentSession,
                                            related_name='lastTeleportationPreset',
                                            on_delete=models.CASCADE,
                                            blank=True,
                                            null=True)
    
    experimentSession_2 = models.ForeignKey(ExperimentSession,
                                            related_name='topTimeTeleportationPresets',
                                            on_delete=models.CASCADE,
                                            blank=True,
                                            null=True)

    name = models.CharField(max_length=255, null=True, blank=True)
    time = models.FloatField(null=True)
    teleportationDelay = models.FloatField(null=True)
    allowDashTeleportation = models.BooleanField()
    shiftType = models.IntegerField(null=True)
    linearShiftSpeed = models.FloatField(null=True)
    smoothDampShiftSpeed = models.FloatField(null=True)
    allowScreenFading = models.BooleanField()
    screenFadingMask = models.IntegerField(null=True)
    screenFadingSpeed = models.FloatField(null=True)
    screenFadingAlpha = models.FloatField(null=True)


class RotationPreset(models.Model):

    experimentSession_1 = models.ForeignKey(ExperimentSession,
                                            related_name='lastRotationPreset',
                                            on_delete=models.CASCADE,
                                            blank=True,
                                            null=True)
    
    experimentSession_2 = models.ForeignKey(ExperimentSession,
                                            related_name='topTimeRotationPresets',
                                            on_delete=models.CASCADE,
                                            blank=True,
                                            null=True)

    name = models.CharField(max_length=255, null=True, blank=True)
    time = models.FloatField(null=True)
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

    

