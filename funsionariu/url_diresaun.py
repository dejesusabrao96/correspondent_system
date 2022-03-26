from django.urls import path
from . import views
# from .views import *

urlpatterns = [
	path('',views.list_diresaun,name="list_diresaun"),
	path('add_diresaun/',views.add_diresaun,name="add_diresaun"),
	path('update_diresaun/<str:id>',views.update_diresaun,name="update_diresaun"),
	path('delete_diresaun/<str:id>',views.delete_diresaun,name="delete_diresaun"),

	path('lista_kargu/',views.list_kargu,name="list_kargu"),
	path('add_kargu/',views.add_kargu,name="add_kargu"),
	path('update_kargu/<str:id>',views.update_kargu,name="update_kargu"),
	path('delete_kargu/<str:id>',views.delete_kargu,name="delete_kargu"),

]