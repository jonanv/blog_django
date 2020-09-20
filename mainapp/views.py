from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm

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