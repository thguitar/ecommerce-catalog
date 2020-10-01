from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(
        max_length=100
    )
    descricao = models.CharField(
        max_length=100
    )
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0.00)
        ]
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nome
