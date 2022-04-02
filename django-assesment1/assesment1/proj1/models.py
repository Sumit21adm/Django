# Create your models here.
from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100, default=" ")
    last_name = models.CharField(max_length=100, blank=True)
    roll_no = models.IntegerField(blank=True)

    class Meta:
        db_table = "student"


class Employee(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=30, blank=True)

    class Meta:
        db_table = "employee"

# python3 manage.py makemigrations
# python3 manage.py migrate
