# Generated by Django 3.0.3 on 2020-09-21 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_eqpt_records', '0007_vehicleaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicleactionmodel',
            name='Placeholder',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vehicleactionmodel',
            name='Title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='VehicleAction',
        ),
    ]
