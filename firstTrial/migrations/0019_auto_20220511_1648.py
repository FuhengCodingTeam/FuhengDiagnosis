# Generated by Django 2.2 on 2022-05-11 23:48

from django.db import migrations, models
import firstTrial.models


class Migration(migrations.Migration):

    dependencies = [
        ('firstTrial', '0018_auto_20220511_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='tongueImg',
            field=models.ImageField(blank=True, null=True, upload_to=firstTrial.models.upload_location),
        ),
    ]
