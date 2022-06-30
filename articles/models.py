from django.contrib.auth import get_user_model
from django.db import models
from django_quill.fields import QuillField


class Article(models.Model):
    title = models.CharField(max_length=350)
    body = QuillField()
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
