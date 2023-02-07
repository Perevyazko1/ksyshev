from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Collage, Video, Ip


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('date_load', 'get_html_photo', 'id')
    list_filter = ('date_load',)

    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.image.url}'width=50")


class VideoAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('date_load', 'get_html_video', 'id')
    list_filter = ('date_load',)

    def get_html_video(self, object):
        return mark_safe(f"<video src='{object.video.url}'width=50></video>")


class CollageAdmin(admin.ModelAdmin):
    model = Collage
    list_display = ('date_load', 'get_html_collage', 'id')
    list_filter = ('date_load',)

    def get_html_collage(self, object):
        return mark_safe(f"<img src='{object.image.url}'width=50")


class IpAdmin(admin.ModelAdmin):
    model = Ip
    list_display = ('ip','date_visit')
    list_filter = ('date_visit',)



admin.site.register(Post, PostAdmin)
admin.site.register(Collage, CollageAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Ip, IpAdmin)

