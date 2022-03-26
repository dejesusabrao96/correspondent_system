import os
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.http import JsonResponse
from ..forms import KategoriaForm, DokumentuForm, DokumentuSaiForm, RepondForm
from custom.utils import *
from ..models import *

from datetime import date
from django.db.models import Count

from django.contrib.auth.decorators import login_required
from users.models import User

from django.core.files.base import ContentFile
# filter
from ..filters import DocsFilter, DocsSaiFilter

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
from django.db.models import Q
from datetime import date
# views here
@login_required
def pdf_docs(request):
	person = Funsionariu.objects.get(user=request.user)
	diresaun_funsionariu = person.kargu.diresaun.id
	# funsaun query ne'e fo sai katak diresaun ida idak bele export sai relatorio pdf tuir ninia diresaun labele asesu ba diresaun seluk. 
	docs = Dokumentus.objects.filter(destinu=diresaun_funsionariu)
	# funsaun ne'e fo sai katak se nia login nudar secretaria nia bele print sai rai relatorio kada diresaun nian.
	if request.user.is_secretary:
		docs = Dokumentus.objects.all()

	
	data ={'documents':docs,
			'title':"PDF Docs"}
	pdf = render_to_pdf('pdf/pdf_docs.html', data)
	return HttpResponse(pdf, content_type='application/pdf')

@login_required
def pdf_doc_sai(request):
	doc_sai = DokumentuSai.objects.all()
	# diresaun_funsionariu = person.kargu.diresaun.id
	data = {
		'doc_sai':doc_sai,
		'title':"PDF doc_sai"
	}
	pdf = render_to_pdf('pdf/pdf_doc_sai.html', data)
	return HttpResponse(pdf, content_type='application/pdf')

@login_required
def pdf_doc_sai_interna(request):
	doc_sai_interna = DokumentuSaiInterna.objects.all()
	# diresaun_funsionariu = person.kargu.diresaun.id
	data = {
		'doc_sai_interna':doc_sai_interna,
		'title':"PDF doc_sai_interna"
	}
	pdf = render_to_pdf('pdf/pdf_doc_sai_interna.html', data)
	return HttpResponse(pdf, content_type='application/pdf')

@login_required
def pdf_docs_category(request, hashid):
	cat_docs = Dokumentus.objects.filter(category__hashed=hashid) 
	category = get_object_or_404(Category, hashed=hashid)
	data = {
			'documents':cat_docs,
			'category':category,
			'title':"PDF Docs"
		}
	pdf = render_to_pdf('pdf/pdf_docs_category.html', data)
	return HttpResponse(pdf, content_type='application/pdf')


@login_required
def pdf_doc_sai_category(request, hashid):
	cat_doc_sai = DokumentuSai.objects.filter(category__hashed=hashid) 
	category = get_object_or_404(Category, hashed=hashid)
	data = {
			'documents':cat_doc_sai,
			'category':category,
			'title':"PDF Docs"
		}
	pdf = render_to_pdf('pdf/pdf_doc_sai_category.html', data)
	return HttpResponse(pdf, content_type='application/pdf')

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def csv_documents(request):
	docRes = DocRes()
	dataset = docRes.export()
	response = HttpResponse(dataset.csv, content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="dokumentu.csv"'	
	return response



# Report incoming and outgoing letter
def report(request):
	category = Category.objects.all()
	diresaun = Diresaun.objects.all()

	import calendar, datetime
	month = calendar.month_name[1:]
	years = [datetime.datetime.today().year - i for i in range(25)]

	context = {
	'month' : month,
	'years' : years,
	'category' : category,
	'diresaun' : diresaun,
	}
	return render (request, 'report/report.html', context)

def reportPrint(request):
	presidente = get_object_or_404(Funsionariu,kargu__kargu="Prezidente")
	currentDate = date.today()
	tipu_karta = request.GET['tipukarta']
	category = ""
	klasifikasaun = ""
	fulan = ""
	tinan = ""
	if tipu_karta == "Karta Sai":
		titulu_kategoria = ""
	elif tipu_karta == "Karta Tama":
		titulu_kategoria = ""

	if request.GET['category'] != "geral":
		category = " Q(category = request.GET['category'])"
		naran_kategoria = get_object_or_404(Category,id=request.GET['category'])
		titulu_kategoria = titulu_kategoria + " Kategoria : " + naran_kategoria.cat_name

	if request.GET['klasifikasaun'] != "geral":
		klasifikasaun = " & Q(klasifikasaun = request.GET['klasifikasaun'])"
		titulu_kategoria = titulu_kategoria + ", Klasifikasaun : " + request.GET['klasifikasaun']

	if request.GET['fulan'] != "geral":
		fulanID, fulanTetun = getFulanID(request.GET['fulan'])
		fulan = " & Q(date_created__month = "+ fulanID + ")"
		titulu_kategoria = titulu_kategoria + ", Fulan : " + fulanTetun

	if request.GET['tinan'] != "geral":
		tinan = " & Q(date_created__year = request.GET['tinan'])"
		titulu_kategoria = titulu_kategoria + ", Tinan : " + request.GET['tinan']
	
		
	if tipu_karta == "Karta Sai":
		getQueryset = "DokumentuSai.objects.filter("+ category + klasifikasaun + fulan + tinan + ")"
		dadusKarta = eval(getQueryset)


	elif tipu_karta == "Karta Tama":
		getQueryset = "Dokumentus.objects.filter("+ category + klasifikasaun + fulan + tinan + ")"
		dadusKarta = eval(getQueryset)


	context = {
		"tipu_karta": tipu_karta,
		"category": category,
		"klasifikasaun": klasifikasaun,
		"fulan": fulan,
		"tinan": tinan,
		"dadusKarta": dadusKarta,
		"presidente": presidente,
		"currentDate": currentDate,
		"titulu_kategoria": titulu_kategoria,
	}
	return render (request, 'report/report_print.html', context)