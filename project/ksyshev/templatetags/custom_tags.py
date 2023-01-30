from datetime import datetime

from django.core.paginator import Paginator
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

@register.inclusion_tag('all_photos.html', takes_context=True)
def get_photo(context):
    photos = Post.objects.order_by('id')
    p = Paginator(photos, 4)
    request = context['request']
    page_num = request.GET.get('page',1)
    page = p.page(page_num)

    return {'photos': photos, 'items': page}


@register.inclusion_tag('all_collage.html')
def get_callage():
    collages = Collage.objects.all()
    return {'collages': collages}

