# Generated by Django 4.1.6 on 2023-04-14 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_patient_radiologist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='radiologist',
        ),
    ]
