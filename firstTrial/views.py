from distutils.log import error
from email import message
from errno import ESTALE
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



def index(request):
    if "patient_id" not in request.session:
        return render (request, "index.html")
    else:
        login_id = request.session['patient_id']
        patient = Patient.objects.get(id=login_id)
        context={
            "patient": patient,
        } 
        return render(request, "index.html", context)

def not_found (request):
    return render (request, '404.html')


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
        return redirect(f'/dashboard')

def login_By_P(request):
    errors = Patient.objects.login_validator_byPhone(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/loginP')
    else:
        user = Patient.objects.filter(phone_number=request.POST['phone'])
        patient = user[0]
        request.session['patient_id'] = patient.id
        return redirect(f'/dashboard')


def view_dashboard(request):
    if "patient_id" not in request.session:
        return redirect('/')
    else:
        login_id = request.session['patient_id']
        patient = Patient.objects.get(id=login_id)
        context={
            "patient": patient,
            "patient_all_forms": PatientForm.objects.filter(patient=patient),
        }
        return render (request, "dashboard.html", context)


# def patientLogin(request):
#     if request.method == 'POST':   
#         caseNumber = request.POST['caseNumber']
#         if not caseNumber:
#             return redirect("/not_found")
#         else:
#             return redirect (f'/login/{caseNumber}')
#     return render(request, "index.html")

# def searchCase(request, case_number):
#     patient = Patient.objects.filter(caseNumber = case_number)
#     patient_to_view = patient[0]
#     if not patient:
#         return render (request, "404.html")
#     else:
#         return redirect(f"/submit/success/{patient_to_view.id}")

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
        # return render(request, "newPatientForm.html", context)
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
    if request.method == 'GET':
        return redirect("/not_found") 
    if request.method == 'POST':
        new_patient = Patient.objects.get(id=request.session['patient_id'])
        currentdate = datetime.date.today().strftime("%d/%b/%y")
        def random_string():
                return str(random.randint(10000, 99999))
        new_form = PatientForm.objects.create(
            caseNumber = random_string(),
            # sympton = request.POST['sympton'],
            # sweat = request.POST['sweat'],
            # sweatOther = request.POST['sweatOther'],
            # appetite = request.POST['appetite'],
            # appetiteOther = request.POST['appetiteOther'],
            # sleep = request.POST['sleep'],
            # sleepOther = request.POST['sleepOther'],
            # tinnitus = request.POST['tinnitus'],
            # tinnitusOther = request.POST['tinnitusOther'],
            # mouth = request.POST['mouth'],
            # mouthOther = request.POST['mouthOther'],
            # digestion = request.POST['digestion'],
            # digestionOther = request.POST['digestionOther'],
            # stool = request.POST['stool'],
            # stoolOther = request.POST['stoolOther'],
            # eyes = request.POST['eyes'],
            # eyesOther = request.POST['eyesOther'],
            # teeth = request.POST['teeth'],
            # teethOther = request.POST['teethOther'],
            # sexualActivities = request.POST['sexualActivities'],
            # sexualActivitiesOther = request.POST['sexualActivitiesOther'],
            # swelling = request.POST['swelling'],
            # swellingOther = request.POST['swellingOther'],
            # thirst = request.POST['thirst'],
            # thirstOther = request.POST['thirstOther'],
            # urine = request.POST['urine'],
            # urineOther = request.POST['urineOther'],
            # nose = request.POST['nose'],
            # noseOther = request.POST['noseOther'],
            # throat = request.POST['throat'],
            # throatOther = request.POST['throatOther'],
            # allergies = request.POST['allergies'],
            patient = new_patient
        )
        return redirect (f"/newform/{new_form.id}/new")

def uploadTongue(request, form_id):
    if "patient_id" not in request.session:
        return redirect('/not_found')
    else:
        form = PatientForm.objects.get(id=form_id)
        if request.method == 'POST':
            form.tongueCoat = request.FILES.get("uploadImg")
            form.save()
            return redirect (f"/newform/{form.id}/new")
        else:
            return redirect("/not_found")

def uploadLeftEye(request, form_id):
    if "patient_id" not in request.session:
        return redirect('/not_found')
    else:
        form = PatientForm.objects.get(id=form_id)
        if request.method == 'POST':
            form.leftEye = request.FILES.get("uploadImg")
            form.save()
            return redirect (f"/newform/{form.id}/new")
        else:
            return redirect("/not_found")

def uploadRightEye(request, form_id):
    if "patient_id" not in request.session:
        return redirect('/not_found')
    else:
        form = PatientForm.objects.get(id=form_id)
        if request.method == 'POST':
            form.rightEye = request.FILES.get("uploadImg")
            form.save()
            return redirect (f"/newform/{form.id}/new")
        else:
            return redirect("/not_found")

def uploadFace(request, form_id):
    if "patient_id" not in request.session:
        return redirect('/not_found')
    else:
        form = PatientForm.objects.get(id=form_id)
        if request.method == 'POST':
            form.face = request.FILES.get("uploadImg")
            form.save()
            return redirect (f"/newform/{form.id}/new")
        else:
            return redirect("/not_found")

def uploadFiles(request, form_id):
    if "patient_id" not in request.session:
        return redirect('/not_found')
    else:
        patient = Patient.objects.get(id=request.session['patient_id'])
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

def agreementDisable (request, form_id, patient_id):
    new_patient = Patient.objects.get(id=patient_id)
    form = PatientForm.objects.get(id=form_id)
    form.agreementCheck = False
    form.save()
    return redirect (f"/patient/{new_patient.id}/detial")


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
            "form": PatientForm.objects.get(id=form_id)
        }
        return render(request, "success.html", context)

def check_form(request, form_id):
    if "patient_id" not in request.session:
        return redirect('/not_found')
    else:
        form = PatientForm.objects.get(id=form_id)
        if form.agreementCheck == False:
            return redirect (f"/submit/success/{form.id}")
        if form.question == False:
            return (f"/patient/{form.id}/QA")
        else:
            return redirect (f"/patient/{form.id}/seeResult/page")

# def formSubmit(request, patient_id):
#     context={
#         "patient": Patient.objects.get(id=patient_id)
#     }
#     return render(request, "success.html", context)

def host_portal_newest(request):
    context={
        "all_patients": Patient.objects.all(),
        # "no_diagnosis_patients": Patient.objects.exclude(diagnosis='True')
    }
    return render(request, "host.html", context)

def host_portal_oldest(request):
    context={
        "all_patients": Patient.objects.order_by("-created_at"),
        
    }
    return render(request, "host.html", context)

def host_portal_sortby_caseNumber_ascending(request):
    context={
        "all_patients": Patient.objects.order_by("caseNumber"),
        
    }
    return render(request, "host.html", context)

def host_portal_sortby_caseNumber_descending(request):
    context={
        "all_patients": Patient.objects.order_by("-caseNumber"),
    }
    return render(request, "host.html", context)


def delete_patient(request, patient_id):
    patient_to_delete = Patient.objects.get(id=patient_id)
    patient_to_delete.delete()
    return redirect ("/host") 

def Merge(dict1, dict2):
    d = dict1.copy()
    d.update(dict2)
    return d  

def view_patient_detail(request, patient_id):
    patient_to_view = Patient.objects.get(id=patient_id)
    context = {
        "patient": patient_to_view,
        "patient_all_forms": PatientForm.objects.filter(patient=patient_to_view),
    }
    return render (request, "patient.html", context)


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
            "form":form
        }
    return render (request, "patientQuestion.html", context)

def question_complete(request, form_id):
    if "patient_id" not in request.session:
            return redirect('/not_found')
    else:
        patient = Patient.objects.get(id=request.session['patient_id'])
        form = PatientForm.objects.get(id=form_id)
        form.question = True
        form.save()
        return redirect (f"/patient/{form.id}/seeResult/page")

def logout (request):
    request.session.flush()
    return redirect('/')