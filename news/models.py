from django.contrib.auth import get_user_model
from django.db import models
from django_quill.fields import QuillField


class Post(models.Model):
    title = models.CharField(max_length=350)
    description = QuillField()
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, blank=True, null=True)
    date_of_publication = models.DateTimeField()

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
