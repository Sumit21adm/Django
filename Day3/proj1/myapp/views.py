from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myapp.forms import EmployeeForm, EmployeeForm2
from myapp.utils import upload_file



def index(req):
    if req.method == 'POST':
        empForm = EmployeeForm(req.POST)
        if empForm.is_valid():
            return HttpResponse("good job")
        else:
            return render(req, 'employee.html', {'form': empForm})
    else:
        emp = EmployeeForm()
        return render(req, "employee.html", {"form": emp})


def index2(request):
    if request.method == 'POST':
        empForm2 = EmployeeForm2(request.POST, request.FILES)
        if empForm2.is_valid():

            # lets do something
            # print (request.FILES['profile_image'])
            upload_file(request.FILES['profile_image'])
            return HttpResponse("good job")
        else:
            return render(request, 'index2.html', {'form': empForm2})
    else:
        emp = EmployeeForm2()

    return render(request, "index2.html", {"form": emp})