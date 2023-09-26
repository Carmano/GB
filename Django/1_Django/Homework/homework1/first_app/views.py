import logging

from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)
# Create your views here.


def index(request):
    html = """
    <html>
        <head>
            <title>Мой первый Django-сайт</title>
        </head>
        <body>
            <h1>Добро пожаловать на главную страницу!</h1>
            <p>Это мой первый Django-сайт.</p>
        </body>
    </html>
    """
    # Запись в лог
    logger.info("Get main page")
    return HttpResponse(html)


def about(request):
    html = """
    <html>
        <head>
            <title>О себе</title>
        </head>
        <body>
            <h1>Обо мне</h1>
            <p>Привет! Я создал этот Django-сайт.</p>
        </body>
    </html>
    """
    # Запись в лог
    logger.info("Get page about us'")
    return HttpResponse(html)
