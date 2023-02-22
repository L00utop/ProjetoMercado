from django.db import models

class Produto(models.Model):
    descricao_produto = models.CharField(max_length=255)
    preco_normal = models.DecimalField(max_digits=8, decimal_places=2)
    preco_oferta = models.DecimalField(max_digits=8, decimal_places=2)
    indicador_oferta = models.BooleanField(default=False)