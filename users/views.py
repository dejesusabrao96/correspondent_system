from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from administrator.models import *
from funsionariu.models import *
from .models import User
from .forms import UserUpdateForm
# flash messages
from django.contrib import messages
# PasswordChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate
# csrf using for live editable
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required
def userlist(request):
	userlist = User.objects.all()
	funsionariu = Funsionariu.objects.all()
	cat = Category.objects.all()
	
	notif_data = Dokumentus.objects.filter(status="Saved")
	notif_count = Dokumentus.objects.filter(status="Saved").count()
	context = {
		'title':"Lista Utilizador",
		'categories':cat,
		'funsionariu':funsionariu,
		'setting_active':"active",
		'userlist':userlist,
		'notif_data':notif_data,
		'notif_count':notif_count
	}
	return render(request, "settings.html", context)

@login_required
def accountUpdate(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		
		if u_form.is_valid():
			u_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('account-update')
	else:
		u_form = UserUpdateForm(instance=request.user)
	
	notif_data = Dokumentus.objects.filter(status="Saved")
	notif_count = Dokumentus.objects.filter(status="Saved").count()

	context = {
		'u_form': u_form,
		'title': 'ACCOUNT INFO',
		'legend': 'ACCOUNT INFO',
		'notif_data':notif_data,
		'notif_count':notif_count
	}
	return render(request, 'account.html', context)

@login_required
def changePassword(request):
	if request.method == 'POST':
		current_password = request.POST["old_password"]
		new_password = request.POST["new_password"]
		confirm_password = request.POST["confirm_password"]

		user = User.objects.get(id=request.user.id)
		un = user.username
		pwd = new_password
		check = user.check_password(current_password)
		if check==True:
			if new_password == confirm_password:
				user.set_password(new_password)
				user.save()
				authenticate(username = un, password = pwd)
				if request.user.is_authenticated:
					messages.info(request, f'Your password has been changed Successfuly!')
					return redirect('home')
			else:
				messages.warning(request, f'Your New password {new_password} and Confirmation Password {confirm_password} does not match!')
				return redirect('home')
		else:
			messages.warning(request, f'Your current password {current_password} is Incorrect!')
			return redirect('home')
	
	notif_data = Dokumentus.objects.filter(status="Saved")
	notif_count = Dokumentus.objects.filter(status="Saved").count()

	context = {
		'title': 'CHANGE PASSWORD',
		'legend': 'CHANGE PASSWORD',
		'notif_data':notif_data,
		'notif_count':notif_count
	}
	return render(request, 'changePassword.html', context)

@login_required
def profile(request):
	cat = Category.objects.all()
	if not request.user.is_staff:
		if not request.user.is_vogal:
			funsionariu = Funsionariu.objects.get(user=request.user.id)
		else:	
			funsionariu = Vogal.objects.get(user=request.user.id)
		
	notif_data = Dokumentus.objects.filter(status="Saved")
	notif_count = Dokumentus.objects.filter(status="Saved").count()
	context = {
		'title':"Profile Utilizador",
		'categories':cat,
		'profile':funsionariu,
		'notif_data':notif_data,
		'notif_count':notif_count
	}
	return render(request, 'profile.html',context)


@login_required
@csrf_exempt
def liveProfileSave(request):
	id = request.POST.get('id','')
	type = request.POST.get('type','')
	value = request.POST.get('value','')
	fun = Funsionariu.objects.get(id=id)

	if type == "naran_funsionariu":
		naran_funsionariu = fun.naran_funsionariu
		fun.naran_funsionariu=value
		if naran_funsionariu != value:
			fun.save()
			messages.success(request, f'{naran_funsionariu} is Successfully Updated to {value}.')
		else :
			fun.save()
	if type == "email":
		email = fun.user.email
		user_email = User.objects.get(email=email)
		user_email.email=value
		if email != value:
			user_email.save()
			messages.success(request, f'{email} is Successfully Updated to {value}.')
		else :
			user_email.save()
			
	return JsonResponse({"success":"Updated"})
