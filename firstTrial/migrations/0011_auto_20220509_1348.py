# Generated by Django 2.2 on 2022-05-09 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstTrial', '0010_auto_20220509_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='appetite',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='digestion',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='eyes',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='mouth',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='nose',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sexualActivities',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sleep',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='stool',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sweat',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='swelling',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='teeth',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='thirst',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='throat',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='tinnitus',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='urine',
            field=models.CharField(max_length=30),
        ),
    ]
