from django.urls import path     
from . import views 
urlpatterns = [
    # main page
    path('', views.index),

    # for patient to submit form
    path('register', views.showform1),
    path('register/<int:patient_id>', views.showform2),
    path('register/<int:patient_id>/img', views.showform3),

    # for patient to view their case
    path('login', views.login),
    path('login/<str:case_number>', views.searchCase),
    
    # patient form submitted
    path('newPatient', views.newPatient),
    path('newPatient/<int:patient_id>/newform', views.newPatient_sympton),
    path('newPatient/<int:patient_id>/tongue', views.uploadTongue),
    path('newPatient/<int:patient_id>/leftEye', views.uploadLeftEye),
    path('newPatient/<int:patient_id>/rightEye', views.uploadRightEye),
    path('newPatient/<int:patient_id>/face', views.uploadFace),
    path('newPatient/<int:patient_id>/files', views.uploadFiles),
    path('submit/success/<int:patient_id>', views.submit_success),
    path('agreementCheck/<int:patient_id>', views.agreemenetCheck),
    
    # login as host that can diagnosis, view patient detail, and delete patient, may need password
    path('host', views.host_portal_newest),
    path('host/oldest', views.host_portal_oldest),
    path('host/sortCaseNumber/Ascending',views.host_portal_sortby_caseNumber_ascending),
    path('host/sortCaseNumber/Decending',views.host_portal_sortby_caseNumber_descending),
    path('patient/<int:patient_id>/delete', views.delete_patient),

    # host to view patient submitted form
    path('patient/<int:patient_id>', views.formSubmit),
    # host to make diagnosis
    path('patient/<int:patient_id>/detial', views.diagnosis),
    path('patient/<int:patient_id>/detail/verify', views.verifyDetail_patient),
    path('patient/<int:patient_id>/seeResult', views.seeResult),
    path('patient/<int:patient_id>/seeResult/page', views.seeResultPage)

]