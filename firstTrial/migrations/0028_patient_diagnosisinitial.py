# Generated by Django 2.2 on 2022-05-18 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstTrial', '0027_auto_20220517_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='diagnosisInitial',
            field=models.TextField(blank=True),
        ),
    ]