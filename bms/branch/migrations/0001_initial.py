# Generated by Django 3.0.8 on 2020-07-12 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('city', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=32)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branch.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=18, unique=True)),
                ('name', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=256)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staffs', to='branch.Department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_id', models.CharField(max_length=18, unique=True)),
                ('name', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=256)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('department', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manager', to='branch.Department')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
