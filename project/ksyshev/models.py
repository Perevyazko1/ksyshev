from django.db import models
from django.urls import reverse


class Post(models.Model):
    class Meta:
        verbose_name = u"Фотку"
        verbose_name_plural = u"Фотки"

    date_load = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
    image = models.ImageField(upload_to='static/images/', default=None)

    def get_absolute_url(self):
        return reverse('photo_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.date_load}| {self.image}'


class Collage(models.Model):
    class Meta:
        verbose_name = u"Коллаж"
        verbose_name_plural = u"Коллажи"

    date_load = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
    image = models.ImageField(upload_to='static/collage/', default=None)
