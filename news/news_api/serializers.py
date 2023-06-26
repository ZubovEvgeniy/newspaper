from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from .models import News, Comments


class NewsSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = News
        fields = ('__all__')


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Comments
        fields = ('__all__')
