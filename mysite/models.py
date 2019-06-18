from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=50)
    login = models.CharField(max_length=20)
    senha = models.CharField(max_length=20)
    

    def __str__(self):
        return self.nome