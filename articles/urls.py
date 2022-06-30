from django.urls import path

from articles.views import ArticleListView, ArticleCreateView, ArticleUpdateView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('update/', ArticleUpdateView.as_view(), name='article_update'),
]