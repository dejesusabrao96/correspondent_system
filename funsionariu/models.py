from django.db import models
from users.models import User

# Create your models here.
class Vogal(models.Model):
	vogal = models.CharField(max_length=100,null=True)
	naran_vogal = models.CharField(max_length=100,null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	hashed = models.CharField(max_length=32,null=True)
	foto = models.ImageField(upload_to='picture',null=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		# return f"{self.naran_vogal}, {self.vogal}"
		template = '{0.naran_vogal} - {0.vogal}'
		return template.format(self)

	class Meta:
		verbose_name_plural ="Vogal"


class Diresaun(models.Model):
	codigu_diresaun = models.CharField(max_length=20, null=True,unique=True)
	diresaun = models.CharField(max_length=100,null=True)
	hashed = models.CharField(max_length=32,null=True)
	vogal = models.ForeignKey(Vogal, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.diresaun 

	class Meta:
		verbose_name_plural ="Diresaun"

#class Unidade(models.Model):
#	codigu_unidade = models.CharField(max_length=20, null=True,unique=True)
#	unidade = models.CharField(max_length=100,null=True)
#	hashed = models.CharField(max_length=32,null=True)
#	vogal = models.ForeignKey(Vogal, on_delete=models.CASCADE, null=True)

#	def __str__(self):
#		return self.unidade

#	class Meta:
#		verbose_name_plural ="Unidade"

class Kargu(models.Model):
	codigu_kargu = models.CharField(max_length=20,null=True,unique=True)
	kargu = models.CharField(max_length=100, null=True)
	diresaun = models.ForeignKey(Diresaun,on_delete=models.CASCADE,null=True)
	#unidade = models.ForeignKey(Unidade,on_delete=models.CASCADE,null=True)
	hashed = models.CharField(max_length=32,null=True)

	def __str__(self):
		return self.kargu 

	class Meta:
		verbose_name_plural ="Kargo"

class Funsionariu(models.Model):
	naran_funsionariu = models.CharField(max_length=100,null=True)
	kargu = models.ForeignKey(Kargu, on_delete=models.SET_NULL,null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	hashed = models.CharField(max_length=32,null=True)
	foto = models.ImageField(upload_to='picture')
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	vogal = models.OneToOneField(Vogal, on_delete=models.CASCADE,null=True)

	def __str__(self):
		return self.naran_funsionariu 

	class Meta:
		verbose_name_plural ="Funsionariu"

	


