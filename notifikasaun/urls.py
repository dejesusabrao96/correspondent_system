from django.urls import path
from . import views

urlpatterns = [
	path('notif_list_tama/',views.notif_list_tama,name="notif_list_tama"),
	path('notif_list_responde/',views.notif_list_responde,name="notif_list_responde"),
	path('notif_list_sai/',views.notif_list_sai,name="notif_list_sai"),


	path('notif_list_sai_interna/',views.notif_list_sai_interna,name="notif_list_sai_interna"),
	path('detallu_karta_sai_interna/<str:id>',views.detallu_karta_sai_interna,name="detallu_karta_sai_interna"),
	path('sent_karta_sai_interna_ba_prezidente/<str:hashid>',views.sent_karta_sai_interna_ba_prezidente,name="sent_karta_sai_interna_ba_prezidente"),


	path('detallu_karta_tama/<str:id>',views.detailkartatama,name="detailkartatama"),
	path('detallu_responde_karta_tama/<str:id>',views.detailrespondekartatama,name="detailrespondekartatama"),
	path('detallu_karta_sai/<str:id>',views.detailkartasai,name="detailkartasai"),
	path('sent_karta_tama_ba_prezidente/<str:hashid>',views.kt_send_to_pre,name="kt_send_to_pre"),
	path('sent_karta_tama_ba_vogal/<str:hashid>',views.kt_send_to_vogal,name="kt_send_to_vogal"),
	path('sent_karta_sai_ba_vogal/<str:hashid>',views.kts_send_to_vogal,name="kts_send_to_vogal"),
	path('sent_karta_sai_ba_pre/<str:hashid>',views.kts_send_to_pre,name="kts_send_to_pre"),
	path('sent_karta_sai_ba_admin/<str:hashid>',views.kts_send_to_admin,name="kts_send_to_admin"),
	path('sent_karta_responde_ba_admin/<str:hashid>',views.ktr_send_to_admin,name="ktr_send_to_admin"),


	path('ksi_vogal_to_diresaun/<str:hashid>',views.ksi_vogal_to_diresaun,name="ksi_vogal_to_diresaun"),


]
