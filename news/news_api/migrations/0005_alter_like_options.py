# Generated by Django 4.2.2 on 2023-06-28 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_api', '0004_like_delete_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'verbose_name': 'Лайк', 'verbose_name_plural': 'Лайки'},
        ),
    ]