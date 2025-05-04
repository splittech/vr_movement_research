from django.db import models


class ExperimentSession(models.Model):
    """
    Данные об одной сессии эксперимента (для одного человека).
    """
    deviceName = models.CharField(max_length=255,
                                  verbose_name='Название устройства')
    sessionTotalTime = models.FloatField(verbose_name='Общее время сессии')
    personAge = models.IntegerField(verbose_name='Возраст')
    personExperienceInVR = models.IntegerField(verbose_name='Опыт в VR',
                                               help_text='В часах')
    comments = models.TextField(verbose_name='Комментарии',
                                null=True, blank=True)

    class Meta:
        verbose_name = 'Сессия'
        verbose_name_plural = 'Сессии'

    def __str__(self):
        return 'Сессия номер ' + str(self.id)


class BasePreset(models.Model):
    """
    Абстрактная модель для набора настроек.
    """
    experimentSession = models.ForeignKey(
        ExperimentSession,
        on_delete=models.CASCADE,
        related_name='%(class)s',
        verbose_name='Сессия'
    )

    isTopTime = models.BooleanField(default=False)

    time = models.FloatField(blank=True, null=True,
                             verbose_name='Время использования')

    allowScreenFading = models.BooleanField(verbose_name='Затемнение экрана')
    screenFadingMask = models.IntegerField(verbose_name='Маска')
    screenFadingSpeed = models.FloatField(verbose_name='Скорость затемнения')
    screenFadingAlpha = models.FloatField(
        verbose_name='Прозрачность затемнения'
    )

    class Meta:
        abstract = True


class LocomotionPreset(BasePreset):
    """
    Модель для набора настроек плавного передвижения.
    """
    movementSpeed = models.FloatField(verbose_name='Скорость передвижения')
    allowHandDirection = models.BooleanField(
        verbose_name='Рука указывает направление'
    )
    handChoice = models.IntegerField(verbose_name='Рука',
                                     help_text='0-левая, 1-правая')
    allowScreenShaking = models.BooleanField(verbose_name='Покачивание экрана')
    screenShakingAmplitude = models.FloatField(
        verbose_name='Амплитуда покачивания'
    )
    screenShakingSpeed = models.FloatField(verbose_name='Скорость покачивания')

    class Meta:
        verbose_name = 'Настройки плавного передвижения'
        verbose_name_plural = 'Настройки плавного передвижения'


class TeleportationPreset(BasePreset):
    """
    Модель для набора настроек телепортации.
    """
    teleportationDelay = models.FloatField(
        verbose_name='Задержка телепортации'
    )
    allowDashTeleportation = models.BooleanField(
        verbose_name='Телепортация рывком'
    )
    shiftType = models.IntegerField(
        verbose_name='Режим перемещения',
        help_text='0-линейное перемещение, 1-перемещение с ускорением'
    )
    linearShiftSpeed = models.FloatField(
        verbose_name='Линейная скорость'
    )
    smoothDampShiftSpeed = models.FloatField(
        verbose_name='Скорость с ускорением'
    )

    class Meta:
        verbose_name = 'Настройки телепортации'
        verbose_name_plural = 'Настройки телепортации'


class RotationPreset(BasePreset):
    """
    Модель для набора настроек вращения.
    """
    rotationType = models.IntegerField(verbose_name='Тип вращения')
    smoothRotationSpeed = models.FloatField(
        verbose_name='Скорость плавного вращения'
    )
    snapRotationAngle = models.FloatField(verbose_name='Угол резкого вращения')
    snapRotationDelay = models.FloatField(
        verbose_name='Задержка резкого вращения'
    )
    allowDashRotation = models.BooleanField(verbose_name='Вращение рывком')
    shiftType = models.IntegerField(
        verbose_name='Режим вращения рывком',
        help_text='0-линейное вращение, 1-вразение с ускорением')
    linearShiftSpeed = models.FloatField(verbose_name='Линейная скорость')
    smoothDampShiftSpeed = models.FloatField(
        verbose_name='Скорость с ускорением'
    )

    class Meta:
        verbose_name = 'Настройки вращения'
        verbose_name_plural = 'Настройки вращения'
