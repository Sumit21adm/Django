from django.db import models
from django.forms import CharField, PasswordInput


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, blank=True)
    mobno = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=200, blank=True)
    password = models.CharField(max_length=50, default='')
    c_password = models.CharField(max_length=50, default='')

    class Meta:
        db_table = "employee"


class EmployeePimg(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=200, blank=True)

    profile_image = models.FileField(blank=True)

    class Meta:
        db_table = "employee_pimg"