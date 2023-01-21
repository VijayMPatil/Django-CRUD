from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeRegisterForm
# Create your views here.

def index(request):
    return render(request,'register/base.html')

def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request,'register/employee_list.html',context)

def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeRegisterForm
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeRegisterForm(instance=employee)
        return render(request, "register/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeRegisterForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeRegisterForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')      

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')