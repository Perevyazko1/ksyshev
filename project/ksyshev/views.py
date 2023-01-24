from django.shortcuts import render
from django.views.generic import View, ListView

from .models import Post


def home(request):
    """
    Представление, для главной страницы.
    """
    return render(request, 'index.html')


class PhotoList(ListView):
    raise_exception = True
    model = Post
    template_name = 'photo.html'
    context_object_name = 'photo'


