from .models import Post, Collage, Video
from django.dispatch import receiver
from django.db.models.signals import m2m_changed, post_delete, post_save, pre_delete




@receiver(pre_delete, sender=Post)
def image_delete(sender, instance, **kwargs):
    if instance.image.name:
        instance.image.delete(False)


@receiver(pre_delete, sender=Collage)
def collage_delete(sender, instance, **kwargs):
    if instance.image.name:
        instance.image.delete(False)


@receiver(pre_delete, sender=Video)
def video_delete(sender, instance, **kwargs):
    if instance.video.name:
        instance.video.delete(False)
