# Generated by Django 4.1.6 on 2023-04-14 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_is_doctor_alter_user_is_patient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_doctor',
            field=models.CharField(choices=[('doctor', 'Doctor'), ('radiologist', 'Radiologist'), ('patient', 'Patient')], default='patient', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_patient',
            field=models.CharField(choices=[('doctor', 'Doctor'), ('radiologist', 'Radiologist'), ('patient', 'Patient')], default='patient', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_radiologist',
            field=models.CharField(choices=[('doctor', 'Doctor'), ('radiologist', 'Radiologist'), ('patient', 'Patient')], default='patient', max_length=20),
        ),
    ]
