# Generated by Django 5.1.4 on 2025-04-11 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_doctorprofile_clinic_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='clinic_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
