from django.contrib import admin
from . import models

admin.site.register(models.LocomotionPresets)
admin.site.register(models.TeleportationPresets)
admin.site.register(models.RotationPresets)