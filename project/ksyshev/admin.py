from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post

class PostAdmin(admin.ModelAdmin):
    model = Post


admin.site.register(Post, PostAdmin)


