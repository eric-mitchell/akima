from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, View

from portal.models import Article, ArticleAnnotation


class ArticleList(ListView):
    model = Article


class ArticleDetail(DetailView):
    model = Article


class SaveArticleAnnotations(View):
    def post(self, request):
        uuid = request.POST.get("uuid")
        annotations = request.POST.get("annotations")

        article_annotation = ArticleAnnotation(
            article=Article.objects.get(uuid=uuid), annotation=annotations
        )
        article_annotation.save()

        return HttpResponseRedirect("/portal/articles")
