from django.urls import path     
from . import views 
urlpatterns = [
    # main page
    path('host', views.request_password),
    path('submit/developer', views.submit_password),
    path('page/not/ready', views.not_correct),
    path('verify',views.notice),
    path('', views.index),
    path('blog', views.show_blog),
    path('aboutus', views.show_about_us),
    path('intro', views.show_intro),
    path('joinus', views.show_join_us),
    path('joinus/new', views.new_join_us),
    path('joinus/submit', views.join_us_submit),



    # path('search/<str:case_number>', views.searchCase),
    # patient register
    path('register', views.registerpage),
    path('register/new', views.patient_register),
    # patient dashboard
    path('dashboard', views.view_dashboard),
    path('dashboard/allcase/<int:patient_id>', views.view_allcase),
    path('dashboard/<int:patient_id>/settings', views.patient_settings),
    path('patient/<int:patient_id>/detail/updateName', views.update_patient_name),
    path('patient/<int:patient_id>/detail/updateGender', views.update_patient_gender),
    path('patient/<int:patient_id>/detail/updatePhone', views.update_patient_phone ),
    path('patient/<int:patient_id>/detail/updateDob', views.update_patient_dob),


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
    path('newform/<int:patient_id>/<int:form_id>/files', views.uploadFiles),
    path('submit/success/<int:form_id>', views.submit_success),
    path('agreementCheck/<int:form_id>', views.agreemenetCheck),
    path('checkform/<int:form_id>', views.check_form),
    
    # login as host that can diagnosis, view patient detail, and delete patient, may need password
    path('host/login', views.host_portal_newest),
    path('host/message/new', views.hostCheckMessage),
    path('host/oldest', views.host_portal_oldest),
    path('host/newPatient', views.hostAddPatient),
    path('host/addPatient', views.hostCreatePatient),
    path('host/seepartners', views.see_partners),
    path('host/login/as/<int:patient_id>', views.hostCheckPatient),
    path('patient/<int:patient_id>/delete', views.delete_patient),
    path('patient/<int:patient_id>/detail', views.view_patient_detail),
    path('patient/<int:form_id>/<int:patient_id>/host/seeResult/page', views.hostCheckResultPage),
    path('patient/<int:form_id>/<int:patient_id>/seeResult/view/report', views.viewReport),
    path('host/<int:patient_id>/settings', views.host_edit_account),
    path('host/<int:patient_id>/detail/updateName', views.host_update_patient_name),
    path('host/<int:patient_id>/detail/updateGender', views.host_update_patient_gender),
    path('host/<int:patient_id>/detail/updatePhone', views.host_update_patient_phone ),
    path('host/<int:patient_id>/detail/updateDob', views.host_update_patient_dob),
    path('host/<int:patient_id>/detail/updateEmail', views.host_update_patient_email),
    path('host/resetpassword/<int:patient_id>', views.host_reset_password),
    # path('agreementCheck/<int:form_id>/<int:patient_id>/disable', views.agreementDisable),


    # host to view patient submitted form
    # path('patient/<int:patient_id>', views.formSubmit),
    # host to make diagnosis
    path('patient/<int:form_id>/seeResult', views.seeResult),
    path('patient/<int:form_id>/QA', views.seeIndexResultPage),
    path('patient/<int:form_id>/QA/complete', views.question_complete),
    path('patient/<int:form_id>/seeResult/page', views.seeResultPage),
    path('searchpatient', views.searchpatinet),
    path('form/<int:patient_id>/<int:form_id>/delete', views.delete_form),


    # logout
    path('logout', views.logout),

    # bad request
    path('not_found', views.not_found),

    # reset password
    path('resetPassword', views.resetPassword),
    path('reset/email', views.verifyEmail),
    path('reset/password', views.resetPatientPassword),


]
handler404 = "firstTrial.views.page_404_not_found_view"