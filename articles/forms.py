from django import forms

from articles.models import Article


class ArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Article
        fields = ('title', 'body', 'image')
