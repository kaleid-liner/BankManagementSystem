# Generated by Django 3.0.8 on 2020-07-14 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0003_auto_20200713_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='date_joined',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='staff',
            name='date_joined',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]
