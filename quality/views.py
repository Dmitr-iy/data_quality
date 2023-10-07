from .models import ConcentrateQuality
from django.shortcuts import render, redirect
import json


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
