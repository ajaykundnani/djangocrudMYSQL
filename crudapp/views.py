from django.shortcuts import render,HttpResponseRedirect
from .models import Employee
from .forms import EmployeeForm

# Create your views here.

def add(request):
    if request.method == 'POST':
        myfm = EmployeeForm(request.POST)
        if myfm.is_valid():
            myfm.save()
            return HttpResponseRedirect('/')

    else:
        myfm = EmployeeForm()
        obj = Employee.objects.all()
        return render(request,'add.html',{'form':myfm,'obj':obj})

def edit(request,id):
    if request.method == 'POST':
        myid = Employee.objects.get(id=id)
        myfm = EmployeeForm(request.POST,instance=myid)
        if myfm.is_valid():
            myfm.save()
            return HttpResponseRedirect('/')
    else:
        myid = Employee.objects.get(id=id)
        myfm = EmployeeForm(instance=myid)
        return render(request,'edit.html',{'form':myfm})

def delete(request,id):
    myid = Employee.objects.get(id=id)
    myid.delete()
    return HttpResponseRedirect('/')
