# Generated by Django 2.2 on 2022-05-11 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstTrial', '0017_patient_tongueimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='tongueImg',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
