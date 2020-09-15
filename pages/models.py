from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_lenght=50, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    slug = models.CharField(unique=True, max_lenght=150, verbose_name='URL amigable')
    public = models.BooleanField(verbose_name='Visible')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado')

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = "Páginas"

    def __str__(self):
        return self.title