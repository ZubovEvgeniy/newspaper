from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)
from django.contrib.contenttypes.models import ContentType
from django.db import models

comment_limit = 1


class User(AbstractUser):

    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=150,
        unique=True
    )
    is_staff = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Like(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='likes',
        on_delete=models.CASCADE,
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'


class News(models.Model):

    pub_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )
    name = models.CharField(
        verbose_name='Заголовок новости',
        max_length=256
    )
    text = models.TextField(
        verbose_name='Текст новости',
        help_text='Введите текст новости'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )
    likes = GenericRelation(Like)

    def __str__(self):
        return self.text

    def less_comments(self):
        return (Comments.objects.all()
                .filter(news=self).order_by("-id")[:comment_limit])

    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def total_comments(self):
        return Comments.objects.all().filter(news=self).count()

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comments(models.Model):

    pub_date = models.DateTimeField(
        'Дата создания',
        auto_now_add=True,
    )
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
    )
    text = models.TextField(
        'Текст комментария',
        help_text='Напишите комментарий',
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
