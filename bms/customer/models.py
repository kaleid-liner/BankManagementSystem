from django.db import models


# Create your models here.
class Customer(models.Model):
    card_id = models.CharField(unique=True, max_length=18)
    name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64)
    address = models.CharField(max_length=256)
    contact_name = models.CharField(max_length=64)
    contact_phone_number = models.CharField(max_length=64)
    contact_email = models.EmailField()
    contact_relationship = models.CharField(max_length=64)

    def __str__(self):
        return '{}#{}'.format(self.name, self.pk)
