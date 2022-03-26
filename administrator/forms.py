from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.forms.widgets import FileInput
from .models import *



class DokumentuForm(forms.ModelForm):
	class Meta:
		model = Dokumentus
		fields = ['doc_number','subject','given_by','orijen','destinu','recieve_by','file_name','category','klasifikasaun']
		#fields = ['doc_number','subject','date_created','given_by','orijen','destinu','recieve_by','category','sub_category','klasifikasaun']
		exclude = ['date_created','folder_name','hashed','status','forward_to_president','president_viewed','forward_to_admin','admin_viewed','president_despacho','president_despacho_diresaun','forward_to_vogal','vogal_viewed','forward_to_diresaun','diretor_viewed','obs']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('doc_number', css_class='form-group col-md-6 mb-0'),
				Column('subject', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('given_by', css_class='form-group col-md-6 mb-0'),
				Column('orijen', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('destinu', css_class='form-group col-md-6 mb-0'),
				Column('recieve_by', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('file_name', css_class='form-group col-md-4 mb-0'),
				Column('category', css_class='form-group col-md-4 mb-0'),
				Column('klasifikasaun', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			HTML(""" <div class="text-right mt-4"> <button class="btn btn-sm btn-labeled btn-info" type="submit" title="Update"><span class="btn-label"><i class='fa fa-save'></i></span>Save</button>"""),
			HTML("""  <button class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Cancel</button></div>""")
		)

class DokumentuSaiForm(forms.ModelForm):
	class Meta:
		model = DokumentuSai
		fields = ['doc_number','subject','orijen','destinu','file_name','category','klasifikasaun']
		exclude = ['date_created','folder_name','hashed','status','forward_to_president','president_viewed','forward_to_admin','admin_viewed','forward_to_vogal','vogal_viewed','president_despacho_diresaun','obs']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('doc_number', css_class='form-group col-md-6 mb-0'),
				Column('subject', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('orijen', css_class='form-group col-md-6 mb-0'),
				Column('destinu', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('file_name', css_class='form-group col-md-4 mb-0'),
				Column('category', css_class='form-group col-md-4 mb-0'),
				Column('klasifikasaun', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			HTML(""" <div class="text-right mt-4"> <button class="btn btn-sm btn-labeled btn-info" type="submit" title="Update"><span class="btn-label"><i class='fa fa-save'></i></span>Save</button>"""),
			HTML("""  <button class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Cancel</button></div>""")
		)

class DokumentuSaiInternaForm(forms.ModelForm):
	class Meta:
		model = DokumentuSaiInterna
		fields = ['doc_number','subject','orijen','destinu','file_name','category','klasifikasaun']
		# exclude = ['date_created','folder_name','hashed','status','forward_to_president','president_viewed','forward_to_admin','admin_viewed','president_despacho','president_despacho_diresaun','forward_to_vogal','vogal_viewed','forward_to_diresaun','diretor_viewed','obs']
		exclude = ['date_created','folder_name','hashed','status','forward_to_president','president_viewed','forward_to_admin','admin_viewed','forward_to_vogal','vogal_viewed','president_despacho_diresaun','obs']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('doc_number', css_class='form-group col-md-6 mb-0'),
				Column('subject', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('orijen', css_class='form-group col-md-6 mb-0'),
				Column('destinu', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('file_name', css_class='form-group col-md-4 mb-0'),
				Column('category', css_class='form-group col-md-4 mb-0'),
				Column('klasifikasaun', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			HTML(""" <div class="text-right mt-4"> <button class="btn btn-sm btn-labeled btn-info" type="submit" title="Update"><span class="btn-label"><i class='fa fa-save'></i></span>Save</button>"""),
			HTML("""  <button class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Cancel</button></div>""")
		)


class KategoriaForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['cat_code','cat_name']

class DateInput(forms.DateInput):
	input_type = 'date'

class RepondForm(forms.ModelForm):
	date_respond = forms.DateField(label="Data Responde",widget=DateInput())
	deskrisaun = forms.CharField(label='Deskrisaun',widget=forms.Textarea(attrs={'rows':2}))
	class Meta:
		model = Responde
		fields = ['respond_number','date_respond','file_respond','deskrisaun']
		exclude = ['karta_tama','hashed','forward_to_admin']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('respond_number', css_class='form-group col-md-6 mb-0'),
				Column('date_respond', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('file_respond', css_class='form-group col-md-6 mb-0'),
				Column('deskrisaun', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			HTML(""" <div class="text-right mt-4"> <button class="btn btn-sm btn-labeled btn-info" type="submit" title="Update"><span class="btn-label"><i class='fa fa-save'></i></span>Save</button>"""),
			HTML("""  <button class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Cancel</button></div>""")
		)



# class KategoriaSaiForm(forms.ModelForm):
# 	class Meta:
# 		model = CategoryDocSai
# 		fields = ['cat_code','cat_name']

