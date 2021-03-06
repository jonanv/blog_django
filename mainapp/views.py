from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# Metodo de la vista home.html
def home(request):

    return render(request, 'mainapp/home.html', {
        'title': 'Home'
    })

# Metodo de la vista about.html
def about(request):

    return render(request, 'mainapp/about.html', {
        'title': 'About'
    })

def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        register_form = RegisterForm()

        if request.method == 'POST':
            register_form = RegisterForm(request.POST)

            if register_form.is_valid:
                register_form.save()
                messages.success(request, 'Te has registrado satisfactoriamente')
                return redirect('home')
            else:
                register_form = RegisterForm()

        return render(request, 'users/register.html', {
            'title': 'Registro',
            'register_form': register_form
        })

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, 'No te has identificado correctamente')

        return render(request, 'users/login.html', {
            'title': 'Identificación'
        })

def logout_user(request):
    logout(request)
    return redirect('login')