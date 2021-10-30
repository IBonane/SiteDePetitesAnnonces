
from django.conf.urls.static import static
from django.urls import path

from admin_blog.views import dashboard, MesAnnonces, CreerAnnonce, EditerAnnonce, SupprimerAnnonce
from blog import settings

app_name = "tableau_de_board"
urlpatterns = [
                  path('compte/tableau_de_bord/', dashboard, name="dashboard"),
                  path('compte/mes_annonces/', MesAnnonces.as_view(), name="mes_annonces"),
                  path('compte/Creer_annonce/', CreerAnnonce.as_view(), name="creer"),
                  path('compte/modifier_annonce/<str:slug>/', EditerAnnonce.as_view(), name="editer"),
                  path('compte/supprime_annonce/<str:slug>/', SupprimerAnnonce.as_view(), name="supprimer"),
              ]
