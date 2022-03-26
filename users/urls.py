from django.urls import path

from .views import *

urlpatterns = [
	path('userlist/',userlist,name="user-list"),
	path('accountUpdate/',accountUpdate,name="account-update"),
	path('changePassword/',changePassword,name="change-password"),
	path('profile/',profile,name="profile"),
	path('liveProfileSave/',liveProfileSave,name="liveProfileSave"),


	

	


]