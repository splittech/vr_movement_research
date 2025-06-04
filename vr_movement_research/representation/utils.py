import math

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from django.db.models import ForeignKey
from django.db.models import Q


def get_dependence_chart(PresetModel, field_name_x,
                         field_name_y, presets_type):
    """
    Функция возвращает график зависимости между двумя
    указанными параметрами модели в представлении html.
    """

    # Получаем набор настроек в зависимости от указанного типа и модели.
    presets = []
    if presets_type == 'top_time':
        presets = PresetModel.objects.filter(
             isTopTime=True,
             time__gt=120
        )
    elif presets_type == 'both':
        top_time_presets = PresetModel.objects.filter(
             isTopTime=True,
             time__gt=120
        )
        last_presets = PresetModel.objects.filter(
             isTopTime=False
        )
        presets = top_time_presets | last_presets
    else:
        presets = PresetModel.objects.filter(
             isTopTime=False,
        )

    # Получаем наборы точек для графика.
    if (field_name_x is None or field_name_y is None):
        field_name_x, field_name_y = 'id', 'id'
        field_values_x = [preset.pk for preset in presets]
        field_values_y = [preset.pk for preset in presets]
    else:
        field_values_x = [get_attr_with_nested(obj, field_name_x) for obj in presets]
        field_values_y = [get_attr_with_nested(obj, field_name_y) for obj in presets]
        # Объединяем два списка.
        zipped_lists = zip(field_values_x, field_values_y)
        # Сортируем объединенный список по значениям первого списка.
        sorted_pairs = sorted(zipped_lists)
        # Распаковываем отсортированные пары обратно в отдельные списки.
        sorted_field_values_x, sorted_field_values_y = zip(*sorted_pairs)
        field_values_x = list(sorted_field_values_x)
        field_values_y = list(sorted_field_values_y)

    # Русифицируем.
    verbose_name_x = get_verbose_name_with_nested(PresetModel, field_name_x)
    verbose_name_y = get_verbose_name_with_nested(PresetModel, field_name_y)

    # Строим график.
    fig = px.line(
        x=field_values_x,
        y=field_values_y,
        title='График зависимости',
        labels={'x': verbose_name_x, 'y': verbose_name_y}
    )
    fig.update_layout(
        title={
            'font_size': 24,
            'xanchor': 'center',
            'x': 0.5
        }
    )

    # Возвращаем html-представление.
    return fig.to_html


def get_histogram_chart(PresetModel, field_name, presets_type):
    """
    Функция возвращает гистограмму для указанного
    поля модели в представлении html.
    """

    # Получаем набор настроек в зависимости от указанного типа и модели.
    if presets_type == 'both':
        presets = PresetModel.objects.all()
    else:
        presets = PresetModel.objects.filter(
             isTopTime=presets_type == 'top_time'
        )

    # Получаем набор значений для графика.
    if field_name is None:
        field_name = 'id'
        field_values = [preset.pk for preset in presets]
    else:
        field_values = [get_attr_with_nested(obj, field_name) for obj in presets]

    # Русифицируем.
    verbose_name = get_verbose_name_with_nested(PresetModel, field_name)

    # Строим график.
    fig = px.histogram(
        field_values,
        nbins=len(set(field_values))*5
    )
    fig.update_layout(
        title={
            'text': 'Гистограмма',
            'font_size': 24,
            'xanchor': 'center',
            'x': 0.5
        },
        bargap=0.1,
        xaxis_title=verbose_name,
        yaxis_title='Количество'
    )

    # Возвращаем html-представление.
    return fig.to_html


def get_attr_with_nested(obj, attr):
    if '__' in attr:
        parts = attr.split('__')
        value = obj
        for part in parts:
            value = getattr(value, part)
        return value
    else:
        return getattr(obj, attr)


def get_verbose_name_with_nested(model, field_name):
    if '__' in field_name:
        parts = field_name.split('__')
        current_model = model
        for part in parts[:-1]:
            field = current_model._meta.get_field(part)
            if isinstance(field, ForeignKey):
                current_model = field.related_model
            else:
                raise ValueError(f"Field {part} is not a ForeignKey")
        final_field = current_model._meta.get_field(parts[-1])
        return final_field.verbose_name
    else:
        return model._meta.get_field(field_name).verbose_name
