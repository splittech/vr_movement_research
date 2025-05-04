from django import forms
from get_data import models

# Поля, которые нужно исключить из выбора в форме.
EXCLUDE_PRESET_FIELDS = ('isTopTime',)
EXCLUDE_SESSION_FIELDS = ('id', 'comments')

# Выбор типов рассматриваемых настроек.
PRESETS_TYPE_CHOICES = [('last', 'Последние'),
                        ('top_time', 'Самые частые'),
                        ('both', 'Все')]

# Параметры запроса формы для изменения графика
# зависимости настроек плавного передвижения.
DEPENDENCY_CHART_X_PARAMETER = 'dependency_chart_x'
DEPENDENCY_CHART_Y_PARAMETER = 'dependency_chart_y'
DEPENDENCY_CHART_TYPE_PARAMETER = 'dependency_chart_type'

# Параметры запроса формы для изменения гистограммы
# одного поля настроек плавного передвижения.
HISTOGRAM_CHART_X_PARAMETER = 'histogram_x'
HISTOGRAM_CHART_TYPE_PARAMETER = 'histogram_type'


class BaseChartForm(forms.Form):
    """
    Общий базовый класс форм для динамического изменения
    графиков зависимостей настроек передвижения.
    """

    choices = []

    # Эти поля должны быть переопределены
    preset_fields = []  # Пример: models.LocomotionPreset._meta.get_fields()
    field_names = {'chart_x': 'example_x',
                   'chart_y': 'example_y',
                   'presets_type': 'example_type'}

    def __init__(self, *args, **kwargs):
        super(BaseChartForm, self).__init__(*args, **kwargs)

        self.choices = []

        session_fields = models.ExperimentSession._meta.get_fields()

        for field in self.preset_fields:
            if field.is_relation or field.name in EXCLUDE_PRESET_FIELDS:
                continue
            self.choices.append((field.name, field.verbose_name))

        session_choices = []
        for field in session_fields:
            if field.is_relation or field.name in EXCLUDE_SESSION_FIELDS:
                continue
            session_choices.append((f'experimentSession__{field.name}',
                                    field.verbose_name))

        self.choices.extend(session_choices)

        self.fields[self.field_names['presets_type']] = forms.ChoiceField(
            choices=PRESETS_TYPE_CHOICES,
            label='Тип настроек',
            widget=forms.Select(attrs={'class': 'form-select',
                                       'aria-label': 'Default select example'})
        )


class BaseDependencyChartForm(BaseChartForm):
    """
    Базовый класс форм для динамического изменения
    графиков зависимостей настроек передвижения.
    """

    def __init__(self, *args, **kwargs):
        super(BaseDependencyChartForm, self).__init__(*args, **kwargs)
        self.fields[self.field_names['chart_x']] = forms.ChoiceField(
            choices=self.choices,
            label='Ось X',
            widget=forms.Select(attrs={'class': 'form-select',
                                       'aria-label': 'Default select example'})
        )
        self.fields[self.field_names['chart_y']] = forms.ChoiceField(
            choices=self.choices,
            label='Ось Y',
            widget=forms.Select(attrs={'class': 'form-select',
                                       'aria-label': 'Default select example'})
        )


class BaseHistogramForm(BaseChartForm):
    """
    Базовый класс формы для динамического изменения гистограмм.
    """
    # Эти поля должны быть переопределены
    preset_fields = []  # Пример: models.LocomotionPreset._meta.get_fields()
    field_names = {'chart_x': 'example_x',
                   'presets_type': 'example_type'}

    def __init__(self, *args, **kwargs):
        super(BaseHistogramForm, self).__init__(*args, **kwargs)

        self.fields[self.field_names['chart_x']] = forms.ChoiceField(
            choices=self.choices,
            label='Поле модели',
            widget=forms.Select(attrs={'class': 'form-select',
                                       'aria-label': 'Default select example'})
        )


class LocomotionDependenceChartForm(BaseDependencyChartForm):
    preset_fields = models.LocomotionPreset._meta.get_fields()
    field_names = {'chart_x': DEPENDENCY_CHART_X_PARAMETER,
                   'chart_y': DEPENDENCY_CHART_Y_PARAMETER,
                   'presets_type': DEPENDENCY_CHART_TYPE_PARAMETER}


class TeleportationDependenceChartForm(BaseDependencyChartForm):
    preset_fields = models.TeleportationPreset._meta.get_fields()
    field_names = {'chart_x': DEPENDENCY_CHART_X_PARAMETER,
                   'chart_y': DEPENDENCY_CHART_Y_PARAMETER,
                   'presets_type': DEPENDENCY_CHART_TYPE_PARAMETER}


class RotationDependenceChartForm(BaseDependencyChartForm):
    preset_fields = models.RotationPreset._meta.get_fields()
    field_names = {'chart_x': DEPENDENCY_CHART_X_PARAMETER,
                   'chart_y': DEPENDENCY_CHART_Y_PARAMETER,
                   'presets_type': DEPENDENCY_CHART_TYPE_PARAMETER}


class LocomotionHistogramChartForm(BaseHistogramForm):
    preset_fields = models.LocomotionPreset._meta.get_fields()
    field_names = {'chart_x': HISTOGRAM_CHART_X_PARAMETER,
                   'presets_type': HISTOGRAM_CHART_TYPE_PARAMETER}


class TeleportationHistogramChartForm(BaseHistogramForm):
    preset_fields = models.TeleportationPreset._meta.get_fields()
    field_names = {
        'chart_x': HISTOGRAM_CHART_X_PARAMETER,
        'presets_type': HISTOGRAM_CHART_TYPE_PARAMETER
    }


class RotationHistogramChartForm(BaseHistogramForm):
    preset_fields = models.RotationPreset._meta.get_fields()
    field_names = {'chart_x': HISTOGRAM_CHART_X_PARAMETER,
                   'presets_type': HISTOGRAM_CHART_TYPE_PARAMETER}
