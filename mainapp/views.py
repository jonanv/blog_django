from django.shortcuts import render

# Create your views here.

# Metodo de la vista home.html
def home(request):
    return render(request, 'mainapp/home.html', {
        'title': 'Inicio'
    })