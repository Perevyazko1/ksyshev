from django.shortcuts import render
from django.views.generic import View, ListView, DetailView

from .models import Post, Collage, Ip, Video


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


class VideoList(ListView):
    raise_exception = True
    model = Video
    template_name = 'video.html'
    context_object_name = 'video'


class PhotoDetail(DetailView):
    model = Post
    template_name = 'photo_id.html'
    context_object_name = 'photo'


# Метод для получения айпи
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR') # В REMOTE_ADDR значение айпи пользователя
    return ip



def contact(request):
    ip = get_client_ip(request)
    # if request.method == 'POST':
    #     form = SendMailForm(request.POST)
    #     data = request.POST.get('name')
    #
    #     if form.is_valid():
    #         print(form.cleaned_data)
    # else:
    #     form = SendMailForm()
    #     print(form)
    if Ip.objects.filter(ip=ip).exists():
        ip_save=Ip.objects.filter(ip=ip)
        ip_save.update(ip=ip)
    else:
        Ip.objects.create(ip=ip)
    return render(request, 'contact.html')


# def video(request):
#     return render(request, 'video.html')



