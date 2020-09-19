from django.shortcuts import render

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

    return render(request, 'users/register.html', {
        'title': 'Registro'
    })