from uuid import uuid4

from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


def produto_directory_path(instance, filename):
    filename = uuid4().hex + '.' + filename.split('.')[-1]
    return 'imagens/produtos/{0}'.format(filename)


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
    imagem = models.ImageField(
        null=True,
        blank=True,
        upload_to=produto_directory_path,
    )

    def __str__(self):
        return self.nome
