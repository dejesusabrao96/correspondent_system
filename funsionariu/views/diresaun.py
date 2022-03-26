from django.shortcuts import render,redirect
from ..form import *
from custom.utils import *
from ..models import *
from administrator.models import *
# flash messages
from django.contrib import messages

# Create your views here.

def list_diresaun(request):
	diresaun = Diresaun.objects.all()
	
	notif_data = Dokumentus.objects.filter(status="Saved")
	notif_count = Dokumentus.objects.filter(status="Saved").count()
	context = {
		"title":"Lista Diresaun || Unidade",
		# "funsionariu_active":"active",
		"diresaun":diresaun,
		'notif_data':notif_data,
		'notif_count':notif_count
	}
	return render(request, "lista_diresaun.html",context)

def add_diresaun(request):
	vogal = Vogal.objects.all()
	if request.method == "POST":
		_, newid = getlastid(Diresaun)
		hashid = hash_md5(str(newid))
		kodigu_diresaun = request.POST.get('kodigu_diresaun')
		diresaun = request.POST.get('diresaun1')
		print(diresaun)
		vogal = request.POST.get('vogal')
		vogal = Vogal.objects.get(id=vogal)

		if vogal == "None":
			instance = Diresaun.objects.create(codigu_diresaun=kodigu_diresaun,diresaun=diresaun,hashed=hashid)
			instance.save()
		else :
			instance = Diresaun.objects.create(codigu_diresaun=kodigu_diresaun,diresaun=diresaun,vogal=vogal,hashed=hashid)
			instance.save()
		if 'save' in request.POST:
			messages.success(request, f'Diresaun is Added Successfully.')
			return redirect('list_diresaun')
		elif 'save_and_add_another' in request.POST:
			messages.success(request, f'Diresaun is Added Successfully.')
			return redirect('add_diresaun')
	else :
		form = DiresaunForm()
	
	notif_data = Dokumentus.objects.filter(status="Saved")
	notif_count = Dokumentus.objects.filter(status="Saved").count()


	context = {
		"vogal":vogal,
		"page":"add",
		"button":"Save",
		"title":"Add Diresaun",
		"form":form,
		'notif_data':notif_data,
		'notif_count':notif_count

	}
	return render(request,"form_diresaun.html",context)

def update_diresaun(request,id):
	diresaun = Diresaun.objects.get(hashed=id)
	dir_name = diresaun.codigu_diresaun
	if request.method == "POST":
		form = DiresaunForm(request.POST, instance=diresaun)
		if form.is_valid():
			form.save()
			messages.success(request, f'Diresaun is Updated Successfully.')
			return redirect('list_diresaun')
	else :
		form = DiresaunForm(instance=diresaun)
	
	notif_data = Dokumentus.objects.filter(status="Saved")
	notif_count = Dokumentus.objects.filter(status="Saved").count()


	context = {
		"page":"update",
		"button":"update",
		"title": f"Update Diresaun {dir_name}",
		"form":form,
		'notif_data':notif_data,
		'notif_count':notif_count

	}
	return render(request,"form_diresaun.html",context)

def delete_diresaun(request,id):
	diresaun = Diresaun.objects.get(hashed=id)
	diresaun.delete()
	messages.success(request, f'Diresaun is Deleted Successfully.')
	return redirect('list_diresaun')