from django.contrib import admin
from django.utils.html import mark_safe

from news.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'date_of_publication',)
    list_filter = ('created_by', 'date_of_publication')
    search_fields = ('created_by', 'date_of_publication')
    readonly_fields = ['post_images']

    def post_images(self, obj):
        html = ''

        for img in obj.images.all():
            html += f'<img src="{img.url}" width="{img.width}" height={img.height} />'

        return mark_safe(html)
