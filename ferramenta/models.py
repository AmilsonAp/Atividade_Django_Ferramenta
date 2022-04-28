from django.db import models

# Create your models here.
class Ferramenta(models.Model):
    codigo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    duracao = models.DateField()
    dataCadastro = models.DateField()
    funcao = models.CharField(max_length=100)

    def __str__(self):
        return self.codigo
        return self.descricao
        return self.tipo
        return self.material
        return self.duracao
        return self.dataCadastro
        return self.funcao

