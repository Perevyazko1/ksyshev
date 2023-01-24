from django.urls import path
from django.views.decorators.cache import cache_page

from .views import home

urlpatterns = [
    path('', home, name='home'),
]