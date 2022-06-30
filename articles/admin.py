from django.contrib import admin
from django.utils.html import mark_safe

from articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date',)
    list_filter = ('author', 'date')
    search_fields = ('author', 'date')
    readonly_fields = ['article_images',]

    def article_images(self, obj):
        html = ''

        for img in obj.images.all():
            html += f'<img src="{img.url}" width="{img.width}" height={img.height} />'

        return mark_safe(html)
