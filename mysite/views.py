from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, "index.html", context)

def login(request):
    form = ()
    context = {}
    return render(request, "login.html", context)

def signin(request):
    usuario = Usuario.objects.all()

    if request.method =="POST":
        if form.is_valid():
            n = form.cleaned_data.get('login')
            s = form.cleaned_data.get('senha')

            for usuario in usuario:
                if (usuario.login == n ) and (usuario.senha == s):
                    return redirect ('home.html')
    return render(request, 'login.html')