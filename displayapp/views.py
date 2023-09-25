from django.shortcuts import render
from django.http import HttpResponse
from .models import Display

def display(request):
    if request.method=='GET':
        dis=Display.objects.all()
        return render(request,'form.html',{'disp':dis})
    else:
        Display(
        FIrst_Name=request.POST.get('fname'),
        Last_Name=request.POST.get('lname'),
        EmailId=request.POST.get('email'),
        Mobile=request.POST.get('mobile'),
        Skills=request.POST.get('skills'),
        Experience=request.POST.get('exp'),
        Salary=request.POST.get('salary'),
        Company=request.POST.get('company')
        ).save()
        dis=Display.objects.all()
        return render(request,'form.html',{'disp':dis})
