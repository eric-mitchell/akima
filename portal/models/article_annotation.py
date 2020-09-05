import json

from django.db import models


class ArticleAnnotation(models.Model):
    article = models.ForeignKey("Article", on_delete=models.CASCADE)
    annotation = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    @property
    def annotation_sentences(self):
        if self.annotation:
            result = []
            parsed = json.loads(self.annotation)
            for line in parsed:
                result.append(line[1])

            return result

        return None
