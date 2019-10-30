from django.conf import settings
from django.db import models
from django.utils import timezone

# classe com o objeto que sera visualizado
class Objeto(models.Model):
	nome = models.CharField(max_length=100, blank=False)
	descricao = models.CharField(max_length=2000, blank=True)
	id_marcador = models.IntegerField()
	path_modelos = models.CharField(max_length=2000, blank=True)
	name_OBJ = models.CharField(max_length=2000, blank=True)
	name_MTL = models.CharField(max_length=2000, blank=True)
	def _str_(self):
		return self.nome
	def get_id_marcador(self):
		return self.id_marcador
	def get_name_OBJ(self):
		return self.name_OBJ
	def get_path_modelos(self):
		return self.path_modelos
	def get_name_MTL(self):
		return self.name_MTL
	def get_descricao(self):
		return self.descricao