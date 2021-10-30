from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from adds_blog.models import Article


def dashboard(request):
    return render(request, "admin_blog/dashboard.html")


class MesAnnonces(ListView):
    model = Article
    template_name = "admin_blog/article_list.html"
    context_object_name = "annonces"


class CreerAnnonce(CreateView):
    model = Article
    template_name = "admin_blog/article_create.html"
    fields = [
        'title',
        'desc',
        'price',
        'author',
        'image',
    ]

    success_url = reverse_lazy('tableau_de_board:mes_annonces')


class EditerAnnonce(UpdateView):
    model = Article
    template_name = "admin_blog/article_edit.html"
    fields = [
        'title',
        'desc',
        'price',
        'image',
    ]
    success_url = reverse_lazy('tableau_de_board:mes_annonces')


class SupprimerAnnonce(DeleteView):
    model = Article
    template_name = "admin_blog/article_confirm_delete.html"
    context_object_name = "delete"
    success_url = reverse_lazy('tableau_de_board:mes_annonces')
