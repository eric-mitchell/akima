# urls.py
from django.urls import path

from portal.views import ArticleList, ArticleDetail

urlpatterns = [
    path("articles/", ArticleList.as_view()),
    path("articles/<str:pk>/", ArticleDetail.as_view(), name="author-detail"),
]
