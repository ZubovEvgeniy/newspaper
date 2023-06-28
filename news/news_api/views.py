from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from .mixins import LikedMixin
from .models import Comments, News
from .permissions import IsAuthorAdminModerOrReadOnly
from .serializers import CommentsSerializer, NewsSerializer


class NewsViewSet(LikedMixin, viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthorAdminModerOrReadOnly, )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthorAdminModerOrReadOnly, )

    def get_queryset(self):
        news_id = self.kwargs.get('news_id')
        comments_queryset = Comments.objects.filter(news=news_id)
        return comments_queryset

    def perform_create(self, serializer):
        news = get_object_or_404(News, pk=self.kwargs.get('news_id'))
        serializer.save(author=self.request.user, news=news)
