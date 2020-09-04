from django.views.generic import ListView


class ArticleList(ListView):
    model = Article
