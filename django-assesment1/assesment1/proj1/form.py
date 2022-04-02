from django import forms
from proj1.models import Student

from proj1.models import Employee


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        #fields = "__all__"
        fields = ('name', 'email', 'job_title')
