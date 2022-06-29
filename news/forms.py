from django import forms
from django_quill.forms import QuillFormField

from news.models import Post


class PostForm(forms.Form):
    description = QuillFormField()

    class Meta:
        model = Post
        fields = ('title', 'description', 'date_of_publication', )
