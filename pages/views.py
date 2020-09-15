from django.shortcuts import render

# Create your views here.
def page(request):
    return render(request, 'pages/page.html', {
        'title': 'Pagina',
        'page': 'Hola mundo desde la app page'
    })