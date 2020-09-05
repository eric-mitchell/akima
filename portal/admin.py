from django.contrib import admin

from portal.models import Article, ArticleAnnotation

admin.site.site_header = "Article Annotation Administration"

admin.site.register(Article)
admin.site.register(ArticleAnnotation)
