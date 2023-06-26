from django.contrib import admin
from .models import News, Comments, User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'username',
        'email',
        'is_staff',
        )
    fields = (
        'username',
        'email',
        'is_staff',
        )


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'text',
        'author',
        'pub_date',
    )
    search_fields = (
        'name',
        'text',
    )
    list_filter = (
        'pub_date',
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'text',
    )


admin.site.register(User)
admin.site.register(News)
admin.site.register(Comments)
