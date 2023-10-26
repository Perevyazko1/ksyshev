from django.http import FileResponse
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView

from .models import Post, Collage, Ip, Video
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, viewsets

from .models import Post
from .serializers import *



# def home(request):
#     """
#     Представление, для главной страницы.
#     """
#     return render(request, 'index.html')
class Home(ListView):
    raise_exception = True
    model = Collage
    template_name = 'all_collage.html'
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

# @api_view(['GET'])
# def post_api(request, post_id):
#     if request.method == 'GET':
#         try:
#             post = Post.objects.get(id = post_id)
#         except:
#             return Response(status = status.HTTP_400_BAD_REQUEST)
#
#         setattr(post, 'likesCount', post.likesCount + 1)
#         post.save()
#         return Response(post.likesCount, status.HTTP_200_OK)


class PostViewset(viewsets.ModelViewSet):
   queryset = Post.objects.all()
   serializer_class = PostSerializer

   def get_queryset(self):
       queryset = Post.objects.all()
       photo_id = self.request.query_params.get('photo_id', None)
       if photo_id is not None:
           queryset = queryset.filter(id=photo_id)
       return queryset


class VideoViewset(viewsets.ModelViewSet):
   queryset = Video.objects.all()
   serializer_class = VideoSerializer

   def get_queryset(self):
       queryset = Video.objects.all()
       video_id = self.request.query_params.get('video_id', None)
       if video_id is not None:
           queryset = queryset.filter(id=video_id)
       return queryset


class CollageViewset(viewsets.ModelViewSet):
   queryset = Collage.objects.all()
   serializer_class = CollageSerializer

   def get_queryset(self):
       queryset = Collage.objects.all()
       collage_id = self.request.query_params.get('collage_id', None)
       if collage_id is not None:
           queryset = queryset.filter(id=collage_id)
       return queryset
