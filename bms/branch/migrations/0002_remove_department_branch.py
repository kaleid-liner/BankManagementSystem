# Generated by Django 3.0.8 on 2020-07-12 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='branch',
        ),
    ]
