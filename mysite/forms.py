from django import forms
from mysite.models import Usuario

class LoginForm(forms.ModelForm):
    login_form = forms.Charfield(max_length=20)
    senha_form = forms.Charfield(max_length=20)


class CadastroForm(forms.ModelForm):
nome = forms.CharField(max_length=50)
login = forms.CharField(max_length=20)
senha = forms.CharField(max_length=20)
    class Meta:
    	fields = ('nome', 'login', 'senha')
    	models = Usuario

	
		
