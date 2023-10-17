from django.db import models
from django.utils import timezone

class RegistroCliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    data = models.DateTimeField(default=timezone.now)
    descricao = models.TextField()
    valor = models.FloatField()
    recebimento = models.BooleanField(blank=True, null=True)

def __str__(self) -> str:
    return f'{self.nome}'

