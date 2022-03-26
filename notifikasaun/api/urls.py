from django.urls import path
from . import views

urlpatterns = [
	path('badge/',views.NotifBadge.as_view()),
	path('badge-karta-tama/',views.NotifKartaTama.as_view()),
	path('badge-responde-karta-tama/',views.NotifRespondeKartaTama.as_view()),
	path('badge-karta-sai/',views.NotifKartaSai.as_view()),
	path('badge-karta-sai-interna/',views.NotifKartaSaiInterna.as_view()),
]
