from django.contrib import admin
from usuarios.models import RegistroCliente

# # Register your models here.
@admin.register(RegistroCliente)
class RegistroClienteAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome', 'data', 'descricao', 'valor', 'recebimento',
    list_filter = 'data', 'recebimento',
    ordering = '-id',
