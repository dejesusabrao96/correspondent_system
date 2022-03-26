from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from administrator.models import Dokumentus,DokumentuSai,Responde,DokumentuSaiInterna
from funsionariu.models import Funsionariu,Vogal,Diresaun

# Views ba notifikasaun iha header nian
class NotifBadge(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request, format=None):
		if request.user.is_secretary:
			obj1 = Dokumentus.objects.filter(status="Saved",admin_viewed=False,forward_to_president=False).all().count()
			# total_notif = 0
			obj2 = DokumentuSai.objects.filter(status="Saved",forward_to_admin=True,admin_viewed=False).all().count()
			obj3 = Responde.objects.filter(admin_viewed=False).all().count()
			obj4 = DokumentuSaiInterna.objects.filter(status="Saved",admin_viewed=False,forward_to_president=False).all().count()
			objects = obj1+obj2+obj3+obj4
			return Response({'notifCount':objects})

		if request.user.is_director:
			person = Funsionariu.objects.get(user=request.user)
			diresaun_funsionariu = person.kargu.diresaun.id
			# obj1 = Dokumentus.objects.filter(status="Saved",forward_to_president=True,president_viewed=False).all().count()
			obj1 = Dokumentus.objects.filter(status="Saved",destinu=diresaun_funsionariu,forward_to_president=True,president_viewed=True,president_despacho__isnull=False,president_despacho_diresaun=diresaun_funsionariu,vogal_viewed=True,forward_to_diresaun=True,diretor_viewed=False).all().count()
			# obj2 = DokumentuSai.objects.filter(status="Saved",diretor_viewed=True,forward_to_vogal=False).all().count()
			obj2 = DokumentuSai.objects.filter(status="Saved",forward_to_vogal=False,diretor_viewed=False).all().count()
			obj3 = Responde.objects.filter(admin_viewed=False).all().count()
			objects = obj1+obj2+obj3
			return Response({'notifCount':objects})

		if request.user.is_prezidente:
			obj1 = Dokumentus.objects.filter(status="Saved",forward_to_president=True,president_viewed=False).all().count()
			# total_notif = 0
			obj2 = DokumentuSai.objects.filter(status="Saved",forward_to_president=True,president_viewed=False).all().count()
			obj3 = Responde.objects.filter(admin_viewed=False).all().count()
			obj4 = DokumentuSaiInterna.objects.filter(status="Saved",forward_to_president=True,president_viewed=False).all().count()
			objects = obj1+obj2+obj3
			return Response({'notifCount':objects})

		if request.user.is_vogal:
			vogal = Vogal.objects.get(user__id=request.user.id)
			diresaun_vogal = Diresaun.objects.filter(vogal=vogal)
			total_notif = 0
			for i in diresaun_vogal:
				obj1 = Dokumentus.objects.filter(status="Saved",forward_to_vogal=True,vogal_viewed=False,president_despacho_diresaun__id=i.id).all().count()
				obj2 = DokumentuSai.objects.filter(status="Saved",forward_to_vogal=True,vogal_viewed=False).all().count()
				total_notif = total_notif + obj1 + obj2
			return Response({'notifCount':total_notif})


class NotifKartaTama(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request, format=None):
		if request.user.is_secretary:
			objects = Dokumentus.objects.filter(status="Saved",admin_viewed=False,forward_to_president=False).all().count()
			return Response({'notifKartaTamaCount':objects})

		if request.user.is_prezidente:
			objects = Dokumentus.objects.filter(status="Saved",forward_to_president=True,president_viewed=False).all().count()
			return Response({'notifKartaTamaCount':objects})

		if request.user.is_vogal:
			vogal = Vogal.objects.get(user__id=request.user.id)
			diresaun_vogal = Diresaun.objects.filter(vogal=vogal)
			total_notif = 0
			for i in diresaun_vogal:
				obj1 = Dokumentus.objects.filter(status="Saved",forward_to_vogal=True,vogal_viewed=False,president_despacho_diresaun__id=i.id).all().count()
				total_notif = total_notif + obj1
			return Response({'notifKartaTamaCount':total_notif})

		if request.user.is_director:
			person = Funsionariu.objects.get(user=request.user)
			diresaun_funsionariu = person.kargu.diresaun.id
			objects = Dokumentus.objects.filter(status="Saved",destinu=diresaun_funsionariu,forward_to_president=True,president_viewed=True,president_despacho__isnull=False,president_despacho_diresaun=diresaun_funsionariu,vogal_viewed=True,forward_to_diresaun=True,diretor_viewed=False).all().count()
			return Response({'notifKartaTamaCount':objects})
		
class NotifRespondeKartaTama(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request, format=None):
		if request.user.is_secretary:
			objects = Responde.objects.filter(admin_viewed=False).all().count()
			return Response({'notifRespondeKartaTamaCount':objects})

		# if request.user.is_prezidente:
		# 	objects = Responde.objects.filter().all().count()
		# 	return Response({'notifRespondeKartaTamaCount':objects})

		# if request.user.is_vogal:
		# 	vogal = Vogal.objects.get(user__id=request.user.id)
		# 	diresaun_vogal = Diresaun.objects.filter(vogal=vogal)
		# 	total_notif = 0
		# 	for i in diresaun_vogal:
		# 		obj1 = Responde.objects.filter(status="Saved",forward_to_vogal=True,vogal_viewed=False,president_despacho_diresaun__id=i.id).all().count()
		# 		total_notif = total_notif + obj1
		# 	return Response({'notifRespondeKartaTamaCount':total_notif})

		# if request.user.is_director:
		# 	person = Funsionariu.objects.get(user=request.user)
		# 	diresaun_funsionariu = person.kargu.diresaun.id
		# 	objects = Responde.objects.filter(status="Saved",destinu=diresaun_funsionariu,forward_to_president=True,president_viewed=True,president_despacho__isnull=False,president_despacho_diresaun=diresaun_funsionariu,vogal_viewed=True,forward_to_diresaun=True,diretor_viewed=False).all().count()
		# 	return Response({'notifRespondeKartaTamaCount':objects})
		

class NotifKartaSai(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request, format=None):
		if request.user.is_director:
			person = Funsionariu.objects.get(user=request.user)
			diresaun_funsionariu = person.kargu.diresaun.id
			objects = DokumentuSai.objects.filter(status="Saved",orijen=diresaun_funsionariu,diretor_viewed=False,forward_to_vogal=False).all().count()
			return Response({'notifKartaSaiCount':objects})

		if request.user.is_vogal:
			objects = DokumentuSai.objects.filter(status="Saved",forward_to_vogal=True,vogal_viewed=False).all().count()
			# Fo sai notification count karta sai nian
			return Response({'notifKartaSaiCount':objects})

		if request.user.is_prezidente:
			objects = DokumentuSai.objects.filter(status="Saved",forward_to_president=True,president_viewed=False).all().count()
			return Response({'notifKartaSaiCount':objects})

		if request.user.is_secretary:
			# person = Funsionariu.objects.get(user=request.user)
			# diresaun_funsionariu = person.kargu.diresaun.id
			# objects = DokumentuSai.objects.filter(status="Saved",admin_viewed=True,forward_to_president=False).all().count()
			objects = DokumentuSai.objects.filter(status="Saved",forward_to_vogal=True,vogal_viewed=True,president_viewed=True,forward_to_president=True,admin_viewed=False).all().count()
			return Response({'notifKartaSaiCount':objects})
		
class NotifKartaSaiInterna(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request, format=None):
		if request.user.is_secretary:
			objects = DokumentuSaiInterna.objects.filter(status="Saved",admin_viewed=False,forward_to_president=False).all().count()
			return Response({'notifKartaSaiInternaCount':objects})

		if request.user.is_prezidente:
			objects = DokumentuSaiInterna.objects.filter(status="Saved",forward_to_president=True,president_viewed=False).all().count()
			return Response({'notifKartaSaiInternaCount':objects})

		if request.user.is_vogal:
			vogal = Vogal.objects.get(user__id=request.user.id)
			diresaun_vogal = Diresaun.objects.filter(vogal=vogal)
			total_notif = 0
			for i in diresaun_vogal:
				obj1 = DokumentuSaiInterna.objects.filter(status="Saved",forward_to_vogal=True,vogal_viewed=False,president_despacho_diresaun__id=i.id).all().count()
				total_notif = total_notif + obj1
			return Response({'notifKartaSaiInternaCount':total_notif})

		if request.user.is_director:
			person = Funsionariu.objects.get(user=request.user)
			diresaun_funsionariu = person.kargu.diresaun.id
			objects = DokumentuSaiInterna.objects.filter(status="Saved",destinu=diresaun_funsionariu,forward_to_president=True,president_viewed=True,president_despacho__isnull=False,president_despacho_diresaun=diresaun_funsionariu,vogal_viewed=True,forward_to_diresaun=True,diretor_viewed=False).all().count()
			return Response({'notifKartaSaiInternaCount':objects})