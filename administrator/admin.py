from django.contrib import admin
from .models import *



# Register your models here.
class KategoriaAdmin(admin.ModelAdmin):
	list_display = ('cat_code','cat_name','hashed')

# class RespondAdmin(admin.ModelAdmin):
#  	list_display = ('karta_tama','hashed','date_respond','deskrisaun')

# class SubKategoriaAdmin(admin.ModelAdmin):
# 	list_display = ('id','subcat_code','subcat_name','category')

class DokumentuAdmin(admin.ModelAdmin):
	list_display = ('doc_number','klasifikasaun','subject','date_created','given_by','recieve_by','folder_name','file_name')

class DokumentuSaiAdmin(admin.ModelAdmin):
	list_display = ('doc_number','klasifikasaun','subject','date_created','folder_name','file_name','destinu')


admin.site.register(DokumentuSai, DokumentuSaiAdmin)
admin.site.register(Category, KategoriaAdmin)
admin.site.register(Responde)
admin.site.register(DokumentuSaiInterna)
# admin.site.register(Subcategory, SubKategoriaAdmin)
admin.site.register(Dokumentus, DokumentuAdmin)
#admin.site.register(DokumentuSai, DokumentuSaiAdmin)

