from django.urls import path

from articles.views import ArticleListView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='article_update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='article_delete'),
]