from django import forms
from mysite.models import Usuario

class LoginForm(forms.ModelForm):
    login_form = forms.Charfield(max_length=20)
    senha_form = forms.Charfield(max_length=20)


