from django import forms
from django_quill.forms import QuillFormField

from articles.models import Article


class ArticleForm(forms.Form):
    body = QuillFormField()

    class Meta:
        model = Article
        fields = ('title', 'body', 'date', )
