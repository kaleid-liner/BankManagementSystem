from django.db import models
import datetime


# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=128, unique=True)
    city = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class StaffInfo(models.Model):
    card_id = models.CharField(unique=True, max_length=18)
    name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64)
    address = models.CharField(max_length=256)
    date_joined = models.DateField(default=datetime.date.today, blank=True)
    branch = models.ForeignKey(Branch, related_name='%(class)ss', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{}#{}'.format(self.name, self.pk)

    class Meta:
        abstract = True


class Staff(StaffInfo):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='staffs')


class Manager(StaffInfo):
    department = models.OneToOneField(Department, on_delete=models.SET_NULL, null=True, related_name='manager')
