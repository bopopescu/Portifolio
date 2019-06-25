from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=50)
    login = models.CharField(max_length=20)
    senha = models.CharField(max_length=20)
    

    def __str__(self):
        return self.nome

class MysiteManager(models.Manager):

	def search(self,query):
		return self.get_queryset().filter(
			models.Q(titulo_icontains=query) | \
			models.Q(descricao_icontains=query)
		)

class Portifolio(models.Model):
	id_atualizacao = models.AutoField(primary_key=True)
	titulo = models.CharField(max_length=35)
	legenda = models.CharField(max_length=150)
	descricao = models.TextField('Descrição', blank=True)
	imagem = models.ImageField(
		upload_to='mysite\static\img', verbose_name='Imagem', null=True, blank=True 
		)
	atualizado_em = models.DateTimeField('Atualizdo em ', auto_now_add=True)
	objects = MysiteManager()

	def __str__(self):
		return self.titulo

	class meta:
		verbose_name = 'Portifolio'
		verbose_name_plural = 'Portifolios'