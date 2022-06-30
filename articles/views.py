from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
# from django.shortcuts import render

from articles.forms import ArticleForm
from articles.models import Article


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    context_object_name = 'article_list'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_create.html'
    success_url = reverse_lazy('article_list')
    login_url = '/'


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_update.html'
    success_url = reverse_lazy('article_list')
    login_url = '/'
