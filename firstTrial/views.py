from distutils.log import error
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import json
from .models import *
import random
import datetime
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import bcrypt



first_diagram_partOne = {
    "lung": False,
    "pericardium": False,
    "heart": False,
}

second_diagram_partOne = {
    "lung": True,
    "pericardium": False,
    "heart": False,
}

third_diagram_partOne = {
    "lung": False,
    "pericardium": True,
    "heart": False,
}

fourth_diagram_partOne = {
    "lung": True,
    "pericardium": True,
    "heart": False,
}

fifth_diagram_partOne = {
    "lung": False,
    "pericardium": False,
    "heart": True,
}

sixth_diagram_partOne = {
    "lung": True,
    "pericardium": False,
    "heart": True,
}

seventh_diagram_partOne = {
    "lung": False,
    "pericardium": True,
    "heart": True,
}

eighth_diagram_partOne = {
    "lung": True,
    "pericardium": True,
    "heart": True,
}


first_diagram_partTwo = {
    "stomach":False,
    "gallbladder":False,
    "urinaryBladder":False,
}

second_diagram_partTwo ={
    "stomach":True,
    "gallbladder":False,
    "urinaryBladder":False,
}
    
third_diagram_partTwo = {
    "stomach": False,
    "gallbladder": True,
    "urinaryBladder": False,
}

fourth_diagram_partTwo = {
    "stomach": True,
    "gallbladder": True,
    "urinaryBladder": False,
}

fifth_diagram_partTwo = {
    "stomach": False,
    "gallbladder": False,
    "urinaryBladder": True,
}

sixth_diagram_partTwo = {
    "stomach": True,
    "gallbladder": False,
    "urinaryBladder": True,
}

seventh_diagram_partTwo = {
    "stomach": False,
    "gallbladder": True,
    "urinaryBladder": True,
}

eighth_diagram_partTwo = {
    "stomach":True,
    "gallbladder":True,
    "urinaryBladder":True,
}

first_diagram_partThree = {
    "spleen":False,
    "liver":False,
    "kidney":False,
}

second_diagram_partThree = {
    "spleen":True,
    "liver":False,
    "kidney":False,
}

third_diagram_partThree = {
    "spleen":False,
    "liver":True,
    "kidney":False,
}

fourth_diagram_partThree = {
    "spleen":True,
    "liver":True,
    "kidney":False,
}

fifth_diagram_partThree = {
    "spleen":False,
    "liver":False,
    "kidney":True,
}

sixth_diagram_partThree = {
    "spleen":True,
    "liver":False,
    "kidney":True,
}

seventh_diagram_partThree = {
    "spleen":False,
    "liver":True,
    "kidney":True,
}

eighth_diagram_partThree = {
    "spleen":True,
    "liver":True,
    "kidney":True,
}

first_diagram_partFour = {
    "large intestine":False,
    "san jiao":False,
    "small intestine":False,
}

second_diagram_partFour = {
    "large intestine":True,
    "san jiao":False,
    "small intestine":False,
}

third_diagram_partFour = {
    "large intestine":False,
    "san jiao":True,
    "small intestine":False,
}

fourth_diagram_partFour = {
    "large intestine":True,
    "san jiao":True,
    "small intestine":False,
}

fifth_diagram_partFour = {
    "large intestine":False,
    "san jiao":False,
    "small intestine":True,
}

sixth_diagram_partFour = {
    "large intestine":True,
    "san jiao":False,
    "small intestine":True,
}

seventh_diagram_partFour = {
    "large intestine":False,
    "san jiao":True,
    "small intestine":True,
}

eighth_diagram_partFour = {
    "large intestine":True,
    "san jiao":True,
    "small intestine":True,
}

def request_password(request):
    return render (request, "auth.html")
    
def submit_password(request):
    if request.method == 'GET':
        return redirect("/not_found")
    if request.POST['code'] != "2020HairRich":
        return redirect ("/page/not/ready")
    else:
        request.session['auth'] = True
        return redirect ("/host/login")

def not_correct(request):
    context ={
        "not_correct": "Invalid Password",
    }
    return render (request, 'auth.html', context)

def notice(request):
    if 'auth' not in request.session:
        return redirect("/host")
    else:
        return render (request, "verify.html")

def index(request):
    if "patient_id" not in request.session:
        return render (request, "index.html")
    else:
        context={
            "patient": Patient.objects.get(id=request.session['patient_id'])
        } 
        return render(request, "index.html", context)

def page_404_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def not_found(request):
    return render(request, "404.html")

def show_blog(request):
    return render (request,"blog.html")

def show_about_us(request):
    return render (request, "aboutus.html")

def show_intro(request):
    return render (request, "intro.html")

def show_join_us(request):
    return render (request, "joinus.html")

def new_join_us(request):
    if request.method == 'POST':
        Partner.objects.create(
            firstName = request.POST['firstName'],
            lastName = request.POST['lastName'],
            email = request.POST['email']
        )
        return redirect ("/joinus/submit")
    else:
        return redirect("joinus")

def join_us_submit(request):
    return render (request, "submit.html")

def see_partners(request):
    context = {
        "all_partners": Partner.objects.all(),
    }
    return render (request, "partners.html", context)

def host_edit_account(request, patient_id):
    context = {
        'patient':Patient.objects.get(id = patient_id)
    }
    return render (request, "editPatient.html", context)

def registerpage(request):
    currentdate = datetime.date.today().strftime("%d/%b/%y")
    context = {
        "today_date":currentdate,
        "default_date": datetime.date.today().strftime("%y-%d-%b"),
    }
    return render(request, "patientRegister.html", context)

def patient_register(request):
    errors = Patient.objects.register_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request,value,key)
        return redirect ("/register")
    else:
        if request.method == 'POST':
            new_patient = Patient.objects.create(
                firstName = request.POST['firstName'].lower(),
                lastName = request.POST['lastName'].lower(),
                phone_number = request.POST['phone'],
                email = request.POST['email'],
                sex = request.POST['sex'],
                date_of_birth = request.POST['date_of_birth'],
                # hearUs = request.POST['hearUs'],
                # referByFriend = request.POST['hearUsOther'],
                # insurance = request.POST['insurance'],
                # insuranceId = request.POST['insuranceId'],
                password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode(),
                )
            request.session['patient_id'] = new_patient.id
            return redirect (f"/dashboard")
        else:
            return redirect ("/register")

def loginpageE(request):
    currentdate = datetime.date.today().strftime("%d/%b/%y")
    context = {
        "today_date":currentdate,
        "default_date": datetime.date.today().strftime("%y-%d-%b"),
    }
    return render(request, "loginWithEmail.html", context)

def loginpageP(request):
    currentdate = datetime.date.today().strftime("%d/%b/%y")
    context = {
        "today_date":currentdate,
        "default_date": datetime.date.today().strftime("%y-%d-%b"),
    }
    return render(request, "loginWithPhone.html", context)

def login_By_E(request):
    if request.method == 'GET':
        return render (request, "404.html")
    errors = Patient.objects.login_validator_byEmail(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/loginE')
    else:
        user = Patient.objects.filter(email=request.POST['email'])
        patient = user[0]
        request.session['patient_id'] = patient.id
        return redirect('/dashboard')

def login_By_P(request):
    if request.method == 'GET':
        return render (request, "404.html")
    errors = Patient.objects.login_validator_byPhone(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/loginP')
    else:
        user = Patient.objects.filter(phone_number=request.POST['phone'])
        patient = user[0]
        request.session['patient_id'] = patient.id
        return redirect('/dashboard')


def view_dashboard(request):
    if "patient_id" not in request.session:
            return redirect('/loginE')
    else:
        login_id = request.session['patient_id']
        patient = Patient.objects.get(id=login_id)
        currentdate = datetime.date.today().strftime("%b/%d/%y")
        context={
            "patient": patient,
            "today_date":currentdate,
        }
        return render (request, "dashboard.html", context)

def view_allcase(request, patient_id):
    context = {
        "patient":Patient.objects.get(id=patient_id),
        "today_date":datetime.date.today().strftime("%b/%d/%y"),
        "patient_all_forms": PatientForm.objects.filter(patient=Patient.objects.get(id=patient_id)),
    }
    return render (request, "mycase.html", context)


def searchpatinet(request):
    if 'auth' not in request.session:
        return redirect("/host")
    else:
        if request.method == 'POST':   
            phoneEnter = request.POST['phone']
            patient = Patient.objects.filter(phone_number = phoneEnter)
            if not patient:
                messages.error(request, "No Patient Found")
                return redirect("/host/login")
            else:
                patient_to_view = patient[0]
                return redirect(f"/patient/{patient_to_view.id}/detail")

def hostAddPatient(request):
    if 'auth' not in request.session:
        return redirect("/host")
    else:
        return render (request, "hostNewPatient.html")

def hostCreatePatient(request):
    if 'auth' not in request.session:
        return redirect("/host")
    else:
        if request.method == 'POST':
            new_patient = Patient.objects.create(
                firstName = request.POST['firstName'].lower(),
                lastName = request.POST['lastName'].lower(),
                phone_number = request.POST['phone'],
                email = request.POST['email'],
                sex = request.POST['sex'],
                date_of_birth = request.POST['date_of_birth'],
                )
            return redirect ("/host/login")
        else:
            return redirect ("/host/newPatient")

def hostCheckPatient(request, patient_id):
    if 'auth' not in request.session:
        return redirect("/host")
    request.session['patient_id'] = patient_id
    context={
        "patient":Patient.objects.get(id=patient_id)
    }
    return render (request, "dashboard.html", context)

def hostCheckMessage(request):
    if 'auth' not in request.session:
        return redirect("/host")
    return render (request, "verify.html")

def new_patient_form(request, form_id):
    if "patient_id" not in request.session:
        return redirect('/not_found')
    else:
        new_form = PatientForm.objects.get(id=form_id)
        currentdate = datetime.date.today().strftime("%d/%b/%y")
        new_patient = Patient.objects.get(id=request.session['patient_id'])
        context = {
            "today_date":currentdate,
            "default_date": datetime.date.today().strftime("%y-%d-%b"),
            "patient":new_patient,
            "form":new_form
        }
        
        return render(request, "newPatientFormUploadFiles.html", context)

# def form_upload_files(request, form_id, patient_id):
#     if "patient_id" not in request.session:
#         return redirect('/not_found')
#     else:
#         currentdate = datetime.date.today().strftime("%d/%b/%y")
#         new_form = PatientForm.objects.get(id=form_id)
#         new_patient = Patient.objects.get(id=patient_id)
#         context = {
#             "today_date":currentdate,
#             "default_date": datetime.date.today().strftime("%y-%d-%b"),
#             "patient":new_patient,
#         }
#         return render(request, "newPatientFormUploadFiles.html", context)

def new_form(request):
    new_patient = Patient.objects.get(id=request.session['patient_id']) 
    if request.method == 'GET':
        return redirect("/not_found") 
    if request.method == 'POST':    
        def random_string():
                return str(random.randint(10000, 99999))
        new_form = PatientForm.objects.create(
            caseNumber = random_string(),
            patient = new_patient
        )
        return redirect (f"/newform/{new_form.id}/new")

def uploadTongue(request, form_id):
        form = PatientForm.objects.get(id=form_id)
        if request.method == 'POST':
            form.tongueCoat = request.FILES.get("uploadImg")
            form.save()
            return redirect (f"/newform/{form.id}/new")
        else:
            return redirect("/not_found")

def uploadLeftEye(request, form_id):
        form = PatientForm.objects.get(id=form_id)
        if request.method == 'POST':
            form.leftEye = request.FILES.get("uploadImg")
            form.save()
            return redirect (f"/newform/{form.id}/new")
        else:
            return redirect("/not_found")

def uploadRightEye(request, form_id):
        form = PatientForm.objects.get(id=form_id)
        if request.method == 'POST':
            form.rightEye = request.FILES.get("uploadImg")
            form.save()
            return redirect (f"/newform/{form.id}/new")
        else:
            return redirect("/not_found")

def uploadFace(request, form_id):
        form = PatientForm.objects.get(id=form_id)
        if request.method == 'POST':
            form.face = request.FILES.get("uploadImg")
            form.save()
            return redirect (f"/newform/{form.id}/new")
        else:
            return redirect("/not_found")

def uploadFiles(request, form_id, patient_id):
    patient = Patient.objects.get(id=patient_id)
    form = PatientForm.objects.get(id=form_id)
    if request.method == 'POST':
        patientUploadFile = request.FILES.getlist("medicalRecord")
        for oneFile in patientUploadFile:
            PatientFiles.objects.create(
                file = oneFile,
                patient = patient
                )
        return redirect (f"/newform/{form.id}/new")
    else:
        return redirect("/not_found")



def agreemenetCheck (request, form_id):
    if "patient_id" not in request.session:
        return redirect('/not_found')
    else:
        new_patient = Patient.objects.get(id=request.session['patient_id'])
        form = PatientForm.objects.get(id=form_id)
        if request.method == 'GET':
            return redirect('/not_found')
        if request.method == 'POST':
            form.agreementCheck = True
            patient_phone = new_patient.phone_number

            # getting patient phone last 3 dight, if somewhere is 0, we will move on to the perious dight
            def find_last_Index():
                for x in range(1,11,1):
                    if (patient_phone[len(patient_phone)-x] != "0"):
                        return x
            def find_second_Index():
                for y in range(find_last_Index()+1,11,1):
                    if (patient_phone[len(patient_phone)-y] != "0"):
                        return y

            def find_first_Index():
                for z in range(find_second_Index()+1,11,1):
                    if (patient_phone[len(patient_phone)-z] != "0"):
                        return z

            secondIndex = patient_phone[len(patient_phone)-find_second_Index()]
            firstIndex = patient_phone[len(patient_phone)-find_first_Index()]
            lastIndex = patient_phone[len(patient_phone)-find_last_Index()]

            # assign different diagram with different number in specific index
            # may remove as only the result will be needed
            def diagnosis_first_index():
                if (firstIndex == "1") or (firstIndex == "9"):
                    first_diagnosis = first_diagram_partOne
                    return first_diagnosis
                if firstIndex == "2":
                    first_diagnosis = second_diagram_partOne
                    return first_diagnosis
                if firstIndex == "3":
                    first_diagnosis = third_diagram_partOne
                    return first_diagnosis
                if firstIndex == "4":
                    first_diagnosis = fourth_diagram_partOne
                    return first_diagnosis
                if firstIndex == "5":
                    first_diagnosis = fifth_diagram_partOne
                    return first_diagnosis
                if firstIndex == "6":
                    first_diagnosis = sixth_diagram_partOne
                    return first_diagnosis
                if firstIndex == "7":
                    first_diagnosis = seventh_diagram_partOne
                    return first_diagnosis
                if firstIndex == "8":
                    first_diagnosis = eighth_diagram_partOne
                    return first_diagnosis
            
            
            def diagnosis_second_index(): 
                if (secondIndex == "1") or (secondIndex == "9"):
                    second_diagnosis = first_diagram_partTwo
                    return second_diagnosis
                if secondIndex == "2":
                    second_diagnosis = second_diagram_partTwo
                    return second_diagnosis
                if secondIndex == "3":
                    second_diagnosis = third_diagram_partTwo
                    return second_diagnosis
                if secondIndex == "4":
                    second_diagnosis = fourth_diagram_partTwo
                    return second_diagnosis
                if secondIndex == "5":
                    second_diagnosis = fifth_diagram_partTwo
                    return second_diagnosis
                if secondIndex == "6":
                    second_diagnosis = sixth_diagram_partTwo
                    return second_diagnosis
                if secondIndex == "7":
                    second_diagnosis = seventh_diagram_partTwo
                    return second_diagnosis
                if secondIndex == "8":
                    second_diagnosis = eighth_diagram_partTwo
                    return second_diagnosis
            
            def diagnosis2_first_index():
                if (lastIndex == "1") or (lastIndex == "9"):
                    third_diagnosis = first_diagram_partThree
                    return third_diagnosis
                if (lastIndex == "2"):
                    third_diagnosis = second_diagram_partThree
                    return third_diagnosis
                if (lastIndex == "3"):
                    third_diagnosis = third_diagram_partThree
                    return third_diagnosis
                if (lastIndex == "4"):
                    third_diagnosis = fourth_diagram_partThree
                    return third_diagnosis
                if (lastIndex == "5"):
                    third_diagnosis = fifth_diagram_partThree
                    return third_diagnosis
                if (lastIndex == "6"):
                    third_diagnosis = sixth_diagram_partThree
                    return third_diagnosis
                if (lastIndex == "7"):
                    third_diagnosis = seventh_diagram_partThree
                    return third_diagnosis
                if (lastIndex == "8"):
                    third_diagnosis = eighth_diagram_partThree
                    return third_diagnosis

            def diagnosis2_second_index():
                if (secondIndex == "1") or (secondIndex == "9"):
                    fourth_diagnosis = first_diagram_partFour
                    return fourth_diagnosis
                if secondIndex == "2":
                    fourth_diagnosis = second_diagram_partFour
                    return fourth_diagnosis
                if secondIndex == "3":
                    fourth_diagnosis = third_diagram_partFour
                    return fourth_diagnosis
                if secondIndex == "4":
                    fourth_diagnosis = fourth_diagram_partFour
                    return fourth_diagnosis
                if secondIndex == "5":
                    fourth_diagnosis = fifth_diagram_partFour
                    return fourth_diagnosis
                if secondIndex == "6":
                    fourth_diagnosis = sixth_diagram_partFour
                    return fourth_diagnosis
                if secondIndex == "7":
                    fourth_diagnosis = seventh_diagram_partFour
                    return fourth_diagnosis
                if secondIndex == "8":
                    fourth_diagnosis = eighth_diagram_partFour
                    return fourth_diagnosis

            # specify the initial diagram to modify
            # initial_diagnosis = json.dumps(diagnosis_first_index())[1:-1]+" "+json.dumps(diagnosis_second_index())[1:-1] + " " + json.dumps(diagnosis2_first_index())[1:-1] + " " + json.dumps(diagnosis2_second_index())[1:-1]
            result1 = Merge(diagnosis_first_index(),diagnosis_second_index())
            result2 = Merge(diagnosis2_first_index(), diagnosis2_second_index())
            initial_statement = Merge(result1,result2)
            form.diagnosisInitial = json.dumps(initial_statement)
            form.save()
            new_patient.save()
            return redirect (f"/submit/success/{form.id}")

def submit_success(request, form_id):
    if "patient_id" not in request.session:
        return redirect('/not_found')
    else:
        context={
            "patient": Patient.objects.get(id=request.session['patient_id']),
            "form": PatientForm.objects.get(id=form_id),
            "today_date":datetime.date.today().strftime("%b/%d/%y"),
        }
        return render(request, "success.html", context)

def check_form(request, form_id):
    if "patient_id" not in request.session:
        return redirect('/not_found')
    else:
        patient = Patient.objects.get(id = request.session['patient_id'])
        form = PatientForm.objects.get(id=form_id)
        if form.agreementCheck == False:
            return redirect (f"/newform/{form.id}/new")
        if form.question == False:
            return (f"/patient/{form.id}/QA")
        else:
            return redirect (f"/patient/{form.id}/seeResult/page")

def host_portal_newest(request):
    if 'auth' not in request.session:
        return redirect("/host")
    else:
        context={
            "all_patients": Patient.objects.all(),
            "all_forms": PatientForm.objects.all(),
            # "no_diagnosis_patients": Patient.objects.exclude(diagnosis='True')
        }
        return render(request, "host.html", context)

def host_portal_oldest(request):
    if 'auth' not in request.session:
        return redirect("/host")
    else:
        context={
            "all_patients": Patient.objects.order_by("-created_at"),
            "all_forms": PatientForm.objects.all(),
        }
        return render(request, "host.html", context)


def delete_patient(request, patient_id):
    if 'auth' not in request.session:
        return redirect("/host")
    else:
        patient_to_delete = Patient.objects.get(id=patient_id)
        patient_to_delete.delete()
        return redirect ("/host/login") 

def delete_form(request,patient_id, form_id):
    if 'auth' not in request.session:
        return redirect("/host")
    else:
        form = PatientForm.objects.get(id=form_id)
        patient = Patient.objects.get(id=patient_id)
        form.delete()
        return redirect (f"/patient/{patient.id}/detail") 

def Merge(dict1, dict2):
    d = dict1.copy()
    d.update(dict2)
    return d  

def view_patient_detail(request, patient_id):
    if 'auth' not in request.session:
        return redirect("/host")
    else:
        patient_to_view = Patient.objects.get(id=patient_id)
        context = {
            "patient": patient_to_view,
            "patient_all_forms": PatientForm.objects.filter(patient=patient_to_view),
        }
        return render (request, "patient.html", context)

def patient_settings(request, patient_id):
    patient = Patient.objects.get(id = patient_id)
    context = {
        "patient":patient
    }
    return render (request, 'patientsetting.html', context)

def update_patient_name(request, patient_id):
    if request.method == 'POST':
        patient_to_view = Patient.objects.get(id=patient_id)
        errors = Patient.objects.update_name(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ('/dashboard/patient/settings')
        else:    
            patient_to_view.firstName = request.POST['firstName']
            patient_to_view.lastName = request.POST['lastName']
            patient_to_view.save()
            return redirect('/dashboard/patient/settings')

def update_patient_gender(request, patient_id):
    if request.method == 'POST':
        patient_to_view = Patient.objects.get(id=patient_id)
        patient_to_view.sex = request.POST['sex']      
        patient_to_view.save()
        return redirect('/dashboard/patient/settings')

def update_patient_dob(request, patient_id):
    if request.method == 'POST':
        patient_to_view = Patient.objects.get(id=patient_id)
        patient_to_view.date_of_birth = request.POST['date_of_birth']
        patient_to_view.save()
        return redirect('/dashboard/patient/settings')

def update_patient_phone(request, patient_id):
    if request.method == 'POST':
        patient_to_view = Patient.objects.get(id=patient_id)
        errors = Patient.objects.update_phone(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ('/dashboard/patient/settings')
        else:    
            patient_to_view.phone_number = request.POST['phone']
            patient_to_view.save()
            return redirect('/dashboard/patient/settings')

def host_update_patient_name(request, patient_id):
    if request.method == 'POST':
        patient_to_view = Patient.objects.get(id=patient_id)
        errors = Patient.objects.update_name(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect (f'/host/{patient_to_view.id}/settings')
        else:    
            patient_to_view.firstName = request.POST['firstName']
            patient_to_view.lastName = request.POST['lastName']
            patient_to_view.save()
            return redirect(f'/host/{patient_to_view.id}/settings')

def host_update_patient_gender(request, patient_id):
    if request.method == 'POST':
        patient_to_view = Patient.objects.get(id=patient_id)
        patient_to_view.sex = request.POST['sex']      
        patient_to_view.save()
        return redirect(f'/host/{patient_to_view.id}/settings')

def host_update_patient_dob(request, patient_id):
    if request.method == 'POST':
        patient_to_view = Patient.objects.get(id=patient_id)
        patient_to_view.date_of_birth = request.POST['date_of_birth']
        patient_to_view.save()
        return redirect(f'/host/{patient_to_view.id}/settings')

def host_update_patient_phone(request, patient_id):
    if request.method == 'POST':
        patient_to_view = Patient.objects.get(id=patient_id)
        errors = Patient.objects.update_phone(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect (f'/host/{patient_to_view.id}/settings')
        else:    
            patient_to_view.phone_number = request.POST['phone']
            patient_to_view.save()
            return redirect(f'/host/{patient_to_view.id}/settings')

def host_update_patient_email(request, patient_id):
    if request.method == 'POST':
        patient_to_view = Patient.objects.get(id=patient_id)
        patient_to_view.email = request.POST['email']
        patient_to_view.save()
        return redirect(f'/host/{patient_to_view.id}/settings')

def host_reset_password(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    if request.method == 'POST':
        reset = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        patient.password = reset
        patient.save()
        return redirect (f'/host/{patient.id}/settings')

def seeResult(request, form_id):
    patient_to_view = Patient.objects.get(id=request.session['patient_id'])
    patient_phone = patient_to_view.phone_number
    form = PatientForm.objects.get(id=form_id)
    if request.method == 'GET':
        context={
            "patient": patient_to_view,
            "final_diagnosis": form.diagnosisResult
        }
        return render (request, "seeResult.html", context)
    if request.method == 'POST':
                # getting patient phone last 3 dight, if somewhere is 0, we will move on to the perious dight
        def find_last_Index():
            for x in range(1,11,1):
                if (patient_phone[len(patient_phone)-x] != "0"):
                    return x
        def find_second_Index():
            for y in range(find_last_Index()+1,11,1):
                if (patient_phone[len(patient_phone)-y] != "0"):
                    return y

        def find_first_Index():
            for z in range(find_second_Index()+1,11,1):
                if (patient_phone[len(patient_phone)-z] != "0"):
                    return z

        lastIndex = patient_phone[len(patient_phone)-find_last_Index()]
        secondIndex = patient_phone[len(patient_phone)-find_second_Index()]
        firstIndex = patient_phone[len(patient_phone)-find_first_Index()]
        


        # assign different diagram with different number in specific index
        def diagnosis_first_index():
            if (firstIndex == "1") or (firstIndex == "9"):
                first_diagnosis = first_diagram_partOne
                return first_diagnosis
            if firstIndex == "2":
                first_diagnosis = second_diagram_partOne
                return first_diagnosis
            if firstIndex == "3":
                first_diagnosis = third_diagram_partOne
                return first_diagnosis
            if firstIndex == "4":
                first_diagnosis = fourth_diagram_partOne
                return first_diagnosis
            if firstIndex == "5":
                first_diagnosis = fifth_diagram_partOne
                return first_diagnosis
            if firstIndex == "6":
                first_diagnosis = sixth_diagram_partOne
                return first_diagnosis
            if firstIndex == "7":
                first_diagnosis = seventh_diagram_partOne
                return first_diagnosis
            if firstIndex == "8":
                first_diagnosis = eighth_diagram_partOne
                return first_diagnosis
        
        
        def diagnosis_second_index(): 
            if (secondIndex == "1") or (secondIndex == "9"):
                second_diagnosis = first_diagram_partTwo
                return second_diagnosis
            if secondIndex == "2":
                second_diagnosis = second_diagram_partTwo
                return second_diagnosis
            if secondIndex == "3":
                second_diagnosis = third_diagram_partTwo
                return second_diagnosis
            if secondIndex == "4":
                second_diagnosis = fourth_diagram_partTwo
                return second_diagnosis
            if secondIndex == "5":
                second_diagnosis = fifth_diagram_partTwo
                return second_diagnosis
            if secondIndex == "6":
                second_diagnosis = sixth_diagram_partTwo
                return second_diagnosis
            if secondIndex == "7":
                second_diagnosis = seventh_diagram_partTwo
                return second_diagnosis
            if secondIndex == "8":
                second_diagnosis = eighth_diagram_partTwo
                return second_diagnosis

        def diagnosis_last_index():
            if (lastIndex <= "3") or (lastIndex >= "7"):
                diagram_to_change = diagnosis_second_index()
                if (lastIndex == "1") or (lastIndex =="7"):
                    sympton_to_change = diagram_to_change.get("urinaryBladder")
                    new_change = (not sympton_to_change)
                    diagram_to_change["urinaryBladder"] = new_change
                    return (diagram_to_change)

                if (lastIndex == "2") or (lastIndex =="8"):
                    sympton_to_change = diagram_to_change.get("gallbladder")
                    new_change = (not sympton_to_change)
                    diagram_to_change["gallbladder"] = new_change
                    return (diagram_to_change)

                if (lastIndex == "3") or (lastIndex =="9"):
                    sympton_to_change = diagram_to_change.get("stomach")
                    new_change = (not sympton_to_change)
                    diagram_to_change["stomach"] = new_change
                    return (diagram_to_change)
            else:
                diagram_to_change = diagnosis_first_index()
                if lastIndex == "4":
                    sympton_to_change = diagram_to_change.get("heart")
                    new_change = (not sympton_to_change)
                    diagram_to_change["heart"] = new_change
                    return (diagram_to_change)

                if lastIndex == "5":
                    sympton_to_change = diagram_to_change.get("pericardium")
                    new_change = (not sympton_to_change)
                    diagram_to_change["pericardium"] = new_change
                    return (diagram_to_change)

                if lastIndex == "6":
                    sympton_to_change = diagram_to_change.get("lung")
                    new_change = (not sympton_to_change)
                    diagram_to_change["lung"] = new_change
                    return (diagram_to_change)
    

        # specify the final diagnosis diagram with different possible result

        if (lastIndex <= "3") or (lastIndex >= "7"):
            # result1 = (json.dumps(diagnosis_first_index())[1:-1]+", "+json.dumps(diagnosis_last_index())[1:-1])
            result1= Merge(diagnosis_first_index(),diagnosis_last_index())
            
        else:
            # result1 = (json.dumps(diagnosis_last_index())[1:-1]+", "+json.dumps(diagnosis_second_index())[1:-1])
            result1= Merge(diagnosis_second_index(),diagnosis_last_index())
            
            
        
        def diagnosis2_first_index():
            if (lastIndex == "1") or (lastIndex == "9"):
                third_diagnosis = first_diagram_partThree
                return third_diagnosis
            if (lastIndex == "2"):
                third_diagnosis = second_diagram_partThree
                return third_diagnosis
            if (lastIndex == "3"):
                third_diagnosis = third_diagram_partThree
                return third_diagnosis
            if (lastIndex == "4"):
                third_diagnosis = fourth_diagram_partThree
                return third_diagnosis
            if (lastIndex == "5"):
                third_diagnosis = fifth_diagram_partThree
                return third_diagnosis
            if (lastIndex == "6"):
                third_diagnosis = sixth_diagram_partThree
                return third_diagnosis
            if (lastIndex == "7"):
                third_diagnosis = seventh_diagram_partThree
                return third_diagnosis
            if (lastIndex == "8"):
                third_diagnosis = eighth_diagram_partThree
                return third_diagnosis

        def diagnosis2_second_index():
            if (secondIndex == "1") or (secondIndex == "9"):
                fourth_diagnosis = first_diagram_partFour
                return fourth_diagnosis
            if secondIndex == "2":
                fourth_diagnosis = second_diagram_partFour
                return fourth_diagnosis
            if secondIndex == "3":
                fourth_diagnosis = third_diagram_partFour
                return fourth_diagnosis
            if secondIndex == "4":
                fourth_diagnosis = fourth_diagram_partFour
                return fourth_diagnosis
            if secondIndex == "5":
                fourth_diagnosis = fifth_diagram_partFour
                return fourth_diagnosis
            if secondIndex == "6":
                fourth_diagnosis = sixth_diagram_partFour
                return fourth_diagnosis
            if secondIndex == "7":
                fourth_diagnosis = seventh_diagram_partFour
                return fourth_diagnosis
            if secondIndex == "8":
                fourth_diagnosis = eighth_diagram_partFour
                return fourth_diagnosis
        
        def diagnosis2_last_index():
            if (firstIndex <= "3") or (firstIndex >= "7"):
                diagram_to_change = diagnosis2_second_index()
                if (firstIndex == "1") or (firstIndex =="7"):
                    sympton_to_change = diagram_to_change.get("small intestine")
                    new_change = (not sympton_to_change)
                    diagram_to_change["small intestine"] = new_change
                    return (diagram_to_change)

                if (firstIndex == "2") or (firstIndex =="8"):
                    sympton_to_change = diagram_to_change.get("san jiao")
                    new_change = (not sympton_to_change)
                    diagram_to_change["san jiao"] = new_change
                    return (diagram_to_change)

                if (firstIndex == "3") or (firstIndex =="9"):
                    sympton_to_change = diagram_to_change.get("large intestine")
                    new_change = (not sympton_to_change)
                    diagram_to_change["large intestine"] = new_change
                    return (diagram_to_change)
            else:
                diagram_to_change = diagnosis2_first_index()
                if firstIndex == "4":
                    sympton_to_change = diagram_to_change.get("kidney")
                    new_change = (not sympton_to_change)
                    diagram_to_change["heart"] = new_change
                    return (diagram_to_change)

                if firstIndex == "5":
                    sympton_to_change = diagram_to_change.get("liver")
                    new_change = (not sympton_to_change)
                    diagram_to_change["liver"] = new_change
                    return (diagram_to_change)

                if firstIndex == "6":
                    sympton_to_change = diagram_to_change.get("spleen")
                    new_change = (not sympton_to_change)
                    diagram_to_change["spleen"] = new_change
                    return (diagram_to_change)

        if (firstIndex <= "3") or (firstIndex >= "7"):
            # result2 = (json.dumps(diagnosis2_first_index())[1:-1]+", "+json.dumps(diagnosis2_last_index())[1:-1])
            result2 = Merge(diagnosis2_first_index(), diagnosis2_last_index())
            

        else:
            # result2 = (json.dumps(diagnosis2_last_index())[1:-1]+", "+json.dumps(diagnosis2_second_index())[1:-1])
            result2 = Merge(diagnosis2_second_index(),diagnosis2_last_index())
        
        # y = np.array([100, 0])
        # colors = ['lime','red']
        # fig1, ax1 = plt.subplots()
        # ax1.pie(y, colors=colors,  shadow=True, startangle=90)
        # ax1.axis('equal') 
        # plt.savefig('media/diagnosis/1000.png',dpi=100)
        # #
        # y = np.array([60,40])
        # colors = ['lime','red']
        # fig1, ax1 = plt.subplots()
        # ax1.pie(y, colors=colors,  shadow=True, startangle=90)
        # ax1.axis('equal') 
        # plt.savefig('media/diagnosis/6040.png',dpi=100)
        # #  
        # y = np.array([40, 60])
        # colors = ['lime','red']
        # fig1, ax1 = plt.subplots()
        # ax1.pie(y, colors=colors,  shadow=True, startangle=90)
        # ax1.axis('equal') 
        # plt.savefig('media/diagnosis/4060.png',dpi=100)
        # # 
        # y = np.array([30, 70])
        # colors = ['lime','red']
        # fig1, ax1 = plt.subplots()
        # ax1.pie(y, colors=colors,  shadow=True, startangle=90)
        # ax1.axis('equal') 
        # plt.savefig('media/diagnosis/3070.png',dpi=100)
        patient_status_dict = Merge(result1, result2)
        form.diagnosisResult = json.dumps(patient_status_dict)
        form.diagnosis = True
        form.save()
        patient_to_view.save()
        return redirect (f"/patient/{form.id}/QA")

def seeResultPage (request, form_id):
   
    if "patient_id" not in request.session:
            return redirect('/not_found')
    else:
        form = PatientForm.objects.get(id=form_id)
        if form.question == False:
            return redirect("/patient/{form.id}/{patient_to_view.id}/QA")
        else:
            diagnosis_patient = Patient.objects.get(id=request.session['patient_id'])
            patient_initial_status_dict = json.loads(form.diagnosisInitial)
            patient_status_dict = json.loads(form.diagnosisResult)
            initialLung = patient_initial_status_dict.get("lung")
            lung = patient_status_dict.get("lung")  
            initialPericardium = patient_initial_status_dict.get("pericardium")
            pericardium = patient_status_dict.get("pericardium")
            initialHeart = patient_initial_status_dict.get("heart")
            heart = patient_status_dict.get("heart")
            initialStomach = patient_initial_status_dict.get("stomach")
            stomach = patient_status_dict.get("stomach")
            initialGallbladder = patient_initial_status_dict.get("gallbladder")
            gallbladder = patient_status_dict.get("gallbladder")
            initialUrinaryBladder = patient_initial_status_dict.get("urinaryBladder")
            urinaryBladder = patient_status_dict.get("urinaryBladder")
            initialSpleen = patient_initial_status_dict.get("spleen")
            spleen = patient_status_dict.get("spleen")
            initialLiver = patient_initial_status_dict.get("liver")
            liver = patient_status_dict.get("liver")
            initialKidney = patient_initial_status_dict.get("kidney")
            kidney = patient_status_dict.get("kidney")
            initialLarge_intestine = patient_initial_status_dict.get("large intestine")
            large_intestine = patient_status_dict.get("large intestine")
            initialSan_jiao = patient_initial_status_dict.get("san jiao")
            san_jiao = patient_status_dict.get("san jiao")
            initialSmall_intestine = patient_initial_status_dict.get("small intestine")
            small_intestine = patient_status_dict.get("small intestine")
            context={
                    "patient": diagnosis_patient,
                    "lung": lung,
                    "initialLung": initialLung,
                    "pericardium": pericardium,
                    "initialPericardium":initialPericardium,
                    "heart": heart,
                    "initialHeart":initialHeart,
                    "stomach": stomach,
                    "initialStomach":initialStomach,
                    "gallbladder": gallbladder,
                    "initialGallbladder":initialGallbladder,
                    "urinaryBladder": urinaryBladder,
                    "initialUrinaryBladder": initialUrinaryBladder,
                    "spleen": spleen,
                    "initialSpleen":initialSpleen,
                    "liver": liver,
                    "initialLiver":initialLiver,
                    "kidney":kidney,
                    "initialKidney":initialKidney,
                    "large_intestine": large_intestine,
                    "initialLarge_intestine":initialLarge_intestine,
                    "san_jiao":san_jiao,
                    "initialSan_jiao":initialSan_jiao,
                    "small_intestine": small_intestine,
                    "initialSmall_intestine":initialSmall_intestine,
                    "patient_status_dict":patient_status_dict,
                    "form":form,
                }
            return render (request, "seeResult.html", context)

def hostCheckResultPage (request, form_id, patient_id):
    if 'auth' not in request.session:
        return redirect("/host")
    else:
            form = PatientForm.objects.get(id=form_id)
            diagnosis_patient = Patient.objects.get(id=patient_id)
            patient_initial_status_dict = json.loads(form.diagnosisInitial)
            patient_status_dict = json.loads(form.diagnosisResult)
            initialLung = patient_initial_status_dict.get("lung")
            lung = patient_status_dict.get("lung")  
            initialPericardium = patient_initial_status_dict.get("pericardium")
            pericardium = patient_status_dict.get("pericardium")
            initialHeart = patient_initial_status_dict.get("heart")
            heart = patient_status_dict.get("heart")
            initialStomach = patient_initial_status_dict.get("stomach")
            stomach = patient_status_dict.get("stomach")
            initialGallbladder = patient_initial_status_dict.get("gallbladder")
            gallbladder = patient_status_dict.get("gallbladder")
            initialUrinaryBladder = patient_initial_status_dict.get("urinaryBladder")
            urinaryBladder = patient_status_dict.get("urinaryBladder")
            initialSpleen = patient_initial_status_dict.get("spleen")
            spleen = patient_status_dict.get("spleen")
            initialLiver = patient_initial_status_dict.get("liver")
            liver = patient_status_dict.get("liver")
            initialKidney = patient_initial_status_dict.get("kidney")
            kidney = patient_status_dict.get("kidney")
            initialLarge_intestine = patient_initial_status_dict.get("large intestine")
            large_intestine = patient_status_dict.get("large intestine")
            initialSan_jiao = patient_initial_status_dict.get("san jiao")
            san_jiao = patient_status_dict.get("san jiao")
            initialSmall_intestine = patient_initial_status_dict.get("small intestine")
            small_intestine = patient_status_dict.get("small intestine")
            context={
                    "patient": diagnosis_patient,
                    "lung": lung,
                    "initialLung": initialLung,
                    "pericardium": pericardium,
                    "initialPericardium":initialPericardium,
                    "heart": heart,
                    "initialHeart":initialHeart,
                    "stomach": stomach,
                    "initialStomach":initialStomach,
                    "gallbladder": gallbladder,
                    "initialGallbladder":initialGallbladder,
                    "urinaryBladder": urinaryBladder,
                    "initialUrinaryBladder": initialUrinaryBladder,
                    "spleen": spleen,
                    "initialSpleen":initialSpleen,
                    "liver": liver,
                    "initialLiver":initialLiver,
                    "kidney":kidney,
                    "initialKidney":initialKidney,
                    "large_intestine": large_intestine,
                    "initialLarge_intestine":initialLarge_intestine,
                    "san_jiao":san_jiao,
                    "initialSan_jiao":initialSan_jiao,
                    "small_intestine": small_intestine,
                    "initialSmall_intestine":initialSmall_intestine,
                    "patient_status_dict":patient_status_dict,
                    "form":form,
                }
            return render (request, "seeResult.html", context)

def viewReport(request, form_id, patient_id):

    form = PatientForm.objects.get(id=form_id)
    diagnosis_patient = Patient.objects.get(id=patient_id)
    patient_initial_status_dict = json.loads(form.diagnosisInitial)
    patient_status_dict = json.loads(form.diagnosisResult)
    initialLung = patient_initial_status_dict.get("lung")
    lung = patient_status_dict.get("lung")  
    initialPericardium = patient_initial_status_dict.get("pericardium")
    pericardium = patient_status_dict.get("pericardium")
    initialHeart = patient_initial_status_dict.get("heart")
    heart = patient_status_dict.get("heart")
    initialStomach = patient_initial_status_dict.get("stomach")
    stomach = patient_status_dict.get("stomach")
    initialGallbladder = patient_initial_status_dict.get("gallbladder")
    gallbladder = patient_status_dict.get("gallbladder")
    initialUrinaryBladder = patient_initial_status_dict.get("urinaryBladder")
    urinaryBladder = patient_status_dict.get("urinaryBladder")
    initialSpleen = patient_initial_status_dict.get("spleen")
    spleen = patient_status_dict.get("spleen")
    initialLiver = patient_initial_status_dict.get("liver")
    liver = patient_status_dict.get("liver")
    initialKidney = patient_initial_status_dict.get("kidney")
    kidney = patient_status_dict.get("kidney")
    initialLarge_intestine = patient_initial_status_dict.get("large intestine")
    large_intestine = patient_status_dict.get("large intestine")
    initialSan_jiao = patient_initial_status_dict.get("san jiao")
    san_jiao = patient_status_dict.get("san jiao")
    initialSmall_intestine = patient_initial_status_dict.get("small intestine")
    small_intestine = patient_status_dict.get("small intestine")
    context={
            "patient": diagnosis_patient,
            "lung": lung,
            "initialLung": initialLung,
            "pericardium": pericardium,
            "initialPericardium":initialPericardium,
            "heart": heart,
            "initialHeart":initialHeart,
            "stomach": stomach,
            "initialStomach":initialStomach,
            "gallbladder": gallbladder,
            "initialGallbladder":initialGallbladder,
            "urinaryBladder": urinaryBladder,
            "initialUrinaryBladder": initialUrinaryBladder,
            "spleen": spleen,
            "initialSpleen":initialSpleen,
            "liver": liver,
            "initialLiver":initialLiver,
            "kidney":kidney,
            "initialKidney":initialKidney,
            "large_intestine": large_intestine,
            "initialLarge_intestine":initialLarge_intestine,
            "san_jiao":san_jiao,
            "initialSan_jiao":initialSan_jiao,
            "small_intestine": small_intestine,
            "initialSmall_intestine":initialSmall_intestine,
            "patient_status_dict":patient_status_dict,
            "form":form,
        }
    return render (request, "phoneReport.html", context)

def seeIndexResultPage (request, form_id):
    diagnosis_patient = Patient.objects.get(id=request.session['patient_id'])
    form = PatientForm.objects.get(id=form_id)
    patient_initial_status_dict = json.loads(form.diagnosisInitial)
    patient_status_dict = json.loads(form.diagnosisResult)

    initialLung = patient_initial_status_dict.get("lung")
    lung = patient_status_dict.get("lung")
    
    initialPericardium = patient_initial_status_dict.get("pericardium")
    pericardium = patient_status_dict.get("pericardium")
    
    initialHeart = patient_initial_status_dict.get("heart")
    heart = patient_status_dict.get("heart")
    
    initialStomach = patient_initial_status_dict.get("stomach")
    stomach = patient_status_dict.get("stomach")
    
    initialGallbladder = patient_initial_status_dict.get("gallbladder")
    gallbladder = patient_status_dict.get("gallbladder")
    
    initialUrinaryBladder = patient_initial_status_dict.get("urinaryBladder")
    urinaryBladder = patient_status_dict.get("urinaryBladder")
    
    initialSpleen = patient_initial_status_dict.get("spleen")
    spleen = patient_status_dict.get("spleen")
    
    initialLiver = patient_initial_status_dict.get("liver")
    liver = patient_status_dict.get("liver")
    
    initialKidney = patient_initial_status_dict.get("kidney")
    kidney = patient_status_dict.get("kidney")
    
    initialLarge_intestine = patient_initial_status_dict.get("large intestine")
    large_intestine = patient_status_dict.get("large intestine")
    
    initialSan_jiao = patient_initial_status_dict.get("san jiao")
    san_jiao = patient_status_dict.get("san jiao")
    
    initialSmall_intestine = patient_initial_status_dict.get("small intestine")
    small_intestine = patient_status_dict.get("small intestine")

    context={
            "patient": diagnosis_patient,
            "lung": lung,
            "initialLung": initialLung,
            "pericardium": pericardium,
            "initialPericardium":initialPericardium,
            "heart": heart,
            "initialHeart":initialHeart,
            "stomach": stomach,
            "initialStomach":initialStomach,
            "gallbladder": gallbladder,
            "initialGallbladder":initialGallbladder,
            "urinaryBladder": urinaryBladder,
            "initialUrinaryBladder": initialUrinaryBladder,
            "spleen": spleen,
            "initialSpleen":initialSpleen,
            "liver": liver,
            "initialLiver":initialLiver,
            "kidney":kidney,
            "initialKidney":initialKidney,
            "large_intestine": large_intestine,
            "initialLarge_intestine":initialLarge_intestine,
            "san_jiao":san_jiao,
            "initialSan_jiao":initialSan_jiao,
            "small_intestine": small_intestine,
            "initialSmall_intestine":initialSmall_intestine,
            "patient_status_dict":patient_status_dict,
            "form":form,
            "today_date":datetime.date.today().strftime("%b/%d/%y"),
            
        }
    return render (request, "patientQuestion.html", context)

def question_complete(request, form_id):
    if "patient_id" not in request.session:
            return redirect('/not_found')
    else:
        if request.method == 'POST':
            diagnosis_patient = Patient.objects.get(id=request.session['patient_id'])
            form = PatientForm.objects.get(id=form_id)
            form.question = True
            patient_initial_status_dict = json.loads(form.diagnosisInitial)
            patient_status_dict = json.loads(form.diagnosisResult)
            # check lung status
            initialLung = patient_initial_status_dict.get("lung")
            lung = patient_status_dict.get("lung")
            if lung == initialLung:
                if lung == False:
                    form.lungResult = request.POST['lungQA1'] + request.POST['lungQA2'] + request.POST['lungQA3'] + request.POST['lungQA4']
                else:
                    form.lungResult = request.POST['lungQA1'] + request.POST['lungQA2'] + request.POST['lungQA3'] + request.POST['lungQA4'] + request.POST['lungQA5'] + request.POST['lungQA6'] + request.POST['lungQA7']
            if lung != initialLung:
                if lung == False:
                    form.lungResult = request.POST['lungQA1'] + request.POST['lungQA2'] + request.POST['lungQA3']
                else: 
                    form.lungResult = request.POST['lungQA1'] + request.POST['lungQA2'] + request.POST['lungQA3'] + request.POST['lungQA4'] + request.POST['lungQA5'] + request.POST['lungQA6']
            
            # check pericardium status
            initialPericardium = patient_initial_status_dict.get("pericardium")
            pericardium = patient_status_dict.get("pericardium")
            if pericardium == initialPericardium:
                if pericardium == False:
                    if diagnosis_patient.sex == 'Female':
                        form.pericardiumResult = request.POST['pericardiumQA1']+request.POST['pericardiumQA2']+request.POST['pericardiumQA3']
                    else:
                        form.pericardiumResult = request.POST['pericardiumQA1']+request.POST['pericardiumQA2']
                else:
                    if diagnosis_patient.sex == 'Female':
                        form.pericardiumResult = request.POST['pericardiumQA1'] + request.POST['pericardiumQA2'] + request.POST['pericardiumQA3'] + request.POST['pericardiumQA4'] + request.POST['pericardiumQA5'] + request.POST['pericardiumQA6'] + request.POST['pericardiumQA7']
                    else:
                        form.pericardiumResult = request.POST['pericardiumQA1'] + request.POST['pericardiumQA2'] + request.POST['pericardiumQA3'] + request.POST['pericardiumQA4'] + request.POST['pericardiumQA5'] + request.POST['pericardiumQA6']
            if pericardium != initialPericardium:
                if pericardium == False:
                    if diagnosis_patient.sex == 'Female':
                        form.pericardiumResult = request.POST['pericardiumQA1'] + request.POST['pericardiumQA2']
                    else:
                        form.pericardiumResult = request.POST['pericardiumQA1']
                else:
                    if diagnosis_patient.sex == 'Female':
                        form.pericardiumResult = request.POST['pericardiumQA1'] + request.POST['pericardiumQA2'] + request.POST['pericardiumQA3'] + request.POST['pericardiumQA4'] + request.POST['pericardiumQA5']
                    else:
                        form.pericardiumResult = request.POST['pericardiumQA1'] + request.POST['pericardiumQA2'] + request.POST['pericardiumQA3'] + request.POST['pericardiumQA4']
            
            # check heart status
            initialHeart = patient_initial_status_dict.get("heart")
            heart = patient_status_dict.get("heart")
            if heart == initialHeart:
                if heart == False:
                    form.heartResult = request.POST['heartQA1']
                else:
                    form.heartResult = request.POST['heartQA1'] + request.POST['heartQA2'] + request.POST['heartQA3'] + request.POST['heartQA4']
            if heart != initialHeart:
                if heart == False:
                    form.heartResult = request.POST['heartQA1']
                else:
                    form.heartResult = request.POST['heartQA1'] + request.POST['heartQA2']

            # check stomach status
            initialStomach = patient_initial_status_dict.get("stomach")
            stomach = patient_status_dict.get("stomach")
            if stomach == initialStomach:
                if stomach == False:
                    form.stomachResult = request.POST['stomachQA1']
                else: 
                    form.stomachResult = request.POST['stomachQA1'] + request.POST['stomachQA2'] + request.POST['stomachQA3']
            if stomach != initialStomach:
                if stomach == False:
                    form.stomachResult = request.POST['stomachQA1'] + request.POST['stomachQA2'] + request.POST['stomachQA3']
                else: 
                    form.stomachResult = request.POST['stomachQA1'] + request.POST['stomachQA2'] + request.POST['stomachQA3'] + request.POST['stomachQA4']
            
            # check gallbladder status 
            initialGallbladder = patient_initial_status_dict.get("gallbladder")
            gallbladder = patient_status_dict.get("gallbladder")
            if gallbladder == initialGallbladder:
                if gallbladder == False:
                    form.gallbladderResult = request.POST['gallbladderQA1']
                else: 
                    form.gallbladderResult = request.POST['gallbladderQA1'] + request.POST['gallbladderQA2'] + request.POST['gallbladderQA3'] + request.POST['gallbladderQA4']
            if gallbladder != initialGallbladder:
                if gallbladder == False:
                    form.gallbladderResult = request.POST['gallbladderQA1']
                else: 
                    form.gallbladderResult = request.POST['gallbladderQA1'] + request.POST['gallbladderQA2']
            
            # check urinary status
            initialUrinaryBladder = patient_initial_status_dict.get("urinaryBladder")
            urinaryBladder = patient_status_dict.get("urinaryBladder")
            if urinaryBladder == initialUrinaryBladder:
                if urinaryBladder == False: 
                    if diagnosis_patient.sex == 'Male':
                        form.urinaryBladderResult = request.POST['urinaryQA1'] + request.POST['urinaryQA2']
                    else:
                        form.urinaryBladderResult = request.POST['urinaryQA1']
                else: 
                    if diagnosis_patient.sex == 'Male':
                        form.urinaryBladderResult = request.POST['urinaryQA1'] + request.POST['urinaryQA2'] + request.POST['urinaryQA3']
                    else:
                        form.urinaryBladderResult = request.POST['urinaryQA1'] + request.POST['urinaryQA2'] + request.POST['urinaryQA3'] + request.POST['urinaryQA4'] + request.POST['urinaryQA5'] + request.POST['urinaryQA6']
            if urinaryBladder != initialUrinaryBladder:
                if urinaryBladder == False:
                    if diagnosis_patient.sex == 'Male':
                        form.urinaryBladderResult = request.POST['urinaryQA1'] + request.POST['urinaryQA2'] 
                    else:
                        form.urinaryBladderResult = request.POST['urinaryQA1']
                else:
                    if diagnosis_patient.sex == 'Male':
                        form.urinaryBladderResult = request.POST['urinaryQA1'] + request.POST['urinaryQA2']+ request.POST['urinaryQA3']
                    else:
                        form.urinaryBladderResult = request.POST['urinaryQA1']
            
            # check spleen status
            initialSpleen = patient_initial_status_dict.get("spleen")
            spleen = patient_status_dict.get("spleen")
            if spleen == initialSpleen:
                if spleen == False:
                    form.spleenResult = request.POST['spleenQA1']
                else: 
                    form.spleenResult = request.POST['spleenQA1'] + request.POST['spleenQA2'] + request.POST['spleenQA3']
            if spleen != initialSpleen:
                if spleen == False:
                    form.spleenResult = request.POST['spleenQA1'] + request.POST['spleenQA2'] + request.POST['spleenQA3'] + request.POST['spleenQA4'] + request.POST['spleenQA5']
                else: 
                    form.spleenResult = request.POST['spleenQA1'] + request.POST['spleenQA2'] + request.POST['spleenQA3'] + request.POST['spleenQA4']
            
            # check liver status
            initialLiver = patient_initial_status_dict.get("liver")
            liver = patient_status_dict.get("liver")
            if liver == initialLiver:
                if liver == False:
                    form.liverResult = request.POST['liverQA1'] + request.POST['liverQA2'] + request.POST['liverQA3'] + request.POST['liverQA4']
                else:
                    form.liverResult = request.POST['liverQA1'] + request.POST['liverQA2'] + request.POST['liverQA3'] + request.POST['liverQA4'] + request.POST['liverQA5'] + request.POST['liverQA6']
            if liver != initialLiver:
                if liver == False:
                    form.liverResult = request.POST['liverQA1'] + request.POST['liverQA2'] + request.POST['liverQA3'] + request.POST['liverQA4'] + request.POST['liverQA5'] + request.POST['liverQA6'] + request.POST['liverQA7']
                else: 
                    form.liverResult = request.POST['liverQA1'] + request.POST['liverQA2'] + request.POST['liverQA3'] + request.POST['liverQA4'] + request.POST['liverQA5'] + request.POST['liverQA6']
            
            # check kidney status
            initialKidney = patient_initial_status_dict.get("kidney")
            kidney = patient_status_dict.get("kidney")
            if kidney == initialKidney:
                if kidney == False:
                    form.kidneyResult = request.POST['kidneyQA1'] + request.POST['kidneyQA2'] + request.POST['kidneyQA3'] + request.POST['kidneyQA4']
                else:
                    form.kidneyResult = request.POST['kidneyQA1'] + request.POST['kidneyQA2'] + request.POST['kidneyQA3'] + request.POST['kidneyQA4'] + request.POST['kidneyQA5'] + request.POST['kidneyQA6'] + request.POST['kidneyQA7']
            if kidney != initialKidney:
                if kidney == False:
                    form.kidneyResult = request.POST['kidneyQA1'] + request.POST['kidneyQA2'] + request.POST['kidneyQA3'] + request.POST['kidneyQA4']
                else:
                    form.kidneyResult = request.POST['kidneyQA1'] + request.POST['kidneyQA2'] + request.POST['kidneyQA3']
            
            # check Large Intestine status
            initialLarge_intestine = patient_initial_status_dict.get("large intestine")
            large_intestine = patient_status_dict.get("large intestine")
            if large_intestine == initialLarge_intestine:
                if large_intestine == False:
                    form.large_intestineResult = request.POST['largeInQA1'] + request.POST['largeInQA2'] + request.POST['largeInQA3']
                else:
                    form.large_intestineResult = request.POST['largeInQA1'] + request.POST['largeInQA2'] + request.POST['largeInQA3'] + request.POST['largeInQA4'] + request.POST['largeInQA5'] + request.POST['largeInQA6']
            if large_intestine != initialLarge_intestine:
                if large_intestine == False:
                    form.large_intestineResult = request.POST['largeInQA1'] + request.POST['largeInQA2'] + request.POST['largeInQA3']
                else:
                    form.large_intestineResult = request.POST['largeInQA1'] + request.POST['largeInQA2'] + request.POST['largeInQA3'] 
            
            # check San Jiao status
            initialSan_jiao = patient_initial_status_dict.get("san jiao")
            san_jiao = patient_status_dict.get("san jiao")
            if initialSan_jiao == san_jiao:
                if san_jiao == False:
                    form.san_jiaoResult = request.POST['sanJQA1'] + request.POST['sanJQA2'] + request.POST['sanJQA3']
                else:
                    if diagnosis_patient.sex == 'Female':
                        form.san_jiaoResult = request.POST['sanJQA1'] + request.POST['sanJQA2'] + request.POST['sanJQA3'] + request.POST['sanJQA4'] + request.POST['sanJQA5'] + request.POST['sanJQA6'] + request.POST['sanJQA7']
                    else: 
                        form.san_jiaoResult = request.POST['sanJQA1'] + request.POST['sanJQA2'] + request.POST['sanJQA3']
            if initialSan_jiao != san_jiao:
                if san_jiao == False:
                    if diagnosis_patient.sex == 'Female':
                        form.san_jiaoResult = request.POST['sanJQA1'] + request.POST['sanJQA2']
                    else:
                        form.san_jiaoResult = request.POST['sanJQA1']
                else:
                    if diagnosis_patient.sex == 'Female':
                        form.san_jiaoResult = request.POST['sanJQA1'] + request.POST['sanJQA2'] + request.POST['sanJQA3'] + request.POST['sanJQA4'] 
                    else: 
                        form.san_jiaoResult = request.POST['sanJQA1'] + request.POST['sanJQA2'] 
            
            # check Small Intestine status
            initialSmall_intestine = patient_initial_status_dict.get("small intestine")
            small_intestine = patient_status_dict.get("small intestine")
            if initialSmall_intestine == small_intestine:
                if small_intestine == False:
                    form.small_intestineResult = request.POST['smallInQA1'] + request.POST['smallInQA2'] + request.POST['smallInQA3'] + request.POST['smallInQA4'] + request.POST['smallInQA5'] + request.POST['smallInQA6']
                else:
                    form.small_intestineResult = request.POST['smallInQA1'] + request.POST['smallInQA2'] + request.POST['smallInQA3'] + request.POST['smallInQA4'] + request.POST['smallInQA5']
            if initialSmall_intestine != small_intestine:
                if small_intestine == False:
                    form.small_intestineResult = request.POST['smallInQA1'] + request.POST['smallInQA2'] + request.POST['smallInQA3'] + request.POST['smallInQA4'] + request.POST['smallInQA5']
                else:
                    form.small_intestineResult = request.POST['smallInQA1'] + request.POST['smallInQA2'] + request.POST['smallInQA3'] + request.POST['smallInQA4'] + request.POST['smallInQA5']
            
            form.save()
            return redirect (f"/patient/{form.id}/seeResult/page")
        else:
            return redirect('/not_found')

def resetPassword (request):
    return render (request, 'resetPassword.html')

def verifyEmail (request):
    if request.method == 'POST':
        check_patient = Patient.objects.filter(email=request.POST['email'])
        if check_patient.count()!=1 :
            messages.error(request, "No Patient Found")
            return redirect("/resetPassword")
        else:
            patient = check_patient[0]
            request.session['patient_id'] = patient.id
            return render (request, 'reset.html')
    else:
        if request.session['patient_id']:
            return render (request, 'reset.html')
        else:
            return redirect('/not_found')


def resetPatientPassword(request):
    patient = Patient.objects.get(id=request.session['patient_id'])
    if request.method == 'POST':
        errors = Patient.objects.password_change(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ('/reset/email')
        else:
            newpassword = bcrypt.hashpw(request.POST['newPassword'].encode(), bcrypt.gensalt()).decode()
            patient.password = newpassword
            patient.save()
            request.session.flush()
            return redirect ('/loginE')

def logout (request):
    request.session.flush()
    return redirect('/')