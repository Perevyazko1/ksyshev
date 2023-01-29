from datetime import datetime
from django.utils import timezone

from django import template


from ..models import Post, Collage

register = template.Library()



@register.simple_tag()
def get_collage_one():
    return Collage.objects.get(id=1).image

@register.simple_tag()
def get_collage_two():
    return Collage.objects.get(id=2).image

@register.simple_tag()
def get_collage_three():
    return Collage.objects.get(id=3).image

@register.simple_tag()
def get_collage_four():
    return Collage.objects.get(id=4).image


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    return d.urlencode()


@register.simple_tag()
def current_hour():
    return timezone.localtime(timezone.now()).hour

@register.inclusion_tag('all_photos.html')
def get_photo():
    photos = Post.objects.all()
    return {'photos' : photos}


@register.inclusion_tag('all_collage.html')
def get_callage():
    collages = Collage.objects.all()
    return {'collages' : collages}

