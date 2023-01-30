from django.urls import path
from django.views.decorators.cache import cache_page

from .views import Home, PhotoList, PhotoDetail, video, contact

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('video/', video, name='video'),
    path('contact/', contact, name='contact'),
    path('photo/', PhotoList.as_view(), name='photo'),
    path('<int:pk>', PhotoDetail.as_view(), name='photo_detail'),

]
