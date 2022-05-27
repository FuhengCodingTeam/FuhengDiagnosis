# Generated by Django 2.2 on 2022-05-12 16:35

from django.db import migrations, models
import django.db.models.deletion
import firstTrial.models


class Migration(migrations.Migration):

    dependencies = [
        ('firstTrial', '0019_auto_20220511_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='tongueImg',
        ),
        migrations.CreateModel(
            name='patientImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to=firstTrial.models.upload_location)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imgs', to='firstTrial.Patient')),
            ],
        ),
    ]
