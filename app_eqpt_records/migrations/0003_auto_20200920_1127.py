# Generated by Django 3.0.3 on 2020-09-20 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_eqpt_records', '0002_auto_20200919_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleactionmodel',
            name='ActionDate',
            field=models.DateField(),
        ),
    ]
