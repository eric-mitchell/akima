from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, View

from portal.models import Article


class ArticleList(ListView):
    model = Article


class ArticleDetail(DetailView):
    model = Article


class SaveArticleAnnotations(View):
    def post(self, request):
        print(request.POST)
        return HttpResponseRedirect("/portal/articles")
