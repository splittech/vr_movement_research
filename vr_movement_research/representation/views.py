from django.shortcuts import render
from django.urls import resolve

from . import forms
from . import utils
from get_data import models


def general_charts(request, page_header, preset_model,
                   dependency_chart_form, histogram_chart_form):
    """
    Базовое представление для отображения графика зависимости и гистограммы
    для указанного поля с возможностью изменять поля для графиков.
    """

    dependency_chart = utils.get_dependence_chart(
        preset_model,
        request.GET.get(forms.DEPENDENCY_CHART_X_PARAMETER),
        request.GET.get(forms.DEPENDENCY_CHART_Y_PARAMETER),
        request.GET.get(forms.DEPENDENCY_CHART_TYPE_PARAMETER)
    )

    histogram_chart = utils.get_histogram_chart(
        preset_model,
        request.GET.get(forms.HISTOGRAM_CHART_X_PARAMETER),
        request.GET.get(forms.HISTOGRAM_CHART_TYPE_PARAMETER)
    )

    context = {
        'url_name': resolve(request.path).url_name,
        'page_header': page_header,
        'dependency_chart': dependency_chart,
        'dependency_form': dependency_chart_form(request.GET),
        'histogram_chart': histogram_chart,
        'histogram_form': histogram_chart_form(request.GET)
    }

    return render(request, 'representation/charts.html', context)


def locomotion_charts(request):
    """
    Представление для отображения графиков для настроек плавного передвижения.
    """
    return general_charts(
        request,
        'Анализ данных для настроек плавного передвижения',
        models.LocomotionPreset,
        forms.LocomotionDependenceChartForm,
        forms.LocomotionHistogramChartForm
    )


def teleportation_charts(request):
    """
    Представление для отображения графиков для настроек телепортации.
    """
    return general_charts(
        request,
        'Анализ данных для настроек телепортации',
        models.TeleportationPreset,
        forms.TeleportationDependenceChartForm,
        forms.TeleportationHistogramChartForm
    )


def rotation_charts(request):
    """
    Представление для отображения графиков для настроек вращения.
    """
    return general_charts(
        request,
        'Анализ данных для настроек вращения',
        models.RotationPreset,
        forms.RotationDependenceChartForm,
        forms.RotationHistogramChartForm
    )
