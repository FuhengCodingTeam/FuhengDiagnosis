from django.urls import path     
from . import views 
urlpatterns = [
    # main page
    path('', views.index),
    # path('search/<str:case_number>', views.searchCase),
    # patient register
    path('register', views.registerpage),
    path('register/new', views.patient_register),
    # patient dashboard
    path('dashboard', views.view_dashboard),

    # patient create newform
    path('newform', views.new_form),
    # path('newform/<int:form_id>/upload_files', views.form_upload_files),

    # for patient to login
    path('loginE', views.loginpageE),
    path('loginP', views.loginpageP),
    path('login/email', views.login_By_E),
    path('login/phone', views.login_By_P),

    
    
    # patient submit newform and upload files
    path('newform/<int:form_id>/new', views.new_patient_form),
    path('newform/<int:form_id>/tongue', views.uploadTongue),
    path('newform/<int:form_id>/leftEye', views.uploadLeftEye),
    path('newform/<int:form_id>/rightEye', views.uploadRightEye),
    path('newform/<int:form_id>/face', views.uploadFace),
    path('newform/<int:form_id>/files', views.uploadFiles),
    path('submit/success/<int:form_id>', views.submit_success),
    path('agreementCheck/<int:form_id>', views.agreemenetCheck),
    path('checkform/<int:form_id>', views.check_form),
    
    # login as host that can diagnosis, view patient detail, and delete patient, may need password
    path('host', views.host_portal_newest),
    path('host/oldest', views.host_portal_oldest),
    path('host/sortCaseNumber/Ascending',views.host_portal_sortby_caseNumber_ascending),
    path('host/sortCaseNumber/Decending',views.host_portal_sortby_caseNumber_descending),
    path('patient/<int:patient_id>/delete', views.delete_patient),
    path('patient/<int:patient_id>/detial', views.view_patient_detail),
    path('agreementCheck/<int:form_id>/<int:patient_id>/disable', views.agreementDisable),


    # host to view patient submitted form
    # path('patient/<int:patient_id>', views.formSubmit),
    # host to make diagnosis
    path('patient/<int:form_id>/seeResult', views.seeResult),
    path('patient/<int:form_id>/QA', views.seeIndexResultPage),
    path('patient/<int:form_id>/QA/complete', views.question_complete),
    path('patient/<int:form_id>/seeResult/page', views.seeResultPage),

    # logout
    path('logout', views.logout),

    # bad request
    path('not_found', views.not_found)
]