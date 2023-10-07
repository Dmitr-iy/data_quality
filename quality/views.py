from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import ConcentrateQuality
from django.shortcuts import render, redirect
import json
from django.db.models import Avg, Min, Max
from rest_framework import viewsets
from .serializers import ConcentrateQualitySerializer


@login_required
def add_concentrate(request):
    user = request.user

    if request.method == 'POST':
        excel_data = request.POST.get('data-json')

        # Проверка наличия данных
        if not excel_data:
            return render(request, 'add_concentrate.html', {'error': 'No data received'})

        # Преобразование JSON-строки в список данных
        try:
            data_list = json.loads(excel_data)
        except json.JSONDecodeError:
            return render(request, 'add_concentrate.html', {'error': 'Invalid JSON data'})

        # Получение текущего пользователя
        user = request.user

        # Создание и сохранение объектов ConcentrateQuality в базе данных
        for data in data_list:
            concentrate_quality = ConcentrateQuality(
                name=data[0],
                month=data[1],
                iron=data[2],
                silicon=data[3],
                aluminum=data[4],
                calcium=data[5],
                sulfur=data[6],
                user=user
            )
            concentrate_quality.save()
        return redirect('add_concentrate')

    else:
        return render(request, 'add_concentrate.html', {'user': user})


def report(request):
    if request.method == 'POST':
        selected_month = request.POST.get('selected_month')

        report_data = ConcentrateQuality.objects.filter(month=selected_month).aggregate(
            average_iron=Avg('iron'),
            average_silicon=Avg('silicon'),
            average_aluminum=Avg('aluminum'),
            average_calcium=Avg('calcium'),
            average_sulfur=Avg('sulfur'),
            min_iron=Min('iron'),
            min_silicon=Min('silicon'),
            min_aluminum=Min('aluminum'),
            min_calcium=Min('calcium'),
            min_sulfur=Min('sulfur'),
            max_iron=Max('iron'),
            max_silicon=Max('silicon'),
            max_aluminum=Max('aluminum'),
            max_calcium=Max('calcium'),
            max_sulfur=Max('sulfur')
        )

        return render(request, 'report.html', {'report_data': report_data})

    return render(request, 'report.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('add_concentrate')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


class ConcentrateQualityViewSet(viewsets.ModelViewSet):
    queryset = ConcentrateQuality.objects.all()
    serializer_class = ConcentrateQualitySerializer
