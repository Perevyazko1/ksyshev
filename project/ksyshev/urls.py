from django.urls import path

from .views import Home, PhotoList, PhotoDetail, VideoList, contact, PostViewset,VideoViewset,CollageViewset

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('video/', VideoList.as_view(), name='video'),
    path('contact/', contact, name='contact'),
    path('photo/', PhotoList.as_view(), name='photo'),
    path('<int:pk>', PhotoDetail.as_view(), name='photo_detail'),
    path('api-photo/', PostViewset.as_view({'get': 'list'}), name='api-photo'),
    path('api-video/', VideoViewset.as_view({'get': 'list'}), name='api-video'),
    path('api-collage/', CollageViewset.as_view({'get': 'list'}), name='api-collage'),

]
