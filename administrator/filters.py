import django_filters
from django_filters import CharFilter

from .models import *

class DocsFilter(django_filters.FilterSet):
	subject = CharFilter(field_name='subject', lookup_expr='icontains')
	class Meta:
		model = Dokumentus
		fields = '__all__'
		exclude = ['given_by','recieve_by','folder_name','hashed','date_created','date_despacho','file_name']

class DocsSaiFilter(django_filters.FilterSet):
	subject = CharFilter(field_name='subject', lookup_expr='icontains')
	class Meta:
		model = DokumentuSai
		fields = '__all__'
		exclude = ['folder_name','hashed','date_created','file_name']

class DocsSaiInteranFilter(django_filters.FilterSet):
	subject = CharFilter(field_name='subject', lookup_expr='icontains')
	class Meta:
		model = DokumentuSaiInterna
		fields = '__all__'
		exclude = ['folder_name','hashed','date_created','file_name']