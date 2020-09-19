from django.shortcuts import render
from blog.models import Article, Category

# Create your views here.
def articles(request):
    articles = Article.objects.all()

    return render(request, 'articles/list.html', {
        'title': 'Artículos',
        'articles': articles
    })