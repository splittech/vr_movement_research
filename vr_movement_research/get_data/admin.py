from django.contrib import admin
from . import models

admin.site.register(models.LocomotionPreset)
admin.site.register(models.TeleportationPreset)
admin.site.register(models.RotationPreset)
admin.site.register(models.PresetUsers)