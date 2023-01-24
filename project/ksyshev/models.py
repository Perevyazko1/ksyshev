from django.db import models


class Post(models.Model):
    date_load = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
    image = models.ImageField(upload_to='static/images/', default=None)
