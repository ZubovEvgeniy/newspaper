from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""
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

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Likes(models.Model):
    news = models.ForeignKey(
        News,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Новость',
    )
    liked_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Поставил лайк',
    )
    like = models.BooleanField(
        'Like',
        default=False,
    )

    def __str__(self):
        return self.liked_by

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'


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
