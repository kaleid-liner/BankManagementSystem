from django.db import models
from django.utils import timezone


# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=128, unique=True)
    city = models.CharField(max_length=256)


class Department(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=32)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)


class StaffInfo(models.Model):
    card_id = models.CharField(unique=True, max_length=18)
    name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64)
    address = models.CharField(max_length=256)
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Staff(StaffInfo):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='staffs')


class Manager(StaffInfo):
    department = models.OneToOneField(Department, on_delete=models.SET_NULL, null=True, related_name='manager')
