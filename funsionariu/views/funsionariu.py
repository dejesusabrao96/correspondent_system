from django.shortcuts import render,redirect
from ..form import *
from custom.utils import *
from ..models import *
from administrator.models import *
from users.models import *
# flash messages
from django.contrib import messages

# Create your views here.
def list_funsionariu(request):
	funsionariu = Funsionariu.objects.all()
	
	notif_data = Dokumentus.objects.filter(status="Saved")
	notif_count = Dokumentus.objects.filter(status="Saved").count()
	context = {
		"title":"Lista Funsionariu",
		"funsionariu_active":"active",
		"funsionariu":funsionariu,
		'notif_data':notif_data,
		'notif_count':notif_count
	}
	return render(request, "lista_funsionariu.html",context)

def ajax_load_kargu(request):
	diresaunid = request.GET.get('diresaun')
	kargu = Kargu.objects.filter(diresaun=diresaunid).order_by('id')
	context = {'kargu':kargu}

	return render(request, 'dependent_dropdown.html',context)

def add_funsionariu(request):
	diresaun = Diresaun.objects.all()
	if request.method == "POST":
		_, newid = getlastid(Funsionariu)
		hashid = hash_md5(str(newid))

		funsionariu_id = newid
		funsionariu_hashed = hashid
		naran = request.POST.get('naran')
		# vogalid = request.POST.get('vogal')
		# vogal = Vogal.objects.get(id=vogalid)
		email = request.POST.get('email')
		foto = request.FILES.get('foto')

		karguid = request.POST.get('kargu')
		if karguid:
			kargu = Kargu.objects.get(id=karguid)

		user_level = request.POST.get('level')
		if user_level == "Sec":
			form1 = User.objects.create(username=user_level+"_"+str(kargu.diresaun.codigu_diresaun))
			form1.set_password("password"+str(kargu.diresaun.codigu_diresaun))
			form1.is_secretary = True
			form1.email = email
			form1.save()
			funsionariu = Funsionariu.objects.create(id=funsionariu_id,naran_funsionariu=naran,kargu=kargu,hashed=funsionariu_hashed,foto=foto,user=form1)

		if user_level == "Pr":
			form1 = User.objects.create(username=user_level+"_"+str(kargu.diresaun.codigu_diresaun))
			form1.set_password("password"+str(kargu.diresaun.codigu_diresaun))
			form1.is_prezidente = True
			form1.email = email
			form1.save()
			funsionariu = Funsionariu.objects.create(id=funsionariu_id,naran_funsionariu=naran,kargu=kargu,hashed=funsionariu_hashed,foto=foto,user=form1)

		if user_level == "Dir":
			form1 = User.objects.create(username=user_level+"_"+str(kargu.diresaun.codigu_diresaun))
			form1.set_password("password"+str(kargu.diresaun.codigu_diresaun)+str(user_level))
			form1.is_director = True
			form1.email = email
			form1.save()
			funsionariu = Funsionariu.objects.create(id=funsionariu_id,naran_funsionariu=naran,kargu=kargu,hashed=funsionariu_hashed,foto=foto,user=form1)

		# if user_level == "Vg":
		# 	form1 = User.objects.create(username=user_level+"_"+str(vogal.vogal))
		# 	form1.set_password("password"+str(vogal.vogal))
		# 	form1.is_vogal = True
		# 	form1.email = email
		# 	form1.save()
		# 	funsionariu = Funsionariu.objects.create(id=funsionariu_id,naran_funsionariu=naran,vogal=vogal,hashed=funsionariu_hashed,foto=foto,user=form1)

		funsionariu.save()
		if 'save' in request.POST:
			messages.success(request, f'Funsionariu {naran} is Added Successfully.')
			return redirect('list-funsionariu')
		elif 'save_and_add_another' in request.POST:
			messages.success(request, f'Funsionariu {naran} is Added Successfully.')
			return redirect('add_funsionariu')
	
	notif_data = Dokumentus.objects.filter(status="Saved")
	notif_count = Dokumentus.objects.filter(status="Saved").count()


	context = {
		"title":"Add Funsionariu",
		"funsionariu_active":"active",
		"diresaun":diresaun,
		'notif_data':notif_data,
		'notif_count':notif_count
	}
	return render(request, "form_funsionariu.html", context)

def updateFun(request,hashid):
	if request.method == "GET":
		fun = Funsionariu.objects.get(hashed=hashid)
		form = FuncionarioForm(instance=fun)
		return render(request, "update_funcionario.html", {'form':form})

	
#def update_doc(request, hashid):
	#cat = Category.objects.all()
	#dokumentu = Dokumentus.objects.get(hashid=request.dokumentu.hashid)
#    dokumentu = Dokumentus.objects.get(hashed=hashid)
#    form = DokumentuForm(instance=dokumentu)

#    if request.method == 'POST':
#    	form = DokumentuForm(request.POST, instance=dokumentu)
#    	if form.is_valid():
#    		form.save()
#    		return redirect('/')
#    context = {'form':form}
#    return render(request,'update_doc.html', context)
	
	
def deleteFun(request,hashid):
	fun = Funsionariu.objects.get(hashed=hashid)
	userFun = User.objects.get(username=fun.user)
	fun.delete()
	userFun.delete()
	return redirect("list-funsionariu")

def addVogal(request):
	if request.method == "POST":
		_, newid = getlastid(Vogal)
		hashid = hash_md5(str(newid))
		vogal_id = newid
		vogal_hashed = hashid
		naran_vogal = request.POST.get('naran')
		# vogalid = request.POST.get('vogal')
		# vogal = Vogal.objects.get(id=vogalid)
		vogal = request.POST.get('vogal')
		email = request.POST.get('email')
		foto = request.FILES.get('foto')

		form1 = User.objects.create(username=vogal)
		form1.set_password("password"+str(vogal))
		form1.is_vogal = True
		form1.email = email
		form1.save()
		vogal = Vogal.objects.create(id=vogal_id,vogal=vogal,naran_vogal=naran_vogal,hashed=vogal_hashed,foto=foto,user=form1)
		vogal.save()
		if 'save' in request.POST:
			messages.success(request, f'Vogal {naran_vogal} is Added Successfully.')
			return redirect('list_vogal')
		elif 'save_and_add_another' in request.POST:
			messages.success(request, f'Vogal {naran_vogal} is Added Successfully.')
			return redirect('addVogal')
	context = {
		"title":"Lista Vogal & Prezidente",
		"vogal_active":"active",
		# 'notif_data':notif_data,
		# 'notif_count':notif_count
	}
	return render(request, "form_vogal.html", context)	

def list_vogal(request):
	vogal = Vogal.objects.all()
	context = {
		"title":"Lista Vogal & Prezidente",
		"vogal_active":"active",
		"vogal":vogal,
		# 'notif_data':notif_data,
		# 'notif_count':notif_count
	}
	return render(request, "lista_vogal.html", context)
