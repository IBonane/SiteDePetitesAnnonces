from django.contrib.auth import views

from django.urls import path

from accounts_blog.views import signup, profile

app_name = "compte"
urlpatterns = [
                  path('compte/nouveau/', signup, name='signup'),
                  path('compte/connexion/', views.LoginView.as_view(), name='login'),
                  path('compte/deconnexion/', views.LogoutView.as_view(), name='logout'),
              ]