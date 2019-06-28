from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mysite.views import index, login, cadastro, portifolio_sites, sobre
from . import views
admin.autodiscover()

urlpatterns = [

    path('', views.index, name='index'),
    path('home',views.index, name='home'),
    path('login', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('portifolio', views.portifolio_sites, name='portifolio'),
    path('sobre', views.sobre, name='sobre')

]