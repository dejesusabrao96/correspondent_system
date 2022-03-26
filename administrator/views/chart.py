import os
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.http import JsonResponse
from administrator.forms import KategoriaForm, DokumentuForm, DokumentuSaiForm, RepondForm
from custom.utils import *
from administrator.models import *

from datetime import date
from django.db.models import Count

from django.contrib.auth.decorators import login_required
from users.models import User

from django.core.files.base import ContentFile
# filter
from administrator.filters import DocsFilter, DocsSaiFilter

# pdf lib
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

# pagination
from django.core.paginator import Paginator
# csrf
from django.views.decorators.csrf import csrf_exempt
# resources
from custom.resources import DocRes
# flash messages
from django.contrib import messages
from users.decorators import *
from funsionariu.models import *
from funsionariu.models import Diresaun

@login_required
def charts(request):
	cat = Category.objects.all()
	queryset_category = Dokumentus.objects.values('category__cat_name').annotate(count=Count('category__cat_name'))

	
	notif_data = Dokumentus.objects.filter(status="Saved")
	notif_count = Dokumentus.objects.filter(status="Saved").count()
	
	context = {
		'title':"Charts Dadus",
		'categories':cat,
		'chart_active':"active",
		'queryset_category':queryset_category,
		'notif_data':notif_data,
		'notif_count':notif_count
	}
	return render(request, "charts.html",context)

@login_required
def chart_docsai(request):
	cat = Category.objects.all()
	queryset_category = DokumentuSai.objects.values('category__cat_name').annotate(count=Count('category__cat_name'))
	
	notif_data_sai = DokumentuSai.objects.filter(status="Saved")
	notif_count_sai = DokumentuSai.objects.filter(status="Saved").count()
	
	context = {
		'title':"Charts Dadus",
		'categories':cat,
		'chart_active':"active",
		'queryset_category':queryset_category,
		'notif_data_sai':notif_data_sai,
		'notif_count_sai':notif_count_sai
	}
	return render(request, "chart_docsai.html",context)

@login_required
def doc_charts(request):
	labels = []
	data = []
	if request.user.is_director:
		welcome = request.user
		person = Funsionariu.objects.get(user=welcome)
		diresaun_funsionariu = person.kargu.diresaun.id
		print(diresaun_funsionariu)
		title = "Varanda Diretor"
		queryset = Dokumentus.objects.filter(destinu=diresaun_funsionariu).values('category__cat_name').annotate(count=Count('category__cat_name'))
		for entry in queryset:
			labels.append(entry['category__cat_name'])
			data.append(entry['count'])
		return JsonResponse(data={
			'labels':labels,
			'data':data,
			})

	if request.user.is_secretary:
		queryset = Dokumentus.objects.values('category__cat_name').annotate(count=Count('category__cat_name'))
		for entry in queryset:
			labels.append(entry['category__cat_name'])
			data.append(entry['count'])
		return JsonResponse(data={
			'labels':labels,
			'data':data,
			})

	if request.user.is_prezidente:
		queryset = Dokumentus.objects.values('category__cat_name').annotate(count=Count('category__cat_name'))
		for entry in queryset:
			labels.append(entry['category__cat_name'])
			data.append(entry['count'])
		return JsonResponse(data={
			'labels':labels,
			'data':data,
			})

@login_required
def doc_sai_charts(request):
	labels = []
	data = []
	if request.user.is_director:
		welcome = request.user
		person = Funsionariu.objects.get(user=welcome)
		diresaun_funsionariu = person.kargu.diresaun.id
		print(diresaun_funsionariu)
		title = "Varanda Diretor"
		queryset = DokumentuSai.objects.filter(orijen=diresaun_funsionariu).values('category__cat_name').annotate(count=Count('category__cat_name'))
		for entry in queryset:
			labels.append(entry['category__cat_name'])
			data.append(entry['count'])
		return JsonResponse(data={
			'labels':labels,
			'data':data,
			})

	if request.user.is_secretary:
		queryset = DokumentuSai.objects.values('category__cat_name').annotate(count=Count('category__cat_name'))
		for entry in queryset:
			labels.append(entry['category__cat_name'])
			data.append(entry['count'])

		return JsonResponse(data={
			'labels':labels,
			'data':data,
			})

	if request.user.is_prezidente:
		queryset = DokumentuSai.objects.values('category__cat_name').annotate(count=Count('category__cat_name'))
		for entry in queryset:
			labels.append(entry['category__cat_name'])
			data.append(entry['count'])

		return JsonResponse(data={
			'labels':labels,
			'data':data,
			})

@login_required
def charts_tipu_karta(request):
	labels = ['Karta Tama','Karta Sai']

	if request.user.is_director:
		welcome = request.user
		person = Funsionariu.objects.get(user=welcome)
		diresaun_funsionariu = person.kargu.diresaun.id
		# print(diresaun_funsionariu)
		title = "Varanda Diretor"
		kt = Dokumentus.objects.filter(destinu=diresaun_funsionariu).count()
		ks = DokumentuSai.objects.filter(orijen=diresaun_funsionariu).count()
		data = [kt,ks]
	if request.user.is_secretary:
		kt = Dokumentus.objects.all().count()
		ks = DokumentuSai.objects.all().count()
		data = [kt,ks]
	if request.user.is_prezidente:
		kt = Dokumentus.objects.all().count()
		ks = DokumentuSai.objects.all().count()
		data = [kt,ks]

	
	return JsonResponse(data={
		'labels':labels,
		'data':data,
		})