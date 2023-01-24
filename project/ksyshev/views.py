from django.shortcuts import render
from django.views.generic import View


def home(request):
    """
    Представление, для главной страницы.
    """
    return render(request, 'index.html')

