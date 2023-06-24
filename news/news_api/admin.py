from django.contrib import admin
from .models import News, Comments


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'text',
        'author',
    )
    search_fields = (
        'name',
        'text',
    )
    list_filter = (
        'pub_date',
    )


admin.site.register(News)
admin.site.register(Comments)
