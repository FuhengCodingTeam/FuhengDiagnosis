# Generated by Django 2.2 on 2022-05-06 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstTrial', '0002_auto_20220506_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='diagnosisResult',
            field=models.TextField(blank=True),
        ),
    ]
