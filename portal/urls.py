# urls.py
from django.shortcuts import redirect
from django.urls import path

from portal.views import ArticleList, ArticleDetail, SaveArticleAnnotations

urlpatterns = [
    path("", lambda req: redirect("/articles/")),
    path("articles/", ArticleList.as_view(), name="article-list"),
    path("articles/<str:pk>/", ArticleDetail.as_view(), name="author-detail"),
    path(
        "save-annotations/", SaveArticleAnnotations.as_view(), name="save-annotations"
    ),
]
