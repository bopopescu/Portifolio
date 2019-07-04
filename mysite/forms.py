from django import forms
from .models import Usuario, Contato

class UsuarioCreateForm(forms.Form):
    
    nome = forms.CharField(label='Nome ',max_length=50)
    login = forms.CharField(label='Login', max_length=50)
    senha = forms.CharField(label='Senha ',max_length=10)
    class meta:
        fields = ('nome', 'login', 'senha')
        model = Usuario

class ContatoForm(forms.Form):
	email = forms.CharField(label='Email ',max_length=50)
	nome = forms.CharField(label='Nome ',max_length=50)
	Telefone = forms.CharField(label='Telefone ',max_length=15)
	Celular = forms.CharField(label='Celular ',max_length=15)
	mensagem = forms.CharField(label='Mensagem ',max_length=300)
	
