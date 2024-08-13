from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime, date
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    today = datetime.now()
    current_time = today.strftime("%H:%M:%S")
    current_date = date.today()
    msg = f"""Дата: {current_date} <br> Текущее время: {current_time}
                <br> <a href='/'>Вернуться на главную<a/>"""
    return HttpResponse(msg)


def workdir_view(request):
    directory = "first_project/" # Здесь не понял, какую именно папку просмотреть
    files = os.listdir(directory)
    msgs = f"""Файлы рабочей дериктории: <br> {files} 
                <br> <a href='/'>Вернуться на главную<a/>
            """
    return HttpResponse(msgs)