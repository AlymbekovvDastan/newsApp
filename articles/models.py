import os

from django.contrib.auth import get_user_model
from django.db import models
from django_quill.fields import QuillField

from PIL import Image


class Article(models.Model):
    title = models.CharField(max_length=350)
    image = models.ImageField(upload_to='images/')
    body = QuillField()
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        width, height = img.size
        if width*height > 740*420:
            img.thumbnail((740, 420))
            img.save(self.image.path)

    def __str__(self):
        return self.title

