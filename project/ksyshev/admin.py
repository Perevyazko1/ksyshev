from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('date_load', 'get_html_photo')

    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.image.url}'width=50")


admin.site.register(Post, PostAdmin)


