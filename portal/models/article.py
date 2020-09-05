import uuid

from django.db import models
from newspaper import Article as NewspaperArticle


class Article(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()

    html = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    article_html = models.TextField(null=True, blank=True)

    title = models.TextField(null=True, blank=True)

    summary = models.TextField(null=True, blank=True)

    publish_date = models.DateField(null=True, blank=True)

    top_image = models.URLField(null=True, blank=True)

    keywords = models.TextField(null=True, blank=True)
    authors = models.TextField(null=True, blank=True)
    images = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if len(self.html) == 0:
            a = NewspaperArticle(self.url)
            a.download()
            a.parse()
            a.nlp()

            self.html = a.html
            self.text = a.text

            self.summary = a.summary
            self.title = a.title
            self.article_html = a.article_html

            self.authors = a.authors
            self.images = a.images

            self.top_image = a.top_image
            self.keywords = a.keywords
            self.publish_date = a.publish_date

        super(Article, self).save(*args, **kwargs)

    @property
    def text_basic_html(self):
        return self.text.replace("\n", "<br>")
