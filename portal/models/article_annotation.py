from django.db import models


class ArticleAnnotation(models.Model):
    article = models.ForeignKey("Article", on_delete=models.CASCADE)
    annotation = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
