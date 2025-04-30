from django.contrib import admin
from . import models


class BasePresetInLine(admin.TabularInline):
    is_top_time = False

    fk_name = 'experimentSession'
    exclude = ('isTopTime',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(isTopTime=self.is_top_time)


class LastLocomotionPresetInLine(BasePresetInLine):

    verbose_name = 'Последние настройки плавного передвижения'
    verbose_name_plural = 'Последние настройки плавного передвижения'
    model = models.LocomotionPreset


class LastTeleportationPresetInLine(BasePresetInLine):

    verbose_name = 'Последние настройки телепортации'
    verbose_name_plural = 'Последние настройки телепортации'
    model = models.TeleportationPreset


class LastRotationPresetInLine(BasePresetInLine):

    verbose_name = 'Последние настройки поворота'
    verbose_name_plural = 'Последние настройки поворота'
    model = models.RotationPreset


class TopTimeLocomotionPresetInLine(BasePresetInLine):

    verbose_name = 'Самые частые настройки плавного передвижения'
    verbose_name_plural = 'Самые частые настройки плавного передвижения'
    model = models.LocomotionPreset

    is_top_time = True


class TopTimeTeleportationPresetInLine(BasePresetInLine):

    verbose_name = 'Самые частые настройки телепортации'
    verbose_name_plural = 'Самые частые настройки телепортации'
    model = models.TeleportationPreset

    is_top_time = True


class TopTimeRotationPresetInLine(BasePresetInLine):

    verbose_name = 'Самые частые настройки поворота'
    verbose_name_plural = 'Самые частые настройки поворота'
    model = models.RotationPreset

    is_top_time = True


class ExperimentSessionAdmin(admin.ModelAdmin):

    model = models.ExperimentSession

    inlines = (LastLocomotionPresetInLine,
               LastTeleportationPresetInLine,
               LastRotationPresetInLine,
               TopTimeLocomotionPresetInLine,
               TopTimeTeleportationPresetInLine,
               TopTimeRotationPresetInLine)


admin.site.register(models.ExperimentSession, ExperimentSessionAdmin)
admin.site.register(models.LocomotionPreset)
admin.site.register(models.TeleportationPreset)
admin.site.register(models.RotationPreset)
