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
    return render(request, "index.html")

def login(request):
    if request.method == 'POST':   
        caseNumber = request.POST['caseNumber']
        if not caseNumber:
            return render (request, "404.html")
        else:
            return redirect (f'/login/{caseNumber}')
    return render(request, "index.html")

def searchCase(request, case_number):
    patient = Patient.objects.filter(caseNumber = case_number)
    patient_to_view = patient[0]
    if not patient:
        return render (request, "404.html")
    else:
        return redirect(f"/submit/success/{patient_to_view.id}")

def showform1(request):
    currentdate = datetime.date.today().strftime("%d/%b/%y")
    
    context = {
        "today_date":currentdate,
        "default_date": datetime.date.today().strftime("%y-%d-%b"),
    }
    return render(request, "form1.html", context)

def showform2(request, patient_id):
    currentdate = datetime.date.today().strftime("%d/%b/%y")
    new_patient = Patient.objects.get(id=patient_id)
    context = {
        "today_date":currentdate,
        "default_date": datetime.date.today().strftime("%y-%d-%b"),
        "patient":new_patient
    }
    return render(request, "form2.html", context)

def showform3(request, patient_id):
    currentdate = datetime.date.today().strftime("%d/%b/%y")
    new_patient = Patient.objects.get(id=patient_id)
    context = {
        "today_date":currentdate,
        "default_date": datetime.date.today().strftime("%y-%d-%b"),
        "patient":new_patient
    }
    return render(request, "form3.html", context)

def random_string():
    return str(random.randint(10000, 99999))

def newPatient(request):
    if request.method == 'POST':
        errors = Patient.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/register')
        else:
            
            new_patient = Patient.objects.create(
                firstName = request.POST['firstName'],
                lastName = request.POST['lastName'],
                caseNumber = random_string(),
                phone_number = request.POST['phone'],
                email = request.POST['email'],
                sex = request.POST['sex'],
                date_of_birth = request.POST['date_of_birth'],
            )
            
            return redirect(f"/register/{new_patient.id}")
    return redirect("/register")

def newPatient_sympton(request, patient_id):
    new_patient = Patient.objects.get(id=patient_id)
    if request.method == 'GET':
        return redirect(f"/register/{new_patient.id}") 
    if request.method == 'POST':
        new_patient.sympton = request.POST['sympton']
        new_patient.sweat = request.POST['sweat'] 
        new_patient.sweatOther = request.POST['sweatOther']
        new_patient.appetite = request.POST['appetite']
        new_patient.appetiteOther = request.POST['appetiteOther']
        new_patient.sleep = request.POST['sleep']
        new_patient.sleepOther = request.POST['sleepOther']
        new_patient.tinnitus = request.POST['tinnitus']
        new_patient.tinnitusOther = request.POST['tinnitusOther']
        new_patient.mouth = request.POST['mouth']
        new_patient.mouthOther = request.POST['mouthOther']
        new_patient.digestion = request.POST['digestion']
        new_patient.digestionOther = request.POST['digestionOther']
        new_patient.stool = request.POST['stool']
        new_patient.stoolOther = request.POST['stoolOther']
        new_patient.eyes = request.POST['eyes']
        new_patient.eyesOther = request.POST['eyesOther']
        new_patient.teeth = request.POST['teeth']
        new_patient.teethOther = request.POST['teethOther']
        new_patient.sexualActivities = request.POST['sexualActivities']
        new_patient.sexualActivitiesOther = request.POST['sexualActivitiesOther']
        new_patient.swelling = request.POST['swelling']
        new_patient.swellingOther = request.POST['swellingOther']
        new_patient.thirst = request.POST['thirst']
        new_patient.thirstOther = request.POST['thirstOther']
        new_patient.urine = request.POST['urine']
        new_patient.urineOther = request.POST['urineOther']
        new_patient.nose = request.POST['nose']
        new_patient.noseOther = request.POST['noseOther']
        new_patient.throat = request.POST['throat']
        new_patient.throatOther = request.POST['throatOther']
        new_patient.allergies = request.POST['allergies']
        new_patient.save()
        return redirect(f"/register/{new_patient.id}/img")

def uploadTongue(request, patient_id):
    new_patient = Patient.objects.get(id=patient_id)
    if request.method == 'GET':
        return redirect (f"/register/{new_patient.id}/img")
    if request.method == 'POST':
        new_patient.tongueCoat = request.FILES.get("uploadImg")
        new_patient.save()
        return redirect (f"/register/{new_patient.id}/img")

def uploadLeftEye(request, patient_id):
    new_patient = Patient.objects.get(id=patient_id)
    if request.method == 'GET':
        return redirect (f"/register/{new_patient.id}/img")
    if request.method == 'POST':
        new_patient.leftEye = request.FILES.get("uploadImg")
        new_patient.save()
        return redirect (f"/register/{new_patient.id}/img")

def uploadRightEye(request, patient_id):
    new_patient = Patient.objects.get(id=patient_id)
    if request.method == 'GET':
        return redirect (f"/register/{new_patient.id}/img")
    if request.method == 'POST':
        new_patient.rightEye = request.FILES.get("uploadImg")
        new_patient.save()
        return redirect (f"/register/{new_patient.id}/img")

def uploadFace(request, patient_id):
    new_patient = Patient.objects.get(id=patient_id)
    if request.method == 'GET':
        return redirect (f"/register/{new_patient.id}/img")
    if request.method == 'POST':
        new_patient.face = request.FILES.get("uploadImg")
        new_patient.save()
        return redirect (f"/register/{new_patient.id}/img")

def uploadFiles(request, patient_id):
    new_patient = Patient.objects.get(id=patient_id)
    if request.method == 'GET':
        return redirect (f"/register/{new_patient.id}/img")
    if request.method == 'POST':
        patientUploadFile = request.FILES.getlist("medicalRecord")
        for oneFile in patientUploadFile:
            PatientFiles.objects.create(
                file = oneFile,
                patient = new_patient
                )
        new_patient.save()
        return redirect (f"/register/{new_patient.id}/img")

def agreemenetCheck (request, patient_id):
    new_patient = Patient.objects.get(id=patient_id)
    if request.method == 'GET':
        return render (request, "404.html")
    if request.method == 'POST':
        new_patient.agreementCheck = True
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
        new_patient.diagnosisInitial = json.dumps(initial_statement)
        new_patient.save()
        return redirect (f"/submit/success/{new_patient.id}")

def submit_success(request, patient_id):
    context={
        "patient": Patient.objects.get(id=patient_id)
    }
    return render(request, "success.html", context)

def formSubmit(request, patient_id):
    context={
        "patient": Patient.objects.get(id=patient_id)
    }
    return render(request, "success.html", context)

def host_portal_newest(request):
    context={
        "all_patients": Patient.objects.all(),
        "no_diagnosis_patients": Patient.objects.exclude(diagnosis='True')
    }
    return render(request, "host.html", context)

def host_portal_oldest(request):
    context={
        "all_patients": Patient.objects.order_by("-created_at"),
        "no_diagnosis_patients": Patient.objects.exclude(diagnosis='True')
    }
    return render(request, "host.html", context)

def host_portal_sortby_caseNumber_ascending(request):
    context={
        "all_patients": Patient.objects.order_by("caseNumber"),
        "no_diagnosis_patients": Patient.objects.exclude(diagnosis='True')
    }
    return render(request, "host.html", context)

def host_portal_sortby_caseNumber_descending(request):
    context={
        "all_patients": Patient.objects.order_by("-caseNumber"),
        "no_diagnosis_patients": Patient.objects.exclude(diagnosis='True')
    }
    return render(request, "host.html", context)

def verify_patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    patient.verifyStatus = True
    patient.save()
    return redirect(f"/host")

def verifyDetail_patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    status_to_change = patient.verifyStatus
    patient.verifyStatus = not status_to_change
    patient.save()
    return redirect(f"/patient/{patient.id}/detial")

def delete_patient(request, patient_id):
    patient_to_delete = Patient.objects.get(id=patient_id)
    patient_to_delete.delete()
    return redirect ("/host") 

def Merge(dict1, dict2):
    d = dict1.copy()
    d.update(dict2)
    return d  

def diagnosis(request, patient_id):
    patient_to_view = Patient.objects.get(id=patient_id)
    context = {
        "patient": patient_to_view,
    }
    return render (request, "patient.html", context)


def seeResult(request, patient_id):
    patient_to_view = Patient.objects.get(id=patient_id)
    patient_phone = patient_to_view.phone_number
    if request.method == 'GET':
        context={
            "patient": patient_to_view,
            "final_diagnosis": patient_to_view.diagnosisResult
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
            
        patient_status_dict = Merge(result1, result2)
        patient_to_view.diagnosisResult = json.dumps(patient_status_dict)
        patient_to_view.diagnosis = True
        patient_to_view.save()
        return redirect (f"/patient/{patient_to_view.id}/seeResult/page")

def seeResultPage (request, patient_id):
    diagnosis_patient = Patient.objects.get(id=patient_id)
    # patient_phone = diagnosis_patient.phone_number
    # def find_last_Index():
    #     for x in range(1,11,1):
    #         if (patient_phone[len(patient_phone)-x] != "0"):
    #             return x
    # def find_second_Index():
    #     for y in range(find_last_Index()+1,11,1):
    #         if (patient_phone[len(patient_phone)-y] != "0"):
    #             return y
    # def find_first_Index():
    #     for z in range(find_second_Index()+1,11,1):
    #         if (patient_phone[len(patient_phone)-z] != "0"):
    #             return z

    # lastIndex = patient_phone[len(patient_phone)-find_last_Index()]
    # secondIndex = patient_phone[len(patient_phone)-find_second_Index()]
    # firstIndex = patient_phone[len(patient_phone)-find_first_Index()]

    # labels = 'Health', 'Sick'
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

    patient_initial_status_dict = json.loads(diagnosis_patient.diagnosisInitial)
    patient_status_dict = json.loads(diagnosis_patient.diagnosisResult)
    # common_pairs = dict()
    # def findDifference(dictionary1, dictionary2):
    #     for key in dictionary1:
    #         if (key in dictionary2 and dictionary1[key] != dictionary2[key]):
    #             common_pairs[key] = dictionary1[key]
        
    #     return common_pairs
    # difference = json.dumps(findDifference(patient_initial_status_dict,patient_status_dict))
    
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
            
        }
    return render (request, "seeResult.html", context)