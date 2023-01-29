from django.shortcuts import render
from django.views.generic import View, ListView, DetailView

from .models import Post, Collage


# def home(request):
#     """
#     Представление, для главной страницы.
#     """
#     return render(request, 'index.html')
class Home(ListView):
    raise_exception = True
    model = Collage
    template_name = 'index.html'
    context_object_name = 'collage'


class PhotoList(ListView):
    raise_exception = True
    model = Post
    template_name = 'photo.html'
    context_object_name = 'photo'


class PhotoDetail(DetailView):
    model = Post
    template_name = 'photo_id.html'
    context_object_name = 'photo'
