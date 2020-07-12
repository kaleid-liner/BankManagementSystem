from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Branch)
admin.site.register(models.Department)
admin.site.register(models.Manager)
admin.site.register(models.Staff)
