from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import News, Comments, User
from . import services


class FanSerializer(serializers.ModelSerializer):

    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'username',
            'full_name',
        )

    def get_full_name(self, obj):
        return obj.get_full_name()


class CommentsSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Comments
        fields = ('__all__')


class NewsSerializer(serializers.ModelSerializer):

    comments = CommentsSerializer(many=True, source="less_comments")
    is_fan = serializers.SerializerMethodField()
    author = SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = News
        fields = (
            'id',
            'author',
            'is_fan',
            'pub_date',
            'name',
            'text',
            'total_likes',
            'total_comments',
            'comments',
        )

    def get_is_fan(self, obj) -> bool:

        user = self.context.get('request').user
        return services.is_fan(obj, user)
