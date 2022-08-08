from django.shortcuts import render, redirect
from .models import Employees


# Create your views here.

def index(request):
    all_obj = Employees.objects.all()
    return render(request,'index.html',{'all_obj':all_obj})

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        emp = Employees(
            name = name,
            email = email,
            address = address,
            phone = phone
        )
        emp.save()
        return redirect('/')
    return render(request,'index.html')

def edit(request):
    all_obj = Employees.objects.all()
    return render(request, 'index.html', {'all_obj': all_obj})

def update(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        emp = Employees(
            id = id,
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        emp.save()
        return redirect('/')
    return render(request, 'index.html')

def delete(request,id):
    all_obj = Employees.objects.filter(id=id)
    all_obj.delete()
    return redirect('/')
