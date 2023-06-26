from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


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
        verbose_name='Текст записи',
        help_text='Введите текст записи'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )

    def __str__(self):
        return self.text

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
        User,
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
