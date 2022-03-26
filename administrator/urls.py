from django.urls import path

from .views import *

urlpatterns = [
	path('',home,name="home"),
	path('documents/',documents,name="documents-list"),
	path('grid_documents/',grid_documents,name="documents-grid"),
	path('category_list/',category_list,name="category-list"),
	path('category-doc-sai-list/',category_doc_sai_list,name="category-doc-sai-list"),
	path('add_category/',add_category,name="add-category"),
	path('add_category_docsai/',add_category_docsai,name="add-category-docsai"),

	path('add_document/',add_document,name="add-documents"),

	path('detail_doc/<str:hashid>', detail_doc, name='detail_doc'),
	path('detail_respond_karta_tama/<str:hashid>', detail_respond_karta_tama, name='detail_respond_karta_tama'),
	path('generate_despacho/<str:hashid>', generate_despacho, name='generate_despacho'),
	path('update_doc/<str:hashid>', update_doc, name='update_doc'),

	path('categories_document/<str:hashid>', categories_doc, name='categories_doc'),
	path('categories_document_sai/<str:hashid>', categories_doc_sai, name='categories_doc_sai'),

	path('delete_dokumentu/<str:hashid>', delete_doc, name='delete_dokumentu'),
	path('delete_doc_sai/<str:hashid>', delete_doc_sai, name='delete_doc_sai'),
	path('delete_category/<str:hashid>', delete_cat, name='delete_category'),
# pdf report
    path('pdf_documents/',pdf_docs, name="pdf_docs"),
    path('pdf_docs_category/<str:hashid>', pdf_docs_category, name="pdf_docs_category"),
# csv reports
    path('csv_documents/', csv_documents, name="csv_documents"),
# charts
	path('documents-charts/',charts,name="charts"),
	path('document-sai-charts/',chart_docsai,name="charts-docsai"),
	path('charts1/',doc_charts,name="charts1"),
	path('charts2/',doc_charts,name="charts2"),
	
	path('charts3/',doc_sai_charts,name="charts3"),
	path('charts4/',doc_sai_charts,name="charts4"),


	path('documentSai/',documentSai,name="documents-sai-list"),

	path('addDocSai/',addDocSai,name="add-doc-sai"),

	path('update_doc_sai/<str:hashid>', update_doc_sai, name='update_doc_sai'),
	path('grid_document_sai/',grid_document_sai,name="grid-doc-sai"),
	path('detail_doc_sai/<str:hashid>',detail_doc_sai,name="detail-doc-sai"),
	path('pdf_doc_sai/',pdf_doc_sai,name="pdf-doc-sai"),



# settings
	# path('userlist/',userlist,name="user-list"),
# live editable api
	path('liveDocSave/',liveDocSave,name="liveDocSave"),

    path('notif_data/', load_notif_data, name='notif-data-url'),
    path('notif_data_sai/', load_notif_data_sai, name='notif-data-sai-url'),
    path('user_imajen_ajax/', user_imajen_ajax, name='user_imajen_ajax'),
	path('detail_doc_notif/<str:hashid>', detail_doc_notif, name='detail_doc_notif'),
	path('detail_doc_sai_notif/<str:hashid>', detail_doc_sai_notif, name='detail_doc_sai_notif'),
	
	path('sent_to_pre/<str:hashid>', sent_to_pre, name='sent_to_pre'),
	path('sent_to_pre_sai/<str:hashid>', sent_to_pre_sai, name='sent_to_pre_sai'),
	path('sent_to_vogal/<str:hashid>', sent_to_vogal, name='sent_to_vogal'),
	path('pre_halo_despacho/<str:hashid>', pre_halo_despacho, name='pre_halo_despacho'),
	path('pre_ba_admin/<str:hashid>', pre_ba_admin, name='pre_ba_admin'),
	path('vogal_ba_diresaun/<str:hashid>', vogal_ba_diresaun, name='vogal_ba_diresaun'),

	path('add_responde_karta_tama/<str:hashid>', add_responde_karta_tama, name='add_responde_karta_tama'),
	path('responde_karta_tama/', responde_karta_tama, name='responde_list'),
	# path('pre_respond_karta_sai/<str:hashid>', pre_respond_karta_sai, name='pre_respond_karta_sai'),

	path('dir_to_adm/<str:hashid>', dir_to_adm, name='dir-to-adm'),
	path('adm_to_pre/<str:hashid>', adm_to_pre, name='adm_to_pre'),


	# Report incoming and outgoing Letter
	path('report', report, name='report'),
	path('reportPrint', reportPrint, name='reportPrint'),
	

	path('charts_tipu_karta', charts_tipu_karta, name='charts_tipu_karta'),


	path('karta_interna', karta_interna, name='karta_interna_list'),
	path('add_karta_interna', add_karta_interna, name='add_karta_interna'),
	path('detete_doc_sai_interna/<str:hashid>', detete_doc_sai_interna, name='detete_doc_sai_interna'),
	path('detail_doc_sai_interna/<str:hashid>', detail_doc_sai_interna, name='detail_doc_sai_interna'),
	path('sent_to_pre_inter/<str:hashid>', sent_to_pre_inter, name='sent_to_pre_inter'),
	path('pre_despacho/<str:hashid>', pre_despacho, name='pre_despacho'),
	path('grid_karta_sai_interna/',grid_karta_sai_interna,name="grid_karta_sai_interna"),
	path('pdf_doc_sai_interna/',pdf_doc_sai_interna,name="pdf-doc-sai-interna"),
	path('pre_ba_vogal/<str:hashid>', pre_ba_vogal, name='pre_ba_vogal'),




	#path('update_doc/<str:hashid>', update_doc, name='update_doc'),
	


	



]