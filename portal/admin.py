from django.contrib import admin
from django.utils.safestring import mark_safe

from portal.models import Article, ArticleAnnotation

admin.site.site_header = "Article Annotation Administration"


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["uuid", "title", "url"]


class ArticleAnnotationAdmin(admin.ModelAdmin):
    list_display = [
        "get_uuid",
        "get_title",
        "get_annotation_sentences",
    ]

    def get_uuid(self, obj):
        return obj.article.uuid

    def get_title(self, obj):
        return obj.article.title

    def get_annotation_sentences(self, obj):
        if obj.annotation_sentences:
            return mark_safe("<br><br>".join(obj.annotation_sentences))

        return obj.annotation_sentences


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleAnnotation, ArticleAnnotationAdmin)
