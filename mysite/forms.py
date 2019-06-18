from django import forms 
from .models import Usuario

class UsuarioCreateForm(forms.Form):
    
    nome = forms.CharField(label='Nome ',max_length=50)
    login = forms.CharField(label='Login', max_length=50)
    senha = forms.CharField(label='Senha ',max_length=10)
    class meta:
        fields = ('nome', 'login', 'senha')
        model = Usuario