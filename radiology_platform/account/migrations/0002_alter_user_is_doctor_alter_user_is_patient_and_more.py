# Generated by Django 4.1.6 on 2023-04-14 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_doctor',
            field=models.BooleanField(default=False, verbose_name='Is doctor'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_patient',
            field=models.BooleanField(default=False, verbose_name='Is patient'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_radiologist',
            field=models.BooleanField(default=False, verbose_name='Is radiologist'),
        ),
    ]
