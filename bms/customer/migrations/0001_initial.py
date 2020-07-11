# Generated by Django 3.0.8 on 2020-07-11 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=18, unique=True)),
                ('name', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=256)),
                ('contact_name', models.CharField(max_length=64)),
                ('contact_phone_number', models.CharField(max_length=64)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_relationship', models.CharField(max_length=64)),
            ],
        ),
    ]
