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


class Video(models.Model):
    class Meta:
        verbose_name = u"Видео"
        verbose_name_plural = u"Видео"

    date_load = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
    video = models.FileField(upload_to='static/video/', default=None)


    def __str__(self):
        return f'{self.date_load}| {self.video}'




class Ip(models.Model): # наша таблица где будут айпи адреса
    class Meta:
        verbose_name = u"Посещение"
        verbose_name_plural = u"Посещения"

    ip = models.CharField(max_length=100)
    date_visit = models.DateTimeField(auto_now=True, verbose_name='Дата посещения')

    def __str__(self):
        return self.ip