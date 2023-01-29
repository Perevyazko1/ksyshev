from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Collage

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('date_load', 'get_html_photo', 'id')
    list_filter = ('date_load',)


    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.image.url}'width=50")

class CollageAdmin(admin.ModelAdmin):
    model = Collage
    list_display = ('date_load', 'get_html_photo', 'id')
    list_filter = ('date_load',)


    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.image.url}'width=50")

admin.site.register(Post, PostAdmin)
admin.site.register(Collage, CollageAdmin)


