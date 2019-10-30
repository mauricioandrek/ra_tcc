from django.conf import settings
from django.db import models
from django.utils import timezone

# classe com o objeto que sera visualizado
class Objeto(models.Model):
	nome = models.CharField(max_length=100, blank=False)
	descricao = models.CharField(max_length=2000, blank=True)
	id_marcador = models.IntegerField()
	path_modelo_OBJ = models.CharField(max_length=2000, blank=True)
	path_modelo_MTL = models.CharField(max_length=2000, blank=True)
	def _str_(self):
		return self.nome
	def get_id_marcador(self):
		return self.id_marcador
	def get_path_modelo_OBJ(self):
		return self.path_modelo_OBJ
	def get_path_modelo_MTL(self):
		return self.path_modelo_MTL
	def get_descricao(self):
		return self.descricao