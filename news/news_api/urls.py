from django.urls import include, path
from rest_framework import routers

from .views import CommentsViewSet, NewsViewSet

router = routers.DefaultRouter()

router.register('news', NewsViewSet)
router.register(
    r'news/(?P<news_id>\d+)/comments',
    CommentsViewSet,
    basename='comments',
)

urlpatterns = [
    path('v1/', include(router.urls)),
]
