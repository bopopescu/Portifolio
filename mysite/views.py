from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Portifolio, Contato
from .forms import UsuarioCreateForm, ContatoForm
from django.http import HttpResponse
from django.contrib import messages
import datetime


# Create your views here.

def index(request):
    portifolio = Portifolio.objects.all()
    context = {
        'portifolio': portifolio
    }
    return render(request, "index.html", context)

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid:
            Contato.objects.create(
                email = form.cleaned_data.get('email'),
                nome = form.cleaned_data.get('nome'),
                telefone = form.cleaned_data.get('telefone'),
                celular = form.cleaned_data.get('celular'),
                mensagem = form.cleaned_data.get('mensagem')
                )
            return redirect('contato_detalhe')
    else:
        form = ContatoForm()

    context = {
        'form': form
    }
    return render(request, "contato.html",context)

def portifolio_sites(request):
    portifolio = Portifolio.objects.all()
    context = {
        'portifolio': portifolio
    }
    return render(request, "portifolio_sites.html", context)

def sobre(request):
    context = {}
    return render(request, "sobre.html", context)

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