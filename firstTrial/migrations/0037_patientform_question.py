# Generated by Django 3.2.13 on 2022-06-16 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstTrial', '0036_auto_20220607_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientform',
            name='question',
            field=models.BooleanField(default=False),
        ),
    ]