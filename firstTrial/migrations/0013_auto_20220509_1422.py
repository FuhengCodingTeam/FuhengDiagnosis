# Generated by Django 2.2 on 2022-05-09 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstTrial', '0012_auto_20220509_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(blank=True, default='unknown', max_length=20),
        ),
    ]
