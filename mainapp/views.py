from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

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
    register_form = UserCreationForm()

    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid:
            register_form.save()
            return redirect('home')

    return render(request, 'users/register.html', {
        'title': 'Registro',
        'register_form': register_form
    })