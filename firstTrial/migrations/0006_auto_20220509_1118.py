# Generated by Django 2.2 on 2022-05-09 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstTrial', '0005_auto_20220509_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='lastTreatment',
        ),
        migrations.AddField(
            model_name='patient',
            name='lastVisit',
            field=models.CharField(default='better', max_length=50),
        ),
    ]
