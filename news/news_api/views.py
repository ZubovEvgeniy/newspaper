from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from .models import News, Comments
from .mixins import LikedMixin
from .serializers import NewsSerializer, CommentsSerializer
from .permissions import AuthorOrReadOnly


class NewsViewSet(LikedMixin, viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (AuthorOrReadOnly, )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    permission_classes = (AuthorOrReadOnly, )

    def get_queryset(self):
        news_id = self.kwargs.get('news_id')
        comments_queryset = Comments.objects.filter(news=news_id)
        return comments_queryset

    def perform_create(self, serializer):
        news = get_object_or_404(News, pk=self.kwargs.get('news_id'))
        serializer.save(author=self.request.user, news=news)
