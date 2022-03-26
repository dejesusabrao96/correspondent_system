from django.http import HttpResponse
from django.shortcuts import redirect
from funsionariu.models import *

def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			# print('Working', allowed_roles)
			level = None
			if request.user.is_secretary:
				funsionariu = Funsionariu.objects.get(user=request.user.id)
				diresaun_user = funsionariu.kargu.diresaun.diresaun
				level = diresaun_user
			if request.user.is_staff:
				level = "is_staff"
			if request.user.is_director:
				level = "is_director"

			if level in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('La Autoriza Ita Boot Atu Haree Pajina Ida nee!')

		return wrapper_func
	return decorator