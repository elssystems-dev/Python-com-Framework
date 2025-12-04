from django.contrib import admin
from .models import Categoria, Receita

# Register your models here.

# Forma 1: Usando decorator
@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    ...
# Forma 2: Registrando manualmente
class CategoriaAdmin(admin.ModelAdmin):
    ...
admin.site.register(Categoria, CategoriaAdmin)
