from django.views.generic import ListView, DetailView

from portal.models import Article


class ArticleList(ListView):
    model = Article


class ArticleDetail(DetailView):
    model = Article
