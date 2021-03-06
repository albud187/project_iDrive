# Generated by Django 3.0.3 on 2020-09-18 22:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('vehicle_make', models.CharField(max_length=200)),
                ('vehicle_modeltype', models.CharField(max_length=200)),
                ('VINNumber', models.CharField(max_length=200)),
                ('Notes', models.TextField(null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleRecordModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_eqpt_records.VehicleModel')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleActionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actionDate', models.DateTimeField()),
                ('description', models.TextField(null=True)),
                ('cost', models.FloatField()),
                ('VehicleRecord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_eqpt_records.VehicleRecordModel')),
            ],
        ),
    ]
