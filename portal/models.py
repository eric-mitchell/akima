from django.db import models
import uuid
from newspaper import Article as NewspaperArticle


# Create your models here.


class Article(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()

    html = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    summary = models.TextField(null=True, blank=True)

    publish_date = models.DateField(null=True, blank=True)

    top_image = models.URLField(null=True, blank=True)

    keywords = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if len(self.html) == 0:
            a = NewspaperArticle(self.url)
            a.download()
            a.parse()
            self.html = a.html
            self.text = a.text
            a.nlp()
            self.summary = a.summary
            self.top_image = a.top_image
            self.keywords = a.keywords
            self.publish_date = a.publish_date

        super(Article, self).save(*args, **kwargs)
