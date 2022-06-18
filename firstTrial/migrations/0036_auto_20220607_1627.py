# Generated by Django 3.2.13 on 2022-06-07 23:27

from django.db import migrations, models
import django.db.models.deletion
import firstTrial.models


class Migration(migrations.Migration):

    dependencies = [
        ('firstTrial', '0035_auto_20220606_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='agreementCheck',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='allergies',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='appetite',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='appetiteOther',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='caseNumber',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='diagnosis',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='diagnosisInitial',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='diagnosisResult',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='digestion',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='digestionOther',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='eyes',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='eyesOther',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='face',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='leftEye',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='mouth',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='mouthOther',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='nose',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='noseOther',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='rightEye',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='sexualActivities',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='sexualActivitiesOther',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='sleep',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='sleepOther',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='stool',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='stoolOther',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='sweat',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='sweatOther',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='swelling',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='swellingOther',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='sympton',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='teeth',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='teethOther',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='thirst',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='thirstOther',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='throat',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='throatOther',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='tinnitus',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='tinnitusOther',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='tongueCoat',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='urine',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='urineOther',
        ),
        migrations.AddField(
            model_name='patient',
            name='hearUs',
            field=models.CharField(default=None, max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='insurance',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='insuranceId',
            field=models.CharField(default=None, max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='password',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='referByFriend',
            field=models.CharField(default=None, max_length=105),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='PatientForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sympton', models.TextField(blank=True, null=True)),
                ('lastVisit', models.CharField(max_length=20)),
                ('lastVisitComment', models.TextField(blank=True)),
                ('newComplaints', models.CharField(max_length=20)),
                ('newComplaintsComment', models.TextField(blank=True)),
                ('changeMedication', models.CharField(max_length=50)),
                ('changeLastVisit', models.CharField(max_length=50)),
                ('sweat', models.CharField(max_length=30)),
                ('sweatOther', models.TextField(blank=True)),
                ('appetite', models.CharField(max_length=30)),
                ('appetiteOther', models.TextField(blank=True)),
                ('sleep', models.CharField(max_length=30)),
                ('sleepOther', models.TextField(blank=True)),
                ('tinnitus', models.CharField(max_length=30)),
                ('tinnitusOther', models.TextField(blank=True)),
                ('mouth', models.CharField(max_length=30)),
                ('mouthOther', models.TextField(blank=True)),
                ('digestion', models.CharField(max_length=30)),
                ('digestionOther', models.TextField(blank=True)),
                ('stool', models.CharField(max_length=30)),
                ('stoolOther', models.TextField(blank=True)),
                ('eyes', models.CharField(max_length=30)),
                ('eyesOther', models.TextField(blank=True)),
                ('teeth', models.CharField(max_length=30)),
                ('teethOther', models.TextField(blank=True)),
                ('sexualActivities', models.CharField(max_length=30)),
                ('sexualActivitiesOther', models.TextField(blank=True)),
                ('swelling', models.CharField(max_length=30)),
                ('swellingOther', models.TextField(blank=True)),
                ('thirst', models.CharField(max_length=30)),
                ('thirstOther', models.TextField(blank=True)),
                ('urine', models.CharField(max_length=30)),
                ('urineOther', models.TextField(blank=True)),
                ('nose', models.CharField(max_length=30)),
                ('noseOther', models.TextField(blank=True)),
                ('throat', models.CharField(max_length=30)),
                ('throatOther', models.TextField(blank=True)),
                ('caseNumber', models.CharField(max_length=5)),
                ('allergies', models.TextField(blank=True)),
                ('diagnosis', models.BooleanField(default=False)),
                ('diagnosisInitial', models.TextField(blank=True)),
                ('diagnosisResult', models.TextField(blank=True)),
                ('agreementCheck', models.BooleanField(default=False)),
                ('tongueCoat', models.ImageField(upload_to=firstTrial.models.upload_location)),
                ('leftEye', models.ImageField(upload_to=firstTrial.models.upload_location)),
                ('rightEye', models.ImageField(upload_to=firstTrial.models.upload_location)),
                ('face', models.ImageField(upload_to=firstTrial.models.upload_location)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patientForm', to='firstTrial.patient')),
            ],
        ),
    ]
