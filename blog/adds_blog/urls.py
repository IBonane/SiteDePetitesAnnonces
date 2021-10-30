from django.urls import path

from adds_blog.views import Home, ArticleDetail, search #category_maison


app_name = "articles"
urlpatterns = [
                  path('', Home.as_view(), name="home"),
                  path('<str:slug>/', ArticleDetail.as_view(), name='article'),
                  path('article/recherche', search, name='search'),
                  #path('article/categorie', category_maison, name='category_maison'),
              ]
