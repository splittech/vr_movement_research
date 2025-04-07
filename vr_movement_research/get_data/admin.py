from django.contrib import admin
from . import models

admin.site.register(models.LocomotionPreset)
admin.site.register(models.TeleportationPreset)
admin.site.register(models.RotationPreset)

class LastLocomotionPresetInLine(admin.TabularInline):

    verbose_name = 'Последние настройки плавного передвижения'
    verbose_name_plural = 'Последние настройки плавного передвижения'
    model = models.LocomotionPreset
    fk_name = 'experimentSession_1'

    exclude=('experimentSession_2', 'name')

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return extra - obj.lastLocomotionPreset.count()
        return extra

class LastTeleportationPresetInLine(admin.TabularInline):

    verbose_name = 'Последние настройки телепортации'
    verbose_name_plural = 'Последние настройки телепортации'
    model = models.TeleportationPreset
    fk_name = 'experimentSession_1'

    exclude=('experimentSession_2', 'name')

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return extra - obj.lastTeleportationPreset.count()
        return extra

class LastRotationPresetInLine(admin.TabularInline):

    verbose_name = 'Последние настройки поворота'
    verbose_name_plural = 'Последние настройки поворота'
    model = models.RotationPreset
    fk_name = 'experimentSession_1'

    exclude=('experimentSession_2', 'name')

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return extra - obj.lastRotationPreset.count()
        return extra

class TopTimeLocomotionPresetInLine(admin.TabularInline):

    verbose_name = 'Самые частые настройки плавного передвижения'
    verbose_name_plural = 'Самые частые настройки плавного передвижения'
    model = models.LocomotionPreset
    fk_name = 'experimentSession_2'

    exclude=('experimentSession_1', 'name')

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return extra - obj.lastLocomotionPreset.count()
        return extra

class TopTimeTeleportationPresetInLine(admin.TabularInline):

    verbose_name = 'Самые частые настройки телепортации'
    verbose_name_plural = 'Самые частые настройки телепортации'
    model = models.TeleportationPreset
    fk_name = 'experimentSession_2'

    exclude=('experimentSession_1', 'name')

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return extra - obj.lastTeleportationPreset.count()
        return extra

class TopTimeRotationPresetInLine(admin.TabularInline):

    verbose_name = 'Самые частые настройки поворота'
    verbose_name_plural = 'Самые частые настройки поворота'
    model = models.RotationPreset
    fk_name = 'experimentSession_2'

    exclude=('experimentSession_1', 'name')

    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        if obj:
            return extra - obj.lastRotationPreset.count()
        return extra

class ExperimentSessionAdmin(admin.ModelAdmin):

    model = models.ExperimentSession

    inlines = (LastLocomotionPresetInLine,
               LastTeleportationPresetInLine,
               LastRotationPresetInLine,
               TopTimeLocomotionPresetInLine,
               TopTimeTeleportationPresetInLine,
               TopTimeRotationPresetInLine)
    
admin.site.register(models.ExperimentSession, ExperimentSessionAdmin)