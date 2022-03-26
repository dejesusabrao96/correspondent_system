from django.db import models
from funsionariu.models import *

# Create your models here.
class Category(models.Model):
	cat_code = models.CharField("Kodigu Kategoria", max_length=10, null=False)
	cat_name = models.CharField("Kategoria", max_length=50, null=False)
	hashed = models.CharField(max_length=32,null=True)


	# Count Total Documents Based On Category
	def getTotDocTama(self):
		return Dokumentus.objects.filter(category=self).count()

	def getTotDocSai(self):
		return DokumentuSai.objects.filter(category=self).count()


	def __str__(self):
		return self.cat_name 

	class Meta:
		verbose_name_plural ="Category"
	

class Dokumentus(models.Model):
	klasifikasaun = (
		('Urgente', 'Urgente'),
		('Normal', 'Normal'),
		('Konfidensial', 'Konfidensial'),
		)
	status = (
					('Saved','Saved'),
					('Readed','Readed'),
					('Done','Done'),
					)
	doc_number = models.CharField("Numeru Dokumentu",max_length=20, unique=True, null=False)
	subject = models.CharField("Naran Dokumentu",max_length=100, null=False)
	date_created = models.DateTimeField(auto_now_add=True)
	given_by = models.CharField("Entrega Husi",max_length=225, null=True)
	orijen = models.CharField("Orijen Dokumentu",max_length=225, null=True)
	destinu = models.ForeignKey(Diresaun, on_delete=models.CASCADE, null=True)
	recieve_by = models.CharField("Simu Husi",max_length=225, null=True)
	folder_name = models.CharField(max_length=50, null=True)
	file_name = models.FileField(max_length=200, null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	klasifikasaun = models.CharField(max_length=32, null=True, choices=klasifikasaun)
	hashed = models.CharField(max_length=32,null=True)
	status = models.CharField(max_length=20, null=True, choices=status)
	forward_to_president = models.BooleanField(default=False)
	president_viewed = models.BooleanField(default=False)
	forward_to_admin = models.BooleanField(default=False)
	admin_viewed = models.BooleanField(default=False)
	president_despacho = models.CharField(null=True, max_length=200,blank=True)
	president_despacho_diresaun = models.ForeignKey(Diresaun,null=True,on_delete=models.CASCADE,related_name="despacho_diresaun",blank=True)
	date_despacho = models.DateTimeField(auto_now_add=True)
	forward_to_vogal = models.BooleanField(default=False)
	vogal_viewed = models.BooleanField(default=False)
	forward_to_diresaun = models.BooleanField(default=False)
	diretor_viewed = models.BooleanField(default=False)
	# obs = models.TextField(null=True, blank=True)

	
	def __str__(self):
		return self.subject 

	class Meta:
		verbose_name_plural ="Documents Tama"

class Responde(models.Model):
	respond_number = models.CharField("Numeru Responde",max_length=20, unique=True, null=False)
	karta_tama = models.OneToOneField(Dokumentus, on_delete=models.CASCADE, null=True,related_name="karta_tama")
	hashed = models.CharField(max_length=32,null=True)
	date_respond = models.DateField(auto_now_add=False)
	file_respond = models.FileField(upload_to="responde/",max_length=200, null=True)
	deskrisaun = models.TextField(null=True, blank=True)
	forward_to_admin = models.BooleanField(default=False)
	admin_viewed = models.BooleanField(default=False)

# class Expedition(models.Model):
# 	karta_sai = models.ForeignKey(DokumentuSai, on_delete=models.CASCADE, null=True)
# 	data_haruka = models.DateField(auto_now_add=False)
	

class DokumentuSai(models.Model):
	klasifikasaun = (
		('Urgente', 'Urgente'),
		('Normal', 'Normal'),
		('Konfidensial', 'Konfidensial'),
		)
	status = (
					('Saved','Saved'),
					('Readed','Readed'),
					('Done','Done'),
					)
	doc_number = models.CharField("Numeru Dokumentu",max_length=20, unique=True, null=False)
	subject = models.CharField("Naran Dokumentu",max_length=100, null=False)
	date_created = models.DateTimeField(auto_now_add=True)
	destinu = models.CharField("Karta ba",max_length=225, null=True)
	orijen = models.ForeignKey(Diresaun, on_delete=models.CASCADE, null=True)
	folder_name = models.CharField(max_length=50, null=True)
	file_name = models.FileField(max_length=200, null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	klasifikasaun = models.CharField(max_length=32, null=True, choices=klasifikasaun)
	hashed = models.CharField(max_length=32,null=True)
	status = models.CharField(max_length=20, null=True, choices=status)
	diretor_viewed = models.BooleanField(default=False)
	forward_to_president = models.BooleanField(default=False)
	president_viewed = models.BooleanField(default=False)
	# aprova = models.BooleanField(default=False)
	forward_to_admin = models.BooleanField(default=False)
	admin_viewed = models.BooleanField(default=False)
	forward_to_vogal = models.BooleanField(default=False)
	vogal_viewed = models.BooleanField(default=False)
	# president_despacho_diresaun = models.CharField(null=True, max_length=200)
	# obs = models.TextField(null=True, blank=True)

	
	def __str__(self):
		return self.subject 

	class Meta:
		verbose_name_plural ="Documents Sai"

class DokumentuSaiInterna(models.Model):
	klasifikasaun = (
		('Urgente', 'Urgente'),
		('Normal', 'Normal'),
		('Konfidensial', 'Konfidensial'),
		)
	status = (
					('Saved','Saved'),
					('Readed','Readed'),
					('Done','Done'),
					)
	doc_number = models.CharField("Numeru Dokumentu",max_length=20, unique=True, null=False)
	subject = models.CharField("Naran Dokumentu",max_length=100, null=False)
	date_created = models.DateTimeField(auto_now_add=True)
	destinu = models.CharField("Karta ba",max_length=225, null=True)
	orijen = models.ForeignKey(Diresaun, on_delete=models.CASCADE, null=True)
	folder_name = models.CharField(max_length=50, null=True)
	file_name = models.FileField(max_length=200, null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	klasifikasaun = models.CharField(max_length=32, null=True, choices=klasifikasaun)
	hashed = models.CharField(max_length=32,null=True)
	status = models.CharField(max_length=20, null=True, choices=status)
	forward_to_president = models.BooleanField(default=False)
	president_viewed = models.BooleanField(default=False)
	deskrisaun = models.TextField(null=True, blank=True)
	admin_viewed = models.BooleanField(default=False)
	forward_to_vogal = models.BooleanField(default=False)
	vogal_viewed = models.BooleanField(default=False)
	forward_to_diresaun = models.BooleanField(default=False)
	diretor_viewed = models.BooleanField(default=False)
	president_informa = models.CharField(null=True, max_length=200,blank=True)
	president_informa_diresaun = models.ForeignKey(Diresaun,null=True,on_delete=models.CASCADE,related_name="informa_diresaun",blank=True)
	# president_informa_diresaun = models.CharField(null=True, max_length=200)
	# obs = models.TextField(null=True, blank=True)

	
	def __str__(self):
		return self.subject 

	class Meta:
		verbose_name_plural ="Documents Sai Interna"







