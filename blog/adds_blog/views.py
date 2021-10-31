from django.shortcuts import render
from django.views.generic import ListView, DetailView
from adds_blog.models import Article


class Home(ListView):
    model = Article
    template_name = "compte/index.html"
    context_object_name = "articles"


class ArticleDetail(DetailView):
    model = Article
    template_name = "compte/article_detail.html"
    context_object_name = "article"


def search(request):
    query = request.GET["article"]
    liste_articles = Article.objects.filter(title__icontains=query)
    return render(request, "compte/search.html", {"liste_articles": liste_articles})
