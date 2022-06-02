from asyncio.windows_events import NULL
from django.db import models
import re


def upload_location(patient,filename):
    return 'patinets/patient_{0}/{1}'.format(patient.id, filename)

def user_directory_path(instance, filename):
    return 'patinets/patient_{0}/{1}'.format(instance.patient.id, filename)

class PatientManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        PHONE_REGEX = re.compile(r'^\+?1?\d{9,15}$')
        if len(postData['firstName']) < 1:
            errors["firstName"] = "FIrst Name must be entered"
        if len(postData['lastName']) < 1:
            errors["lastName"] = "Last Name must be entered"
        if not EMAIL_REGEX.match(postData['email']): 
            errors['email'] = ("Please enter a valid Email")
        if not PHONE_REGEX.match(postData['phone']):
            errors['phone'] = ("Please enter a valid Phone Number")
        if len(postData['sex']) == NULL:
            errors["sex"] = "Please clarify your Gender"
        return errors


class Patient(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.EmailField(max_length=70)
    # phone = PhoneNumberField()
    sex = models.CharField(max_length=20, default= "unknown")
    date_of_birth = models.DateField(null=False, blank=False, auto_now=True)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+1234567890'.")
    phone_number = models.CharField( max_length=10) # validators should be a list
    sympton = models.TextField(blank=True, null=True)
    # lastVisit = models.CharField(max_length=20)
    # lastVisitComment = models.TextField(blank=True)
    # newComplaints = models.CharField(max_length=20, default= "N/A, please ask")
    # newComplaintsComment = models.TextField(blank=True, default="N/A, please ask")
    # changeMedication = models.CharField(max_length=50)
    # changeLastVisit = models.CharField(max_length=50)
    sweat = models.CharField(max_length=30)
    sweatOther = models.TextField(blank=True)
    appetite = models.CharField(max_length=30)
    appetiteOther = models.TextField(blank=True)
    sleep = models.CharField(max_length=30)
    sleepOther = models.TextField(blank=True)
    tinnitus = models.CharField(max_length=30)
    tinnitusOther = models.TextField(blank=True)
    mouth = models.CharField(max_length=30)
    mouthOther = models.TextField(blank=True)
    digestion = models.CharField(max_length=30)
    digestionOther = models.TextField(blank=True)
    stool = models.CharField(max_length=30)
    stoolOther = models.TextField(blank=True)
    eyes = models.CharField(max_length=30)
    eyesOther = models.TextField(blank=True)
    teeth = models.CharField(max_length=30)
    teethOther = models.TextField(blank=True)
    sexualActivities = models.CharField(max_length=30)
    sexualActivitiesOther = models.TextField(blank=True)
    swelling = models.CharField(max_length=30)
    swellingOther = models.TextField(blank=True)
    thirst = models.CharField(max_length=30)
    thirstOther = models.TextField(blank=True)
    urine = models.CharField(max_length=30)
    urineOther = models.TextField(blank=True)
    nose = models.CharField(max_length=30)
    noseOther = models.TextField(blank=True)
    throat = models.CharField(max_length=30)
    throatOther = models.TextField(blank=True)
    caseNumber = models.CharField(max_length=5) 
    allergies = models.TextField(blank=True)
    diagnosis = models.BooleanField(default=False)
    diagnosisInitial = models.TextField(blank=True)
    diagnosisResult = models.TextField(blank=True)
    agreementCheck = models.BooleanField(default=False)
    tongueCoat = models.ImageField(upload_to=upload_location, default=NULL)
    leftEye = models.ImageField(upload_to=upload_location, default=NULL)
    rightEye = models.ImageField(upload_to=upload_location, default=NULL)
    face = models.ImageField(upload_to=upload_location, default=NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PatientManager()
    def delete(self, *args, **kwargs):
        files = PatientFiles.objects.filter(patient=self)
        for file in files:
           file.delete()
        self.tongueCoat.delete()
        self.leftEye.delete()
        self.rightEye.delete()
        self.face.delete()
        super().delete(*args, **kwargs)

        

class PatientFiles(models.Model):
    patient = models.ForeignKey(Patient, related_name="patientFile", on_delete=models.CASCADE)
    file = models.FileField(default=NULL, upload_to=user_directory_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def delete(self, *args, **kwargs):
       self.file.delete()
       super().delete(*args, **kwargs)
