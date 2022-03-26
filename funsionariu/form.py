from django import forms
from .models import *

class DiresaunForm(forms.ModelForm):
	class Meta:
		model = Diresaun
		fields = ['codigu_diresaun','diresaun','vogal']

class KarguForm(forms.ModelForm):
	class Meta:
		model = Kargu
		fields = ['codigu_kargu','kargu','diresaun']

class FuncionarioForm(forms.ModelForm):
	class Meta:
		model = Funsionariu
		fields = ['naran_funsionariu','kargu','user','foto']
		


		