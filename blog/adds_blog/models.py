from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from accounts_blog.models import CustomUser


class Article(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    desc = models.TextField(blank=True, verbose_name="Description")
    price = models.IntegerField(verbose_name="Prix en FR-CFA")
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    #category = models.ForeignKey(Categorie, verbose_name="categorie", on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, upload_to='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
