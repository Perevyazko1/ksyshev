from rest_framework import serializers
from .models import Post, Collage, Video


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('date_load', 'image')


class CollageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collage
        fields = ('date_load', 'image')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('date_load', 'video')
