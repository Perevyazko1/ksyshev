from django.urls import path
from django.views.decorators.cache import cache_page

from .views import home, PhotoList

urlpatterns = [
    path('', home, name='home'),
    path('photo/', PhotoList.as_view(), name='photo'),
]