from django.shortcuts import render,redirect,get_object_or_404
from administrator.models import Dokumentus,DokumentuSai,Responde,DokumentuSaiInterna
from funsionariu.models import Funsionariu,Vogal,Diresaun
# Create your views here.

def notif_list_tama(request):
	if request.user.is_secretary:
		obj1 = Dokumentus.objects.filter(status="Saved",forward_to_president=False).all()

	if request.user.is_prezidente:
		obj1 = Dokumentus.objects.filter(status="Saved",forward_to_president=True,president_viewed=False).all()

	if request.user.is_vogal:
		vogal = Vogal.objects.get(user__id=request.user.id)
		obj1 = Dokumentus.objects.filter(status="Saved",forward_to_vogal=True,vogal_viewed=False,president_despacho_diresaun__vogal=vogal).all()
	
	if request.user.is_director:
		person = Funsionariu.objects.get(user=request.user)
		diresaun_funsionariu = person.kargu.diresaun.id
		obj1 = Dokumentus.objects.filter(status="Saved",destinu=diresaun_funsionariu,forward_to_president=True,president_viewed=True,president_despacho__isnull=False,president_despacho_diresaun=diresaun_funsionariu,vogal_viewed=True,forward_to_diresaun=True,diretor_viewed=False).all()
		# obj1 = Dokumentus.objects.filter(status="Saved",forward_to_president=True,president_viewed=True,president_despacho__isnull=False,president_despacho_diresaun=diresaun_funsionariu,vogal_viewed=True,forward_to_diresaun=True,diretor_viewed=False).all()
	
	# if request.user.is_director:
	# 	obj1 = Dokumentus.objects.filter(status="Saved",forward_to_diresaun=True,diretor_viewed=False).all()
	context = {
		"title":"Notifikasaun Karta Tama",
		"objects":obj1,
	}
	return render(request,'notif_list_tama.html',context)

def notif_list_responde(request):
	if request.user.is_secretary:
		# obj3 = Responde.objects.all()
		obj3 = Responde.objects.filter(forward_to_admin=True,admin_viewed=False).all()

	if request.user.is_prezidente:
		obj3 = Responde.objects.filter(forward_to_admin=True,admin_viewed=False).all()
		# obj3 = Responde.objects.filter(status="Saved",forward_to_admin=True).all()

	if request.user.is_vogal:
		obj3 = Responde.objects.filter(forward_to_admin=True,admin_viewed=False).all()
	
	if request.user.is_director:
		obj3 = Responde.objects.filter(forward_to_admin=True,admin_viewed=False).all()
		# obj3 = Responde.objects.filter(status="Saved",forward_to_admin=False).all()
		
	context = {
		"title":"Notifikasaun Responde Karta Tama",
		"objects":obj3,
	}
	return render(request,'notif_respond_list.html',context)

def notif_list_sai(request):
	if request.user.is_director:
		obj2 = DokumentuSai.objects.filter(status="Saved",forward_to_vogal=False).all()

	if request.user.is_vogal:
		obj2 = DokumentuSai.objects.filter(status="Saved",forward_to_vogal=True,vogal_viewed=False).all()

	if request.user.is_prezidente:
		obj2 = DokumentuSai.objects.filter(status="Saved",forward_to_president=True,president_viewed=False).all()

	if request.user.is_secretary:
		obj2 = DokumentuSai.objects.filter(status="Saved",forward_to_admin=True,admin_viewed=False).all()
		# obj2 = DokumentuSai.objects.filter(status="Saved",forward_to_vogal=True,vogal_viewed=True,president_viewed=True,forward_to_admin=True,admin_viewed=False).all()
	context = {
		"title":"Notifikasaun Karta Sai",
		"objects":obj2,
	}
	return render(request,'notif_list_sai.html',context)

def notif_list_sai_interna(request):
	if request.user.is_secretary:
		obj4 = DokumentuSaiInterna.objects.filter(status="Saved",forward_to_president=False).all()

	if request.user.is_prezidente:
		obj4 = DokumentuSaiInterna.objects.filter(status="Saved",forward_to_president=True,president_viewed=False).all()

	if request.user.is_vogal:
		# vogal = Vogal.objects.get(user__id=request.user.id)
		obj4 = DokumentuSaiInterna.objects.filter(status="Saved",forward_to_vogal=True,vogal_viewed=False).all()
	
	if request.user.is_director:
		# person = Funsionariu.objects.get(user=request.user)
		# diresaun_funsionariu = person.kargu.diresaun.id
		# obj4 = DokumentuSaiInterna.objects.filter(status="Saved",destinu=diresaun_funsionariu,forward_to_president=True,president_viewed=True,president_informa__isnull=False,president_informa_diresaun=diresaun_funsionariu,vogal_viewed=True,forward_to_diresaun=True,diretor_viewed=False).all()
		obj4 = DokumentuSaiInterna.objects.filter(status="Saved",forward_to_president=True,president_viewed=True,forward_to_vogal=True, vogal_viewed=True,forward_to_diresaun=True,diretor_viewed=False).all()
	# if request.user.is_director:
	# 	obj4 = Dokumentus.objects.filter(status="Saved",forward_to_diresaun=True,diretor_viewed=False).all()
	context = {
		"title":"Notifikasaun Karta Sai Interna",
		"objects":obj4,
	}
	return render(request,'notif_list_sai_interna.html',context)

def detailkartatama(request,id):
	latest_docs = Dokumentus.objects.all().order_by('-date_created')[0:5]
	kartaTama = get_object_or_404(Dokumentus,id=id)
	# dokumentu = Dokumentus.objects.get(hashed=hashid)
	if request.user.is_prezidente:
		kartaTama.president_viewed = True
		kartaTama.save()
	if request.user.is_secretary:
		kartaTama.admin_viewed = True
		kartaTama.save()
	if request.user.is_vogal:
		kartaTama.vogal_viewed = True
		kartaTama.save()
	if request.user.is_director:
		kartaTama.diretor_viewed = True
		kartaTama.save()
	
	context = {
		"title":"Detallu Karta Tama",
		"dokumentu":kartaTama,
		# "dokumentu":dokumentu,
	}
	return render(request,'detalluKartaTama.html',context)


def detailrespondekartatama(request,id):
	latest_docs = Responde.objects.all().order_by('-date_created')[0:5]
	respondeKartaTama = get_object_or_404(Responde,id=id)
	
	# Iha function ida ne'e bainhira secretaria haree detail ona karta responde notifcount menus ona.
	if request.user.is_secretary:
		respondeKartaTama.admin_viewed = True
		respondeKartaTama.save()
	
	
	context = {
		"title":"Detallu Responde Karta Tama",
		"dokumentu":respondeKartaTama,
	}
	return render(request,'detalluRespondeKartaTama.html',context)

def detailkartasai(request, id):
	latest_docs = DokumentuSai.objects.all().order_by('-date_created')[0:5]
	kartaSai = get_object_or_404(DokumentuSai, id=id)
	if request.user.is_prezidente:
		kartaSai.president_viewed = True
		kartaSai.save()
	if request.user.is_secretary:
		kartaSai.admin_viewed = True
		kartaSai.save()
	if request.user.is_vogal:
		kartaSai.vogal_viewed = True
		kartaSai.save()
	if request.user.is_director:
		kartaSai.diretor_viewed = True
		kartaSai.save()
	context = {
		"title":"Detallu Karta Tama",
		"dokumentusai":kartaSai,
	}
	return render(request, 'detalluKartaSai.html',context)

def detallu_karta_sai_interna(request, id):
	latest_docs_sai_interna = DokumentuSaiInterna.objects.all().order_by('-date_created')[0:5]
	kartaSaiInterna = get_object_or_404(DokumentuSaiInterna, id=id)
	if request.user.is_prezidente:
		kartaSaiInterna.president_viewed = True
		kartaSaiInterna.save()
	if request.user.is_secretary:
		kartaSaiInterna.admin_viewed = True
		kartaSaiInterna.save()
	if request.user.is_vogal:
		kartaSaiInterna.vogal_viewed = True
		kartaSaiInterna.save()
	if request.user.is_director:
		kartaSaiInterna.diretor_viewed = True
		kartaSaiInterna.save()
	context = {
		"title":"Detallu Karta Sai Interna",
		"dokumentuinterna":kartaSaiInterna,
	}
	return render(request, 'detalluKartaSaiInterna.html',context)

def sent_karta_sai_interna_ba_prezidente(request, hashid):
	doc_sai_inter = DokumentuSaiInterna.objects.get(hashed = hashid)
	doc_sai_inter.forward_to_president = True
	doc_sai_inter.save()
	return redirect('notif_list_sai_interna')

def kt_send_to_pre(request, hashid):
	doc = Dokumentus.objects.get(hashed = hashid)
	doc.forward_to_president = True
	doc.save()
	return redirect('notif_list_tama')

def kt_send_to_vogal(request, hashid):
	doc = Dokumentus.objects.get(hashed = hashid)
	doc.forward_to_diresaun = True
	doc.save()
	return redirect(notif_list_tama)

def kts_send_to_vogal(request, hashid):
	doc_sai = DokumentuSai.objects.get(hashed = hashid)
	doc_sai.forward_to_vogal = True
	doc_sai.save()
	return redirect(notif_list_sai)

def kts_send_to_pre(request, hashid):
	doc_sai = DokumentuSai.objects.get(hashed = hashid)
	doc_sai.forward_to_president = True
	doc_sai.save()
	return redirect(notif_list_sai)

def kts_send_to_admin(request, hashid):
	doc_sai = DokumentuSai.objects.get(hashed = hashid)
	doc_sai.forward_to_admin = True
	doc_sai.save()
	return redirect(notif_list_sai)

def ktr_send_to_admin(request, hashid):
	res = Responde.objects.get(hashed = hashid)
	res.forward_to_admin = True
	res.save()
	return redirect(notif_list_responde)

def ksi_vogal_to_diresaun(request, hashid):
	kartainterna = DokumentuSaiInterna.objects.get(hashed = hashid)
	kartainterna.forward_to_vogal = True
	kartainterna.save()
	return redirect(notif_list_sai_interna)



