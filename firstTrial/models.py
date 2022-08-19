from pyexpat import model
from django.db import models
from address.models import AddressField
import re
import bcrypt


def upload_location(patient,filename):
    return 'patinets/patient_{0}/{1}'.format(patient.id, filename)

def user_directory_path(instance, filename):
    return 'patinets/patient_{0}/{1}'.format(instance.patient.id, filename)

class PatientManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        email_regex = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"
        elif not email_regex.match(postData['email']):
            errors['email'] = "Must be a valid email"
        postEmail=postData['email'].lower()    
        check_email = Patient.objects.filter(email=postEmail)
        if len(check_email) > 0:
            errors['email'] = "This email is already in use"
            errors['email'] = "您输入的邮箱已经被注册了"
        check_phone = Patient.objects.filter(phone_number=postData['phone'])
        if len(check_phone) > 0:
            errors['phone'] = "This phone number is already in use"
            errors['phone'] = "您输入的电话号码已经被注册了"
        if len(postData['password']) < 5:
            errors['password'] = "Password must be at least 5 characters."
            errors['password'] = "密码至少5位数"
        if postData['password'] != postData['passwordConfirm']:
            errors['notmatch'] = "Passwords do not match"
            errors['notmatch'] = "您输入的密码不正确"
        return errors
    
    def udpate_validator(self, postData):
        errors = {}
        email_regex = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"
        elif not email_regex.match(postData['email']):
            errors['email'] = "Must be a valid email"
        postEmail=postData['email'].lower()    
        check_email = Patient.objects.filter(email=postEmail)
        if len(check_email) > 0:
            errors['email'] = "This email is already in use"
            errors['email'] = "您输入的邮箱已经被注册了"
        check_phone = Patient.objects.filter(phone_number=postData['phone'])
        if len(check_phone) > 0:
            errors['phone'] = "This phone number is already in use"
            errors['phone'] = "您输入的电话号码已经被注册了"
        return errors
    
    def update_name(self, postData):
        errors = {}
        if len(postData['firstName'])<1:
            errors['firstName'] = "First Name must be entered."
        if len(postData['lastName'])<1:
            errors['lastName'] = "Last Name must be entered."
        return errors

    def update_phone(self, postData):
        errors = {}
        check_phone = Patient.objects.filter(phone_number=postData['phone'])
        if len(check_phone) > 0:
            errors['phone'] = "This phone number is already in use"
        return errors
        
    def login_validator_byEmail(self, postData):
        errors = {}
        existing_user_email = Patient.objects.filter(email=postData['email'])
        if len(postData['email']) == 0:
            errors['email'] = "Email must be entered"
            
        if len(existing_user_email) != 1:
            errors['email'] = "邮箱不存在 Check your email or try to use your phone number."
        else:
            if len(postData['password']) < 5:
                errors['password'] = "密码至少5位数 Password must be at least 5 characters."           
            elif bcrypt.checkpw(postData['password'].encode(), existing_user_email[0].password.encode()) != True:
                errors['mismatch'] = "邮箱或密码不正确 Invalid Email or Password."
        return errors

    def login_validator_byPhone(self, postData):
        errors = {}
        existing_user_phone = Patient.objects.filter(phone_number=postData['phone'])
        if len(postData['phone']) == 0:    
            errors['phone'] = "Phone Number must be entered"
        if len(existing_user_phone) !=1:
            errors['phone'] = "电话号码不存在 Check your phone number or try to use your email"
        else:
            if len(postData['password']) < 5:
                errors['password'] = "密码至少5位数 Password must be at least 5 characters."
            elif bcrypt.checkpw(postData['password'].encode(), existing_user_phone[0].password.encode()) != True:
                errors['mismatch'] = "电话号码或密码不正确 Invalid Phone Number or Password."
        return errors

    def password_change(self, postData):
        errors = {}
        existing_patient = Patient.objects.get(id = postData['patient_id'])

        if bcrypt.checkpw(postData['oldPassword'].encode(), existing_patient.password.encode()) != True:
            errors['invalid'] = "Password Not Match."
        else:
            if len(postData['newPassword']) < 5:
                errors['newPassword'] = "New password must be at least 5 characters."
            if postData['newPassword'] != postData['confirmPassword']:
                errors['confirmPassword'] = "Password Confirmation not match."
        return errors

class Patient(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=255)
    sex = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=False, blank=False)
    phone_number = models.CharField( max_length=10) 
    insurance = models.CharField(max_length=45)
    insuranceId = models.CharField(max_length=45)
    hearUs = models.CharField(max_length=45)
    referByFriend = models.CharField(max_length=105)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PatientManager()




class PatientForm(models.Model):
    patient = models.ForeignKey(Patient, related_name="patientForm", on_delete=models.CASCADE)
    sympton = models.TextField(blank=True, null=True)
    lastVisit = models.CharField(max_length=20)
    lastVisitComment = models.TextField(blank=True)
    newComplaints = models.CharField(max_length=20)
    newComplaintsComment = models.TextField(blank=True)
    changeMedication = models.CharField(max_length=50)
    changeLastVisit = models.CharField(max_length=50)
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
    tongueCoat = models.ImageField(upload_to=upload_location)
    leftEye = models.ImageField(upload_to=upload_location)
    rightEye = models.ImageField(upload_to=upload_location)
    face = models.ImageField(upload_to=upload_location)
    question = models.BooleanField(default=False)
    lungResult = models.TextField(blank=True)
    pericardiumResult = models.TextField(blank=True)
    heartResult = models.TextField(blank=True)
    stomachResult = models.TextField(blank=True)
    gallbladderResult = models.TextField(blank=True)
    urinaryBladderResult = models.TextField(blank=True)
    spleenResult = models.TextField(blank=True)
    liverResult = models.TextField(blank=True)
    kidneyResult = models.TextField(blank=True)
    large_intestineResult = models.TextField(blank=True)
    san_jiaoResult = models.TextField(blank=True)
    small_intestineResult = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # def delete(self, *args, **kwargs):
    #     files = PatientFiles.objects.filter(patient=self)
    #     for file in files:
    #        file.delete()
    #     self.tongueCoat.delete()
    #     self.leftEye.delete()
    #     self.rightEye.delete()
    #     self.face.delete()
    #     super().delete(*args, **kwargs)

        

class PatientFiles(models.Model):
    patient = models.ForeignKey(Patient, related_name="patientFile", on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def delete(self, *args, **kwargs):
       self.file.delete()
       super().delete(*args, **kwargs)


class Partner(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.EmailField(max_length=70)
    notify = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)