from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
]
