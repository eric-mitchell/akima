# urls.py
from django.urls import path

from portal.views import ArticleList, ArticleDetail, SaveArticleAnnotations

urlpatterns = [
    path("articles/", ArticleList.as_view(), name="article-list"),
    path("articles/<str:pk>/", ArticleDetail.as_view(), name="author-detail"),
    path(
        "save-annotations/", SaveArticleAnnotations.as_view(), name="save-annotations"
    ),
]
