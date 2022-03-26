from django.shortcuts import render,redirect
from ..form import *
from custom.utils import *
from ..models import *
from administrator.models import *
# flash messages
from django.contrib import messages

def list_kargu(request):
	kargu = Kargu.objects.all()
	
	notif_data = Dokumentus.objects.filter(status="Saved")
	notif_count = Dokumentus.objects.filter(status="Saved").count()

	context = {
		"title":"Lista Kargu",
		"kargu":kargu,
		'notif_data':notif_data,
		'notif_count':notif_count
		# "funsionariu_active":"active",
	}
	return render(request, "lista_kargu.html",context)

def add_kargu(request):
	if request.method == "POST":
		_, newid = getlastid(Kargu)
		hashid = hash_md5(str(newid))

		form = KarguForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.id = newid
			instance.hashed = hashid
			instance.save()
			if 'save' in request.POST:
				messages.success(request, f'Kargu is Added Successfully.')
				return redirect('list_kargu')
			elif 'save_and_add_another' in request.POST:
				messages.success(request, f'Kargu is Added Successfully.')
				return redirect('add_kargu')
	else :
		form = KarguForm()
	
	notif_data = Dokumentus.objects.filter(status="Saved")
	notif_count = Dokumentus.objects.filter(status="Saved").count()

	context = {
		"page":"add",
		"button":"Save",
		"title":"Add Kargu Pozisaun",
		"form":form,
		'notif_data':notif_data,
		'notif_count':notif_count

	}
	return render(request,"form_kargu.html",context)

def update_kargu(request,id):
	kargu = Kargu.objects.get(hashed=id)
	kargu_name = kargu.codigu_kargu
	if request.method == "POST":
		form = KarguForm(request.POST, instance=kargu)
		if form.is_valid():
			form.save()
			messages.success(request, f'Kargu/Pozisaun is Updated Successfully.')
			return redirect('list_kargu')
	else :
		form = KarguForm(instance=kargu)
	
	notif_data = Dokumentus.objects.filter(status="Saved")
	notif_count = Dokumentus.objects.filter(status="Saved").count()

	context = {
		"page":"update",
		"button":"update",
		"title": f"Update Pozisaun {kargu_name}",
		"form":form,
		'notif_data':notif_data,
		'notif_count':notif_count

	}
	return render(request,"form_kargu.html",context)

def delete_kargu(request,id):
	kargu = Kargu.objects.get(hashed=id)
	kargu.delete()
	messages.success(request, f'Kargu/Pozisaun is Deleted Successfully.')
	return redirect('list_kargu')