from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mysite.views import index, login, cadastro
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),

]