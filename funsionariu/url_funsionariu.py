from django.urls import path
from . import views
# from .views import *

urlpatterns = [
	path('',views.list_funsionariu,name="list-funsionariu"),
	path('load_kargu',views.ajax_load_kargu,name="ajax_load_kargu"),
	path('add_funsionariu/',views.add_funsionariu,name="add_funsionariu"),
	path('deleteFun/<str:hashid>',views.deleteFun,name="deleteFun"),

	path('updateFun/<str:hashid>',views.updateFun,name="updateFun"),

	path('lista_vogal/',views.list_vogal,name="list_vogal"),
	path('add_Vogal/',views.addVogal,name="addVogal"),
	
]