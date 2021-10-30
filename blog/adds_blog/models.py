from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from accounts_blog.models import CustomUser


'''class Categorie(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name'''


class Article(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    desc = models.TextField(blank=True, verbose_name="Description")
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Prix en FR-CFA")
    #category = models.ForeignKey(Categorie, on_delete=models.CASCADE, verbose_name="Categorie", default=True, null=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='articles')
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
