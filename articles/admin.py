from django.contrib import admin
from django.utils.html import mark_safe

from articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date',)
    list_filter = ('author', 'date')
    search_fields = ('author', 'date')
    readonly_fields = ['article_image',]

    def article_image(self, obj):
        return mark_safe(f'<img src="{obj.url}" width="{obj.width}" height={obj.height} />')
