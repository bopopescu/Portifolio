from django.shortcuts import render, redirect
from .forms import UsuarioCreateForm
from mysite.models import Usuario
from django.http import HttpResponse
from django.contrib import messages
import datetime

# Create your views here.

def index(request):
    context = {}
    return render(request, "index.html", context)

def login(request):
    context = {}
    return render(request, "login.html", context)

def cadastro(request):
    context = {}
    return render(request, "cadastro.html", context)

def logedin(request):
    if request.session.has_key('username'):
        return True
    return False

def logout(request):
    request.session.flush()
    return redirect('login')