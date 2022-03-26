import os
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.http import JsonResponse
# from ..forms import KategoriaForm, DokumentuForm, DokumentuSaiForm, RepondForm
from administrator.forms import KategoriaForm, DokumentuForm, DokumentuSaiForm, RepondForm, DokumentuSaiInternaForm
from custom.utils import *
from administrator.models import *

from datetime import date
from django.db.models import Count

from django.contrib.auth.decorators import login_required
from users.models import User

from django.core.files.base import ContentFile
# filter
from administrator.filters import DocsFilter, DocsSaiFilter, DocsSaiInteranFilter

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

# Create your views here.
@login_required
def home(request):
	today = date.today()
	cat = Category.objects.all()
	# total_docs query
	if request.user.is_secretary:
		today_docs = Dokumentus.objects.filter(date_created__year=today.year,date_created__month=today.month,date_created__day=today.day).count()
		today_doc_sai = DokumentuSai.objects.filter(date_created__year=today.year,date_created__month=today.month,date_created__day=today.day).count()
		tot_docs = Dokumentus.objects.all().count()
		tot_doc_sai = DokumentuSai.objects.all().count()
		this_month_docs = Dokumentus.objects.filter(date_created__year=today.year,date_created__month=today.month).count()
		this_month_doc_sai = DokumentuSai.objects.filter(date_created__year=today.year,date_created__month=today.month).count()
		this_year_docs = Dokumentus.objects.filter(date_created__year=today.year).count()
		this_year_doc_sai = DokumentuSai.objects.filter(date_created__year=today.year).count()
		queryset_categorytama = Dokumentus.objects.values('category__cat_name','category__hashed').annotate(count=Count('category__cat_name'))
		queryset_categorysai = DokumentuSai.objects.values('category__cat_name','category__hashed').annotate(count=Count('category__cat_name'))
		welcome = request.user
		person = Funsionariu.objects.get(user=welcome)
		title = "Varanda Secretaria"
		notif_data = None
		notif_count = 0

		notif_data_sai = DokumentuSai.objects.filter(status="Saved",forward_to_admin=True,admin_viewed=True,forward_to_president=True, president_viewed=True)
		notif_count_sai = DokumentuSai.objects.filter(status="Saved",forward_to_admin=True,admin_viewed=True,forward_to_president=True, president_viewed=True).count()

	if request.user.is_director:
		welcome = request.user
		person = Funsionariu.objects.get(user=welcome)
		diresaun_funsionariu = person.kargu.diresaun.id
		print(diresaun_funsionariu)
		title = "Varanda Diretor"
		today_docs = Dokumentus.objects.filter(destinu=diresaun_funsionariu,date_created__year=today.year,date_created__month=today.month,date_created__day=today.day).count()
		today_doc_sai = DokumentuSai.objects.filter(orijen=diresaun_funsionariu,date_created__year=today.year,date_created__month=today.month,date_created__day=today.day).count()
		tot_docs = Dokumentus.objects.filter(destinu=diresaun_funsionariu).count()
		# tot_docs = Dokumentus.objects.filter(destinu=diresaun_funsionariu).count()
		tot_doc_sai = DokumentuSai.objects.filter(orijen=diresaun_funsionariu).count()
		this_month_docs = Dokumentus.objects.filter(destinu=diresaun_funsionariu,date_created__year=today.year,date_created__month=today.month).count()
		this_month_doc_sai = DokumentuSai.objects.filter(orijen=diresaun_funsionariu,date_created__year=today.year,date_created__month=today.month).count()
		this_year_docs = Dokumentus.objects.filter(destinu=diresaun_funsionariu,date_created__year=today.year).count()
		this_year_doc_sai = DokumentuSai.objects.filter(orijen=diresaun_funsionariu,date_created__year=today.year).count()
		queryset_categorytama = Dokumentus.objects.filter(destinu=diresaun_funsionariu).values('category__cat_name','category__hashed').annotate(count=Count('category__cat_name'))
		queryset_categorysai = DokumentuSai.objects.filter(orijen=diresaun_funsionariu).values('category__cat_name','category__hashed').annotate(count=Count('category__cat_name'))
		
		notif_data = Dokumentus.objects.filter(status="Saved",forward_to_president=True,president_viewed=True,president_despacho__isnull=False,president_despacho_diresaun=diresaun_funsionariu,vogal_viewed=True,forward_to_diresaun=True,diretor_viewed=False)
		notif_count = Dokumentus.objects.filter(status="Saved",forward_to_president=True,president_viewed=True,president_despacho__isnull=False,president_despacho_diresaun=diresaun_funsionariu,vogal_viewed=True,forward_to_diresaun=True,diretor_viewed=False).count()

		notif_data_sai = None
		notif_count_sai = 0
 

	if request.user.is_staff:
		today_docs = Dokumentus.objects.filter(date_created__year=today.year,date_created__month=today.month,date_created__day=today.day).count()
		today_doc_sai = DokumentuSai.objects.filter(date_created__year=today.year,date_created__month=today.month,date_created__day=today.day).count()
		tot_docs = Dokumentus.objects.all().count()
		tot_doc_sai = DokumentuSai.objects.all().count()
		this_month_docs = Dokumentus.objects.filter(date_created__year=today.year,date_created__month=today.month).count()
		this_month_doc_sai = DokumentuSai.objects.filter(date_created__year=today.year,date_created__month=today.month).count()
		this_year_docs = Dokumentus.objects.filter(date_created__year=today.year).count()
		this_year_doc_sai = DokumentuSai.objects.filter(date_created__year=today.year).count()
		queryset_categorytama = Dokumentus.objects.values('category__cat_name','category__hashed').annotate(count=Count('category__cat_name'))
		queryset_categorysai = DokumentuSai.objects.values('category__cat_name','category__hashed').annotate(count=Count('category__cat_name'))
		person = None
		title = "Varanda Admin"
		notif_data = Dokumentus.objects.filter(status="Saved",forward_to_president=True)
		notif_count = Dokumentus.objects.filter(status="Saved",forward_to_president=True).count()
		
		notif_data_sai = DokumentuSai.objects.filter(status="Saved",forward_to_president=True)
		notif_count_sai = DokumentuSai.objects.filter(status="Saved",forward_to_president=True).count()

	if request.user.is_prezidente:
		today_docs = Dokumentus.objects.filter(date_created__year=today.year,date_created__month=today.month,date_created__day=today.day).count()
		today_doc_sai = DokumentuSai.objects.filter(date_created__year=today.year,date_created__month=today.month,date_created__day=today.day).count()
		tot_docs = Dokumentus.objects.all().count()
		tot_doc_sai = DokumentuSai.objects.all().count()
		this_month_docs = Dokumentus.objects.filter(date_created__year=today.year,date_created__month=today.month).count()
		this_month_doc_sai = DokumentuSai.objects.filter(date_created__year=today.year,date_created__month=today.month).count()
		this_year_docs = Dokumentus.objects.filter(date_created__year=today.year).count()
		this_year_doc_sai = DokumentuSai.objects.filter(date_created__year=today.year).count()
		queryset_categorytama = Dokumentus.objects.values('category__cat_name','category__hashed').annotate(count=Count('category__cat_name'))
		queryset_categorysai = DokumentuSai.objects.values('category__cat_name','category__hashed').annotate(count=Count('category__cat_name'))
		person = None
		title = "Varanda Prezidente"
		notif_data = Dokumentus.objects.filter(status="Saved",forward_to_president=True,president_viewed=False)
		notif_count = Dokumentus.objects.filter(status="Saved",forward_to_president=True,president_viewed=False).count()
	
		notif_data_sai = DokumentuSai.objects.filter(status="Saved",forward_to_admin=True,admin_viewed=True,forward_to_president=True,president_viewed=True)
		notif_count_sai = DokumentuSai.objects.filter(status="Saved",forward_to_admin=True,admin_viewed=True,forward_to_president=True,president_viewed=True).count()


	if request.user.is_vogal:
		user = request.user.id
		title = "Varanda Vogal"
		vogal = Vogal.objects.get(user__id=user)
		diresaun_vogal = Diresaun.objects.filter(vogal=vogal)
		doc = []
		for i in diresaun_vogal:
			person = None
			today_docs = Dokumentus.objects.filter(destinu=i.id,date_created__year=today.year,date_created__month=today.month,date_created__day=today.day).count()
			today_doc_sai = DokumentuSai.objects.filter(orijen=i.id,date_created__year=today.year,date_created__month=today.month,date_created__day=today.day).count()
			tot_docs = Dokumentus.objects.filter(destinu=i.id,).count()
			# tot_docs = Dokumentus.objects.filter(destinu=diresaun_funsionariu).count()
			tot_doc_sai = DokumentuSai.objects.filter(orijen=i.id).count()
			this_month_docs = Dokumentus.objects.filter(destinu=i.id,date_created__year=today.year,date_created__month=today.month).count()
			this_month_doc_sai = DokumentuSai.objects.filter(orijen=i.id,date_created__year=today.year,date_created__month=today.month).count()
			this_year_docs = Dokumentus.objects.filter(destinu=i.id,date_created__year=today.year).count()
			this_year_doc_sai = DokumentuSai.objects.filter(orijen=i.id,date_created__year=today.year).count()
			queryset_categorytama = Dokumentus.objects.filter(destinu=i.id).values('category__cat_name','category__hashed').annotate(count=Count('category__cat_name'))
			queryset_categorysai = DokumentuSai.objects.filter(orijen=i.id).values('category__cat_name','category__hashed').annotate(count=Count('category__cat_name'))
			notif_data = Dokumentus.objects.filter(status="Saved",forward_to_president=True,president_viewed=True,president_despacho__isnull=False,president_despacho_diresaun=i.id,vogal_viewed=False)
			notif_count = Dokumentus.objects.filter(status="Saved",forward_to_president=True,president_viewed=True,president_despacho__isnull=False,president_despacho_diresaun=i.id,vogal_viewed=False).count()

			# notif_data_sai = DokumentuSai.objects.filter(status="Saved",forward_to_president=True,president_viewed=True,president_despacho__isnull=False,president_despacho_diresaun=i.id,vogal_viewed=False)
			# notif_count_sai = DokumentuSai.objects.filter(status="Saved",forward_to_president=True,president_viewed=True,president_despacho__isnull=False,president_despacho_diresaun=i.id,vogal_viewed=False).count()

	# print("queryset_categorytama:",queryset_categorytama)
	data = {
		'title':title,
		'home_active':"active",
		'categories':cat,
		'today_docs':today_docs,
		'today_doc_sai':today_doc_sai,
		'this_month_docs':this_month_docs,
		'this_month_doc_sai':this_month_doc_sai,
		'this_year_docs':this_year_docs,
		'this_year_doc_sai':this_year_doc_sai,
		'tot_docs':tot_docs,
		'tot_doc_sai':tot_doc_sai,
		'queryset_categorytama':queryset_categorytama,
		'queryset_categorysai':queryset_categorysai,
		'login_person':person,
		'notif_data':notif_data,
		'notif_count':notif_count,
		'notif_data':notif_data,

		# 'notif_data_sai':notif_data_sai,
		# 'notif_count_sai':notif_count_sai
	}
	return render(request, 'index.html',data)

@login_required
def documents(request):
	cat = Category.objects.all()
	if request.user.is_secretary:
		# Query ne'e fo sai katak secretaria haree detail tiha notifikasaun karta tama hafoin karta tama mosu iha lista karta tama nian. 
		doc = Dokumentus.objects.filter(status="Saved",admin_viewed=True).all()

	if request.user.is_prezidente:
		# Query ne'e fo sai katak karta tama secretaria rai no input ona no forward ba prezidente los ona, prezidente mos haree detail ona iha notifikasaun.
		# hafoin karta tama mosu iha lista karta tama.
		doc = Dokumentus.objects.filter(status="Saved",forward_to_president=True,president_viewed=True)

	if request.user.is_staff:
		doc = Dokumentus.objects.all()
		
	if request.user.is_vogal:
		user = request.user.id
		# title = "Varanda Vogal"
		vogal = Vogal.objects.get(user__id=user)
		diresaun_vogal = Diresaun.objects.filter(vogal=vogal)
		doc = []
		for i in diresaun_vogal:
			person = None
			doc1 = Dokumentus.objects.filter(destinu=i.id,status="Saved",forward_to_president=True,president_viewed=True,vogal_viewed=True)
			for x in doc1.iterator():
				doc.append({
					"id":x.id,
					"hashed":x.hashed,
					"doc_number":x.doc_number,
					"subject":x.subject,
					"date_created":x.date_created,
					"klasifikasaun":x.klasifikasaun,
					"category":x.category,
					"file_name":x.file_name,
					"given_by":x.given_by,
					"orijen":x.orijen,
					"recieve_by":x.recieve_by,
					"destinu":x.destinu,
					"status":x.status,
					"forward_to_president":x.forward_to_president,
					"president_viewed":x.president_viewed,
					"admin_viewed":x.admin_viewed,
					"vogal_viewed":x.vogal_viewed,
					"diretor_viewed":x.diretor_viewed,

				})

	if request.user.is_director:
		person = Funsionariu.objects.get(user=request.user)
		diresaun_funsionariu = person.kargu.diresaun.id
		# Query 
		doc = Dokumentus.objects.filter(destinu=diresaun_funsionariu,status="Saved",forward_to_president=True,president_viewed=True,vogal_viewed=True,forward_to_diresaun=True,diretor_viewed=True).all()
		# doc = Dokumentus.objects.filter(destinu=diresaun_funsionariu)

	notif_data = Dokumentus.objects.filter(status="Saved")
	notif_count = Dokumentus.objects.filter(status="Saved").count()

	data = {
		'title':"Documents",
		'doc_active':"active",
		'categories':cat,
		'documents':doc,
		# 'tamas':tama,
		'notif_data':notif_data,
		'notif_count':notif_count
	}
	return render(request, 'doc_list.html',data)

@login_required
def documentSai(request):
	cat = Category.objects.all()
	# diresaun = Diresaun.objects.all()
	# doc_sai = DokumentuSai.objects.all()
	if request.user.is_director:
		person = Funsionariu.objects.get(user=request.user)
		diresaun_funsionariu = person.kargu.diresaun.id
		# Query ne'e atu fo sai katak director haree detail tiha notifikasaun karta sai hafoin dadus mosu iha lista karta sai nian.
		doc_sai = DokumentuSai.objects.filter(orijen=diresaun_funsionariu,status="Saved",diretor_viewed=True).all()
	
	if request.user.is_vogal:
		user = request.user.id
		# title = "Varanda Vogal"
		vogal = Vogal.objects.get(user__id=user)
		diresaun_vogal = Diresaun.objects.filter(vogal=vogal)
		doc_sai = []
		for i in diresaun_vogal:
			person = None
			doc_sai1 = DokumentuSai.objects.filter(orijen=i.id,status="Saved",forward_to_vogal=True,vogal_viewed=True,forward_to_president=True,president_viewed=True, forward_to_admin=True, admin_viewed=True).all()
			for x in doc_sai1.iterator():
				doc_sai.append({
					"id":x.id,
					"hashed":x.hashed,
					"doc_number":x.doc_number,
					"subject":x.subject,
					"date_created":x.date_created,
					"klasifikasaun":x.klasifikasaun,
					"category":x.category,
					"file_name":x.file_name,
					# "given_by":x.given_by,
					"orijen":x.orijen,
					# "recieve_by":x.recieve_by,
					"destinu":x.destinu,
					"status":x.status,
					"forward_to_vogal":x.forward_to_vogal,
					"vogal_viewed":x.vogal_viewed,
					"forward_to_president":x.forward_to_president,
					"president_viewed":x.president_viewed,
					"diretor_viewed":x.diretor_viewed,
					"forward_to_admin":x.forward_to_admin,
					"admin_viewed":x.admin_viewed,

				})
		# Query ne'e fo sai katak karta sai ne'e diretor forward ba vogal los ona, vogal haree detail ona karta sai husi notifikasaun
		# hafoin karta sai mosu iha lista karta sai nian iha plataforma vogal nian.
		# doc_sai = DokumentuSai.objects.filter(status="Saved",forward_to_vogal=True,vogal_viewed=True).all()
		
	if request.user.is_prezidente:
		# person = Funsionariu.objects.get(user=request.user)
		# Query ne'e atu fo sai katak karta sai forward ona ba vogal, vogal mos haree ona no prezidente haree detail ona karta sai husi notifikasaun karta sai
		# hafoin dadus karta sai mosu iha lista karta sai nian.
		doc_sai = DokumentuSai.objects.filter(status="Saved",forward_to_vogal=True,vogal_viewed=True,president_viewed=True).all()
		# doc_sai = DokumentuSai.objects.all()
		# diresaun_funsionariu = person.kargu.diresaun.id
		# doc_sai = DokumentuSai.objects.filter(orijen=diresaun_funsionariu)

	if request.user.is_secretary:
		# Query ne'e atu fo sai katak secretaria haree detail tiha notifikasaun karta sai hafoin dadus mosu iha lista karta sai nian.
		doc_sai = DokumentuSai.objects.filter(status="Saved",forward_to_vogal=True,vogal_viewed=True,forward_to_president=True,president_viewed=True,admin_viewed=True).all()
		# doc_sai = DokumentuSai.objects.all()
	
	if request.user.is_staff:
		doc_sai = DokumentuSai.objects.all()
		# notif_data_sai = DokumentuSai.objects.filter(status="Saved")
		# notif_count_sai = DokumentuSai.objects.filter(status="Saved").count()
	

	data = {
		# 'diresaun':diresaun,
		'documentSai':doc_sai,
		'categories':cat,
		# 'notif_data_sai':notif_data_sai,
		# 'notif_count_sai':notif_count_sai

	}
	return render(request, 'doc_sai_list.html', data)


@login_required
def grid_documents(request):
	cat = Category.objects.all()
	doc = Dokumentus.objects.all().order_by('-id')
	
	doc_filter = DocsFilter(request.GET, queryset=doc)
	doc = doc_filter.qs

	paginator = Paginator(doc, 6)
	page = request.GET.get('page')
	doc = paginator.get_page(page)
	
	doc = Dokumentus.objects.all()
	notif_data = Dokumentus.objects.filter(status="Saved")
	notif_count = Dokumentus.objects.filter(status="Saved").count()

	data = {
		# 'title':"Documents",
		# 'doc_active':"active",
		'doc_filter':doc_filter,
		'categories':cat,
		'notif_data':notif_data,
		'notif_count':notif_count,
		'documents':doc
	}
	return render(request, 'grid_doc.html',data)

@login_required
def grid_document_sai(request):
	doc_sai = DokumentuSai.objects.all().order_by('-id')
	doc_sai_filter = DocsSaiFilter(request.GET, queryset=doc_sai)
	doc_sai = doc_sai_filter.qs

	paginator = Paginator(doc_sai,6)
	page = request.GET.get('page')
	doc_sai = paginator.get_page(page)

	doc_sai = DokumentuSai.objects.all()

	notif_data_sai = DokumentuSai.objects.filter(status="Saved")
	notif_count_sai = DokumentuSai.objects.filter(status="Saved").count()

	context = {
		# 'title':Document Sai,
		# 'doc_sai_active':active,
		'documentsai':doc_sai,
		'doc_sai_filter':doc_sai_filter,
		'doc_sai':doc_sai,
		'notif_data_sai':notif_data_sai,
		'notif_count_sai':notif_count_sai
	}
	return render(request, 'grid_doc_sai.html', context)

@login_required
def grid_karta_sai_interna(request):
	doc_sai_interna = DokumentuSaiInterna.objects.all().order_by('-id')
	doc_sai_interna_filter = DocsSaiInteranFilter(request.GET, queryset=doc_sai_interna)
	doc_sai_interna = doc_sai_interna_filter.qs

	paginator = Paginator(doc_sai_interna,6)
	page = request.GET.get('page')
	doc_sai_interna = paginator.get_page(page)

	doc_sai_interna = DokumentuSaiInterna.objects.all()

	notif_data_sai_interna = DokumentuSaiInterna.objects.filter(status="Saved")
	notif_count_sai_interna = DokumentuSaiInterna.objects.filter(status="Saved").count()

	context = {
		# 'title':Karta Sai Interna,
		# 'doc_interna_active':active,
		'documentinterna':doc_sai_interna,
		'doc_sai_interna_filter':doc_sai_interna_filter,
		'doc_sai_interna':doc_sai_interna,
		'notif_data_sai_interna':notif_data_sai_interna,
		'notif_count_sai_interna':notif_count_sai_interna
	}
	return render(request, 'grid_doc_sai_interna.html', context)

@login_required
def category_list(request):
	cat = Category.objects.all()
	
	notif_data = Dokumentus.objects.filter(status="Saved")
	notif_count = Dokumentus.objects.filter(status="Saved").count()

	data = {
		'title':"Category",
		'categories':cat,
		'notif_data':notif_data,
		'notif_count':notif_count
	}
	return render(request, 'cat_list.html',data)

@login_required
def category_doc_sai_list(request):
	cat = Category.objects.all()
	
	notif_data_sai = DokumentuSai.objects.filter(status="Saved")
	notif_count = DokumentuSai.objects.filter(status="Saved").count()

	data = {
		'title':"Category",
		'categories':cat,
		'notif_data_sai':notif_data_sai,
		'notif_count_sai':notif_count_sai
	}
	return render(request, 'cat_sai_list.html',data)


@login_required
def add_category(request):
	cat = Category.objects.all()

	if request.method == 'POST':
		_, newid = getlastid(Category)
		hashid = hash_md5(str(newid))

		form = KategoriaForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.hashed = hashid
			instance.save()
			if 'save' in request.POST:
				messages.success(request, f'Category is Added Successfully.')
				return redirect('category-list')
			elif 'save_and_add_another' in request.POST:
				messages.success(request, f'Category is Added Successfully.')
				return redirect('category-list')

	else:
		form = KategoriaForm()
	
	notif_data = Dokumentus.objects.filter(status="Saved")
	notif_count = Dokumentus.objects.filter(status="Saved").count()
	context = {
		'title':"Form Category",
		'form': form, 
		'notif_data':notif_data,
		'notif_count':notif_count,
		'categories':cat
	}
	return render(request, 'form_category.html', context)

@login_required
def add_category_docsai(request):
	cat = Category.objects.all()

	if request.method == 'POST':
		_, newid = getlastid(Category)
		hashid = hash_md5(str(newid))

		form = KategoriaSaiForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.hashed = hashid
			instance.save()
			if 'save' in request.POST:
				messages.success(request, f'Category is Added Successfully.')
				return redirect('category-doc-sai-list')
			elif 'save_and_add_another' in request.POST:
				messages.success(request, f'Category is Added Successfully.')
				return redirect('category-doc-sai-list')

	else:
		form = KategoriaForm()
	
	notif_data_sai = DokumentuSai.objects.filter(status="Saved")
	notif_count_sai = DokumentuSai.objects.filter(status="Saved").count()
	context = {
		'title':"Form Category Outgoing Letter",
		'form': form, 
		'notif_data_sai':notif_data_sai,
		'notif_count_sai':notif_count_sai,
		'categories':cat
	}
	return render(request, 'form_category_docsai.html', context)


@login_required		 
def load_notif_data(request):
	notif_data = None
	notif_count = None
	if not request.user.is_staff :
		funsionariu = Funsionariu.objects.get(user=request.user.id)
		diresaun_user = funsionariu.kargu.diresaun.id
		notif_data = Dokumentus.objects.filter(destinu=diresaun_user,status="Saved")
		notif_count = Dokumentus.objects.filter(destinu=diresaun_user,status="Saved").count()
	else :
		notif_data = Dokumentus.objects.all()
		notif_count = Dokumentus.objects.all().count()
	context = {
		'notif_data':notif_data,
		'notif_count':notif_count
	}
	return render(request, 'ajax_notif.html',context)

@login_required
def load_notif_data_sai(request):
	notif_data_sai = None
	notif_count_sai = None
	if not request.user.is_staff :
		funsionariu = Funsionariu.objects.get(user=request.user.id)
		diresaun_user = funsionariu.kargu.diresaun_id
		notif_data_sai = DokumentuSai.objects.filter(destinu=diresaun_user,status="Saved")
		notif_count_sai = DokumentuSai.objects.filter(destinu=diresaun_user,status="Saved").count()
	else:
		notif_data_sai = DokumentuSai.objects.all()
		notif_count_sai = DokumentuSai.objects.all().count()
	context = {
		'notif_data_sai':notif_data_sai,
		'notif_count_sai':notif_count_sai
}
	return render(request, 'ajax_notif_sai.html', context)

@login_required
def addDocSai(request):
	category = Category.objects.all()

	# select diresaun bazeia ba diresaun ne'ebe mak nia servisu ba 
	welcome = request.user
	person = Funsionariu.objects.get(user=welcome)
	diresaun_funsionariu = person.kargu.diresaun.id
	diresaun = Diresaun.objects.filter(id=diresaun_funsionariu)
	# print("Latama")
	if request.method == "POST" and 'upload_file' in request.FILES:
		# print("Tama")
		_, newid = getlastid(DokumentuSai)
		hashid = hash_md5(str(newid))
		doc_id = newid
		doc_hashed = hashid
		doc_number = request.POST.get('doc_number')
		subject = request.POST.get('subject')
		destinu = request.POST.get('destinu')
		orijen = request.POST.get('diresaun')

		print("diresaun_id:",diresaun)
		klasifikasaun = request.POST.get('klasifikasaun')
		diresaun_id = get_object_or_404(Diresaun,id=orijen)
		cat_id = request.POST.get('kat')
		cat = Category.objects.get(id=cat_id)
		cat_code = cat.cat_code

		file_name = request.FILES.get('upload_file')
		file_format = request.FILES['upload_file']
		folder_name = cat_code
		if not file_format.name.endswith('.pdf'):
			messages.warning(request, f'The uploaded file should in PDF format.')
		else :
			# kria folder bazeia ba codigo categoria.
			cat_path = 'doc_files/'+folder_name+'/'
			uploaded_filename = request.FILES['upload_file'].name
			if not os.path.exists(cat_path):
				os.makedirs(cat_path)
				file_name = folder_name+'/'+str(file_name)
				full_filename = os.path.join(cat_path, uploaded_filename)
			else:
				file_name = folder_name+'/'+str(file_name)
				full_filename = os.path.join(cat_path, uploaded_filename)

			# save the uploaded file inside that folder.
			fout = open(full_filename, 'wb+')
			uploaded_filename = ContentFile(request.FILES['upload_file'].read())
			try:
				# Iterate through the chunks.
				for chunk in uploaded_filename.chunks():
					fout.write(chunk)
				fout.close()
			except:
				html = "<html><body>NOT SAVED</body></html>"
				return HttpResponse(html)

			doc = DokumentuSai.objects.create(id=doc_id,doc_number=doc_number,category=cat,klasifikasaun=klasifikasaun,subject=subject,destinu=destinu,orijen=diresaun_id,folder_name=folder_name,file_name=file_name,hashed=doc_hashed,status="Saved")
			doc.save()
			if 'save' in request.POST:
				messages.success(request, f'Document {doc_number} is Added Successfully.')
				return redirect('documents-sai-list')
			elif 'save_and_add_another' in request.POST:
				messages.success(request, f'Document {doc_number} is Added Successfully.')
				return redirect('add-doc-sai')
	
	notif_data_sai = Dokumentus.objects.filter(status="Saved")
	notif_count_sai = Dokumentus.objects.filter(status="Saved").count()
	context = {
		'title':"Form Documents",
		'doc_active':"active",
		'page':"add",
		'diresaun':diresaun,
		'notif_data_sai':notif_data_sai,
		'notif_count_sai':notif_count_sai,
		'categories':category
	}
	return render(request, 'form_doc_sai.html', context)

@login_required
@allowed_users(allowed_roles=['Prezidente','is_staff'])
def add_document(request):
	category = Category.objects.all()
	diresaun = Diresaun.objects.all()

	if request.method == "POST" and 'upload_file' in request.FILES:
		_, newid = getlastid(Dokumentus)
		hashid = hash_md5(str(newid))
		
		doc_id = newid
		doc_hashed = hashid

		doc_number = request.POST.get('doc_number')
		subject = request.POST.get('subject')
		orijen = request.POST.get('orijen')

		
		destinu = request.POST.get('diresaun')
		klasifikasaun = request.POST.get('Klasifikasaun')
		diresaun_id = Diresaun.objects.get(id=destinu)
		given_by = request.POST.get('given_by')
		recieve_by = request.POST.get('recieve_by')

		cat_id = request.POST.get('kat')
		cat = Category.objects.get(id=cat_id)
		cat_code = cat.cat_code

		file_name = request.FILES.get('upload_file')
		file_format = request.FILES['upload_file']
		folder_name = cat_code

		if not file_format.name.endswith('.pdf'):
			messages.warning(request, f'The uploaded file should in PDF format.')
		else :
			# kria folder bazeia ba codigo categoria
			cat_path = 'doc_files/'+folder_name+'/'
			uploaded_filename = request.FILES['upload_file'].name
			if not os.path.exists(cat_path):
				os.makedirs(cat_path)
				file_name = folder_name+'/'+str(file_name)
				full_filename = os.path.join(cat_path, uploaded_filename)
			else:
				file_name = folder_name+'/'+str(file_name)
				full_filename = os.path.join(cat_path, uploaded_filename)

			# save the uploaded file inside that folder.
			fout = open(full_filename, 'wb+')
			uploaded_filename = ContentFile(request.FILES['upload_file'].read())
			try:
				# Iterate through the chunks.
				for chunk in uploaded_filename.chunks():
					fout.write(chunk)
				fout.close()
			except:
				html = "<html><body>NOT SAVED</body></html>"
				return HttpResponse(html)

			doc = Dokumentus.objects.create(id=doc_id,doc_number=doc_number,category=cat ,klasifikasaun=klasifikasaun,subject=subject,given_by=given_by,orijen=orijen,destinu=diresaun_id,recieve_by=recieve_by,folder_name=folder_name,file_name=file_name,hashed=doc_hashed,status="Saved")
			doc.save()
			if 'save' in request.POST:
				messages.success(request, f'Document {doc_number} is Added Successfully.')
				return redirect('documents-list')
			elif 'save_and_add_another' in request.POST:
				messages.success(request, f'Document {doc_number} is Added Successfully.')
				return redirect('add-documents')
	
	notif_data = Dokumentus.objects.filter(status="Saved")
	notif_count = Dokumentus.objects.filter(status="Saved").count()
	context = {
		'title':"Form Documents",
		'doc_active':"active",
		'page':"add",
		'diresaun':diresaun,
		'notif_data':notif_data,
		'notif_count':notif_count,
		'categories':category
	}
	return render(request, 'form_documents.html', context)

@login_required
def detail_doc(request, hashid):
	cat = Category.objects.all()
	latest_docs = Dokumentus.objects.all().order_by('-date_created')[0:5]
	dokumentu = Dokumentus.objects.get(hashed=hashid)
	
	notif_data = Dokumentus.objects.filter(status="Saved")
	notif_count = Dokumentus.objects.filter(status="Saved").count()
	context = {
		'dokumentu':dokumentu,
		'title':"Detallu Dokumentu",
		'latest_docs':latest_docs,
		'doc_active':"active",
		'notif_data':notif_data,
		'notif_count':notif_count,	
		'categories':cat
		}
		
	return render(request, 'detail_doc.html', context)

@login_required
def generate_despacho(request,hashid):
	dokumentu = get_object_or_404(Dokumentus,hashed=hashid)
	presidente = get_object_or_404(Funsionariu,kargu__kargu="Prezidente")
	context = {
		'dokumentu':dokumentu,
		'presidente':presidente,
		'title':"File Despacho Dokumentu",
		}
		
	return render(request, 'print/generate_despacho.html', context)

@login_required
def detail_doc_sai(request, hashid):
	cat = Category.objects.all()
	# diresaun = Diresaun.objects.all()
	latest_docs_sai = DokumentuSai.objects.all().order_by('-date_created')[0:5]
	dokumentusai = DokumentuSai.objects.get(hashed=hashid)

	notif_data_sai = DokumentuSai.objects.filter(status="Saved")
	notif_count_sai = DokumentuSai.objects.filter(status="Saved").count()
	context = {
		'dokumentusai':dokumentusai,
		# 'diresaun':diresaun,
		'latest_docs_sai':latest_docs_sai,
		'categories':cat,
		'notif_data_sai':notif_data_sai,
		'notif_count_sai':notif_count_sai
	}
	return render(request, 'detail_doc_sai.html', context)

@login_required
def detail_respond_karta_tama(request, hashid):
	latest_docs = Dokumentus.objects.all().order_by('-date_created')[0:5]
	responde = Responde.objects.get(hashed=hashid)

	context = {
		'responde':responde,
		'latest_docs':latest_docs,
	}
	return render(request, 'detail_responde_karta_tama.html', context)


@login_required
def update_doc(request, hashid):
	dokumentu = get_object_or_404(Dokumentus, hashed=hashid)
	diresaun = Diresaun.objects.all()
	categories = Category.objects.all()

	form = DokumentuForm(instance=dokumentu)
	if request.method == 'POST':
		# print("Tama")
		form = DokumentuForm(request.POST, instance=dokumentu)
		print("Tama")
		if form.is_valid():
			print("Tama")
			form.save()
			return redirect('documents-list')
	context = {
		'form':form,
		'page':"update",
		'diresaun':diresaun,
		'dokumentu':dokumentu,
		'categories':categories
	}
	return render(request,'form_documents.html', context)

@login_required
def update_doc_sai(request, hashid):
	dokumentusai = get_object_or_404(DokumentuSai, hashed=hashid)
	dokumentusai = DokumentuSai.objects.get(hashed=hashid)
	diresaun = Diresaun.objects.all()
	categories = Category.objects.all()

	form = DokumentuSaiForm(instance=dokumentusai)
	print("Karta Sai La Tama")
	if request.method == 'POST':
		form = DokumentuSaiForm(request.POST, instance=dokumentusai)
		if form.is_valid():
			form.save()
			return redirect('documents-sai-list')
	context = {
		'form':form,
		'page':"update",
		'diresaun':diresaun,
		'dokumentusai':dokumentusai,
		'categories':categories
	}
	return render(request,'form_doc_sai.html', context)

@login_required
def detail_doc_notif(request, hashid):
	cat = Category.objects.all()
	latest_docs = Dokumentus.objects.all().order_by('-date_created')[0:5]
	dokumentu = Dokumentus.objects.get(hashed=hashid)
	if request.user.is_prezidente:
		dokumentu.president_viewed = True
		notif_data = Dokumentus.objects.filter(status="Saved",forward_to_president=True,president_viewed=False)
		notif_count = Dokumentus.objects.filter(status="Saved",forward_to_president=True,president_viewed=False).count()
	if request.user.is_vogal:
		dokumentu.vogal_viewed = True 
		notif_data = Dokumentus.objects.filter(status="Saved",forward_to_president=True,vogal_viewed=False)
		notif_count = Dokumentus.objects.filter(status="Saved",forward_to_president=True,vogal_viewed=False).count()
	if request.user.is_director:
		dokumentu.diretor_viewed = True
		notif_data = Dokumentus.objects.filter(status="Saved",forward_to_president=True,diretor_viewed=False)
		notif_count = Dokumentus.objects.filter(status="Saved",forward_to_president=True,diretor_viewed=False).count()
	if request.user.is_secretary:
		dokumentu.secretary_viewed = True
		notif_data = Dokumentus.objects.filter(status="Saved",forward_to_president=True,admin_viewed=False)
		notif_count = Dokumentus.objects.filter(status="Saved",forward_to_president=True,admin_viewed=False).count()
	
	dokumentu.save()
	
	context = {'dokumentu':dokumentu,'title':"Detallu Dokumentu",'latest_docs':latest_docs,'doc_active':"active",
		'notif_data':notif_data,
		'notif_count':notif_count,
		'categories':cat
	}		
	return render(request, 'detail_doc_notif.html', context)

@login_required
def detail_doc_sai_notif(request, hashid):
	cat = Category.objects.all()
	latest_doc_sai = DokumentuSai.objects.all().order_by('-date_created')[0:5]
	dokumentusai = DokumentuSai.objects.get(hashed=hashid)
	if request.user.is_prezidente:
		dokumentusai.president_viewed = True
		notif_data_sai = DokumentuSai.objects.filter(status="Saved",forward_to_president=True,president_viewed=False)
		notif_count_sai = DokumentuSai.objects.filter(status="Saved",forward_to_president=True,president_viewed=False).count()
	# if request.user.is_vogal:
	# 	dokumentu.vogal_viewed = True 
	# 	notif_data = Dokumentus.objects.filter(status="Saved",forward_to_president=True,vogal_viewed=False)
	# 	notif_count = Dokumentus.objects.filter(status="Saved",forward_to_president=True,vogal_viewed=False).count()
	if request.user.is_director:
		dokumentusai.diretor_viewed = True
		notif_data_sai = DokumentuSai.objects.filter(status="Saved",forward_to_admin=True,diretor_viewed=False)
		notif_count_sai = DokumentuSai.objects.filter(status="Saved",forward_to_admin=True,diretor_viewed=False).count()
	if request.user.is_secretary:
		dokumentusai.admin_viewed = True
		notif_data_sai = DokumentuSai.objects.filter(status="Saved",forward_to_president=True,admin_viewed=False)
		notif_count_sai = DokumentuSai.objects.filter(status="Saved",forward_to_president=True,admin_viewed=False).count()
	
	dokumentusai.save()
	
	context = {'dokumentusai':dokumentusai,'title':"Detallu Dokumentu Sai",'latest_doc_sai':latest_doc_sai,'doc_sai_active':"active",
		'notif_data_sai':notif_data_sai,
		'notif_count_sai':notif_count_sai,
		'categories':cat
	}		
	return render(request, 'detail_doc_sai_notif.html', context)


@login_required
def delete_doc(request, hashid):
	dokumentu = get_object_or_404(Dokumentus, hashed=hashid)
	dokumentu.delete()
	messages.success(request, f'Karta Tama Hamoos ho Susesu Ona.')
	return redirect('documents-list')

@login_required
def delete_doc_sai(request, hashid):
	dokumentusai = get_object_or_404(DokumentuSai, hashed=hashid)
	dokumentusai.delete()
	messages.success(request, f'Karta Sai Hamoos ho Susesu Ona.')
	return redirect('documents-sai-list')

@login_required
def detete_doc_sai_interna(request, hashid):
	kartainterna = get_object_or_404(DokumentuSaiInterna, hashed=hashid)
	kartainterna.delete()
	messages.success(request, f'Karta Sai Interna Hamoos ho Susesu Ona.')
	return redirect('karta_interna_list')

@login_required
def delete_cat(request, hashid):
	category = get_object_or_404(Category, hashed=hashid)
	category.delete()
	messages.warning(request, f'Category is Deleted Successfully.')
	return redirect('category-list')

@login_required
def categories_doc(request, hashid):
	cat = Category.objects.all()
	category = get_object_or_404(Category, hashed=hashid)
	# welcome = request.user
	# person = Funsionariu.objects.get(user=welcome)
	# diresaun_funsionariu = person.kargu.diresaun.id
	# print(diresaun_funsionariu)
	title = "Varanda Diretor"
	if request.user.is_director:
		welcome = request.user
		person = Funsionariu.objects.get(user=welcome)
		diresaun_funsionariu = person.kargu.diresaun.id
		cat_docs = Dokumentus.objects.filter(destinu=diresaun_funsionariu,category__hashed=hashid)
	if request.user.is_secretary:
		cat_docs = Dokumentus.objects.filter(category__hashed=hashid)
	if request.user.is_prezidente:
		cat_docs = Dokumentus.objects.filter(category__hashed=hashid)
	if request.user.is_vogal:
		user = request.user.id
		# title = "Varanda Vogal"
		vogal = Vogal.objects.get(user__id=user)
		diresaun_vogal = Diresaun.objects.filter(vogal=vogal)
		for i in diresaun_vogal:
			person = None
			cat_docs = Dokumentus.objects.filter(destinu=i.id,category__hashed=hashid)
		

	
	notif_data = Dokumentus.objects.filter(status="Saved")
	notif_count = Dokumentus.objects.filter(status="Saved").count()
		
	context = {
		'dokumentu':cat_docs,
		'category' : category,
		'cat':cat,
		'title':"Category Docs",'cat_active':"active",'categories':cat,'category':category,
		'notif_data':notif_data,
		'notif_count':notif_count 
	}
	return render(request, 'docs_category.html', context)

@login_required
def categories_doc_sai(request, hashid):
	cat = Category.objects.all()
	category = get_object_or_404(Category, hashed=hashid)
	title = "Varanda Diretor"
	if request.user.is_director:
		welcome = request.user
		person = Funsionariu.objects.get(user=welcome)
		diresaun_funsionariu = person.kargu.diresaun.id
		cat_docs = DokumentuSai.objects.filter(orijen=diresaun_funsionariu,category__hashed=hashid)
	if request.user.is_secretary:
		cat_docs = DokumentuSai.objects.filter(category__hashed=hashid)
	if request.user.is_prezidente:
		cat_docs = DokumentuSai.objects.filter(category__hashed=hashid)
	if request.user.is_vogal:
		user = request.user.id
		# title = "Varanda Vogal"
		vogal = Vogal.objects.get(user__id=user)
		diresaun_vogal = Diresaun.objects.filter(vogal=vogal)
		for i in diresaun_vogal:
			person = None
			cat_docs = DokumentuSai.objects.filter(destinu=i.id,category__hashed=hashid)

	print("Tama")
	notif_data_sai = DokumentuSai.objects.filter(status="Saved")
	notif_count_sai = DokumentuSai.objects.filter(status="Saved").count()
		
	context = {
		'dokumentusai':cat_docs,
		'category' : category,
		'cat':cat,
		'title':"Category Doc Sai",'cat_active':"active",'categories':cat,'category':category,
		'notif_data_sai':notif_data_sai,
		'notif_count_sai':notif_count_sai 
	}
	return render(request, 'doc_sai_category.html', context)



@login_required
def userlist(request):
	userlist = User.objects.all()
	cat = Category.objects.all()
	
	notif_data = Dokumentus.objects.filter(status="Saved")
	notif_count = Dokumentus.objects.filter(status="Saved").count()

	notif_data_sai = DokumentuSai.objects.filter(status="Saved")
	notif_count_sai = DokumentuSai.objects.filter(status="Saved").count()
	context = {
		'title':"Lista Utilizador",
		'categories':cat,
		'setting_active':"active",
		'userlist':userlist,
		'notif_data':notif_data,
		'notif_count':notif_count,
		'notif_data_sai':notif_data_sai,
		'notif_count_sai':notif_count_sai
	}
	return render(request, "settings.html", context)

@login_required
@csrf_exempt
def liveDocSave(request):
	id = request.POST.get('id','')
	type = request.POST.get('type','')
	value = request.POST.get('value','')
	doc = Dokumentus.objects.get(id=id)

	if type == "doc_number":
		doc_number = doc.doc_number
		doc.doc_number=value
		if doc_number != value:
			doc.save()
			messages.success(request, f'{doc_number} is Successfully Updated to {value}.')
		else :
			doc.save()
			
	if type == "subject":
		doc.subject = value
		doc.save()
		messages.success(request, f'Category is Added Successfully.')
	if type == "given_by":
		doc.given_by = value
		doc.save()
		messages.success(request, f'Category is Added Successfully.')
	if type == "recieve_by":
		doc.recieve_by = value
		doc.save()
		messages.success(request, f'Category is Added Successfully.')

	return JsonResponse({"success":"Updated"})

@login_required
def user_imajen_ajax(request):
	if not request.user.is_staff :
		if not request.user.is_vogal :
			funsionariu = Funsionariu.objects.get(user=request.user.id)
		# foto_user = funsionariu.foto
			print(funsionariu.foto)
		else :
			funsionariu = Vogal.objects.get(user=request.user.id)
	context = {
		'page':"imajen_user",
		'data':funsionariu
	}
	return render(request, 'ajax.html',context)


def sent_to_pre(request, hashid):
	doc = Dokumentus.objects.get(hashed = hashid)
	doc.forward_to_prezident = False
	# doc_sai.forward_to_prezident = True
	doc.save()
	return redirect('documents-list')

def sent_to_pre_inter(request, hashid):
	doc_inter = DokumentuSaiInterna.objects.get(hashed = hashid)
	doc_inter.forward_to_prezident = False
	# doc_inter.forward_to_prezident = True
	doc_inter.save()
	return redirect('karta_interna_list')

def sent_to_pre_sai(request, hashid):
	doc_sai = DokumentuSai.objects.get(hashed = hashid)
	doc_sai.forward_to_prezident = True
	doc_sai.save()
	return redirect('documents-sai-list')

def sent_to_vogal(request, hashid):
	dokumentusai = DokumentuSai.objects.get(hashed = hashid)
	dokumentusai.forward_to_vogal = True
	# doc_sai.forward_to_prezident = True
	dokumentusai.save()
	return redirect('documents-sai-list')

def adm_to_pre(request, hashid):
	doc_sai = DokumentuSai.objects.get(hashed = hashid)
	doc_sai.forward_to_prezident = True
	doc_sai.save()
	return redirect('documents-sai-list')
	
def dir_to_adm(request, hashid):
	doc_sai = DokumentuSai.objects.get(hashed = hashid)
	doc_sai.forward_to_admin = True
	doc_sai.forward_to_prezident = True
	doc_sai.save()
	return redirect('documents-sai-list')

def pre_halo_despacho(request, hashid):
	doc = Dokumentus.objects.get(hashed = hashid)
	diresaun = Diresaun.objects.all()
	notif_data = Dokumentus.objects.filter(status="Saved",forward_to_president=True,president_viewed=False)
	notif_count = Dokumentus.objects.filter(status="Saved",forward_to_president=True,president_viewed=False).count()
	if request.method == 'POST':
		despacho = request.POST.get('despacho')
		diresaun = request.POST.get('diresaun')
		diresaun = Diresaun.objects.get(id=diresaun)
		doc.president_despacho = despacho
		doc.president_despacho_diresaun = diresaun
		doc.forward_to_vogal = True
		doc.save()
		return redirect('documents-list')
	context = {
		'doc':doc,
		'title': 'Formulario Despacho',
		'legend': 'Formulario Despacho',
		'notif_data':notif_data,
		'notif_count':notif_count,
		'diresaun':diresaun
	}
	return render(request,'form_despacho.html',context)

# def pre_respond_karta_sai(request, hashid):
# 	dokumentusai = DokumentuSai.objects.get(hashed = hashid)
# 	diresaun = Diresaun.objects.all()
# 	notif_data = DokumentuSai.objects.filter(status="Saved",forward_to_president=True,president_viewed=False)
# 	notif_count = DokumentuSai.objects.filter(status="Saved",forward_to_president=True,president_viewed=False).count()
# 	if request.method == 'POST':
# 		despacho = request.POST.get('despacho')
# 		diresaun = request.POST.get('orijen')
# 		diresaun = Diresaun.objects.get(id=diresaun)
# 		dokumentusai.president_despacho = despacho
# 		dokumentusai.president_despacho_diresaun = diresaun
# 		dokumentusai.save()
# 		return redirect('documents-sai-list')
# 	context = {
# 		'dokumentusai':dokumentusai,
# 		'title': 'Formulario Despacho',
# 		'legend': 'Formulario Despacho',
# 		'notif_data':notif_data,
# 		'notif_count':notif_count,
# 		'diresaun':diresaun
# 	}
# 	return render(request,'form_respond_sai.html', context)


def pre_ba_admin(request, hashid):
	doc = Dokumentus.objects.get(hashed = hashid)
	doc.forward_to_vogal = True
	doc.save()
	return redirect('documents-list')

def pre_ba_vogal(request, hashid):
	doc_inter = DokumentuSaiInterna.objects.get(hashed = hashid)
	doc_inter.forward_to_vogal = True
	doc_inter.save()
	return redirect('karta_interna_list')

def vogal_ba_diresaun(request, hashid):
	doc = Dokumentus.objects.get(hashed = hashid)
	doc.forward_to_diresaun = True
	doc.save()
	return redirect('documents-list')

#  karta tama se bainhira karta ne'ebe mak tama ne'e kategoria pedidu ka proposta
def add_responde_karta_tama(request, hashid):
	doc = Dokumentus.objects.get(hashed = hashid)
	if request.method == "POST":
		form = RepondForm(request.POST,request.FILES)
		_, newid = getlastid(Responde)
		hashid = hash_md5(str(newid))
		if form.is_valid:
			instance = form.save(commit=False)
			instance.hashed = hashid
			# instance.forward_to_admin=True
			instance.karta_tama = doc
			instance.save()
			messages.success(request, f'Document {doc.doc_number} is Added Successfully.')
			return redirect('responde_list')
	else:
		form = RepondForm()	
	context = {
		'doc': doc,
		'form': form,
		# 'res': res,
		'title': 'Formulario Responde Karta Tama',
	}
	return render (request, 'form_responde.html', context)

def responde_karta_tama(request):
	res = Responde.objects.all()
	context = {
		'res': res,
		'title': 'Lista Karta Responde',
	}
	return render (request, 'respond_list.html',context)

@login_required
def add_karta_interna(request):
	category = Category.objects.all()

	# select diresaun bazeia ba diresaun ne'ebe mak nia servisu ba 
	welcome = request.user
	person = Funsionariu.objects.get(user=welcome)
	diresaun_funsionariu = person.kargu.diresaun.id
	diresaun = Diresaun.objects.filter(id=diresaun_funsionariu)
	# print("Latama")
	if request.method == "POST" and 'upload_file' in request.FILES:
		# print("Tama")
		_, newid = getlastid(DokumentuSaiInterna)
		hashid = hash_md5(str(newid))
		doc_id = newid
		doc_hashed = hashid
		doc_number = request.POST.get('doc_number')
		subject = request.POST.get('subject')
		# destinu = request.POST.get('destinu')
		orijen = request.POST.get('diresaun')

		print("diresaun_id:",diresaun)
		klasifikasaun = request.POST.get('klasifikasaun')
		diresaun_id = get_object_or_404(Diresaun,id=orijen)
		cat_id = request.POST.get('kat')
		cat = Category.objects.get(id=cat_id)
		cat_code = cat.cat_code

		file_name = request.FILES.get('upload_file')
		file_format = request.FILES['upload_file']
		folder_name = cat_code
		if not file_format.name.endswith('.pdf'):
			messages.warning(request, f'The uploaded file should in PDF format.')
		else :
			# kria folder bazeia ba codigo categoria.
			cat_path = 'doc_files/'+folder_name+'/'
			uploaded_filename = request.FILES['upload_file'].name
			if not os.path.exists(cat_path):
				os.makedirs(cat_path)
				file_name = folder_name+'/'+str(file_name)
				full_filename = os.path.join(cat_path, uploaded_filename)
			else:
				file_name = folder_name+'/'+str(file_name)
				full_filename = os.path.join(cat_path, uploaded_filename)

			# save the uploaded file inside that folder.
			fout = open(full_filename, 'wb+')
			uploaded_filename = ContentFile(request.FILES['upload_file'].read())
			try:
				# Iterate through the chunks.
				for chunk in uploaded_filename.chunks():
					fout.write(chunk)
				fout.close()
			except:
				html = "<html><body>NOT SAVED</body></html>"
				return HttpResponse(html)

			doc = DokumentuSaiInterna.objects.create(id=doc_id,doc_number=doc_number,category=cat,klasifikasaun=klasifikasaun,subject=subject,orijen=diresaun_id,folder_name=folder_name,file_name=file_name,hashed=doc_hashed,status="Saved")
			doc.save()
			if 'save' in request.POST:
				messages.success(request, f'Document {doc_number} is Added Successfully.')
				return redirect('karta_interna_list')
			elif 'save_and_add_another' in request.POST:
				messages.success(request, f'Document {doc_number} is Added Successfully.')
				return redirect('add_karta_interna')
	
	notif_data_sai = DokumentuSaiInterna.objects.filter(status="Saved")
	notif_count_sai = DokumentuSaiInterna.objects.filter(status="Saved").count()
	context = {
		'title':"Form Karta Interna",
		'doc_active':"active",
		'page':"add",
		'diresaun':diresaun,
		'notif_data_sai':notif_data_sai,
		'notif_count_sai':notif_count_sai,
		'categories':category
	}
	return render(request, 'form_karta_interna.html', context)


def karta_interna(request):
	# karta_sai_interna = DokumentuSaiInterna.objects.all()
	cat = Category.objects.all()
	if request.user.is_secretary:
		# Query ne'e fo sai katak secretaria haree detail tiha notifikasaun karta interna hafoin karta interna mosu iha lista karta interna nian. 
		karta_sai_interna = DokumentuSaiInterna.objects.filter(admin_viewed=True).all()

	if request.user.is_prezidente:
		# Query ne'e fo sai katak karta interna secretaria rai no input ona no forward ba prezidente los ona, prezidente mos haree detail ona iha notifikasaun.
		# hafoin karta interna mosu iha lista karta interna.
		karta_sai_interna = DokumentuSaiInterna.objects.filter(forward_to_president=True,president_viewed=True)
	
	if request.user.is_vogal:
		karta_sai_interna = DokumentuSaiInterna.objects.filter(forward_to_president=True,president_viewed=True,vogal_viewed=True)

	if request.user.is_director:
		# person = Funsionariu.objects.get(user=request.user)
		# diresaun_funsionariu = person.kargu.diresaun.id
		# # Query 
		karta_sai_interna = DokumentuSaiInterna.objects.filter(forward_to_president=True,president_viewed=True,vogal_viewed=True,forward_to_diresaun=True,diretor_viewed=True).all()

	context = {
		'title': 'Lista Karta Sai Interna',
		'cat' : cat,
		'karta_sai_interna': karta_sai_interna
	}
	return render(request, 'doc_interna_list.html', context)

@login_required
def detail_doc_sai_interna(request, hashid):
	cat = Category.objects.all()
	# diresaun = Diresaun.objects.all()
	latest_docs_sai_interna = DokumentuSaiInterna.objects.all().order_by('-date_created')[0:5]
	dokumentuinterna = DokumentuSaiInterna.objects.get(hashed=hashid)

	notif_data_sai_interna = DokumentuSaiInterna.objects.filter(status="Saved")
	notif_data_sai_interna = DokumentuSaiInterna.objects.filter(status="Saved").count()
	context = {
		'dokumentuinterna':dokumentuinterna,
		# 'diresaun':diresaun,
		'latest_docs_sai_interna':latest_docs_sai_interna,
		'categories':cat,
		'notif_data_sai_interna':notif_data_sai_interna,
		'notif_data_sai_interna':notif_data_sai_interna
	}
	return render(request, 'detail_doc_sai_interna.html', context)

def pre_despacho(request, hashid):
	doc_inter = DokumentuSaiInterna.objects.get(hashed = hashid)
	diresaun = Diresaun.objects.all()
	notif_data_sai_interna = DokumentuSaiInterna.objects.filter(status="Saved",forward_to_president=True,president_viewed=False)
	notif_count_sai_interna = DokumentuSaiInterna.objects.filter(status="Saved",forward_to_president=True,president_viewed=False).count()
	if request.method == 'POST':
		despacho = request.POST.get('despacho')
		diresaun = request.POST.get('diresaun')
		# diresaun = Diresaun.objects.get(id=diresaun)
		doc_inter.president_informa = despacho
		doc_inter.president_informa_diresaun = diresaun
		doc_inter.forward_to_vogal = True
		doc_inter.save()
		return redirect('karta_interna_list')
	context = {
		'doc_inter':doc_inter,
		'title': 'Formulario Despacho',
		'legend': 'Formulario Despacho',
		'notif_data_sai_interna':notif_data_sai_interna,
		'notif_count_sai_interna':notif_count_sai_interna,
		'diresaun':diresaun
	}
	return render(request,'form_pre_despacho.html',context)


# se error husu IndentationError: unindent does not match any outer indentation level tan nia tab sira nee seidauk loos sei sala hela
# se error husu IndentationError: expected an indented block tan nia tab sira ne'e seidauk loos sei sala



	

	

