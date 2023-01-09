from django.shortcuts import render,redirect
from .forms import Student_form
from .models import Student_model
# Create your views here.

def savedemo(request):
    if request.method=="POST":
        data=Student_form(request.POST)
        if data.is_valid():
            data.save()
            return redirect("/")
    else:
        fm = Student_form()
        return render(request,'showform.html',{'form':fm})

def displaydata(request):
    data=Student_model.objects.all()
    return render(request,'display.html',{'res':data})


def edit(request,id):
    data=Student_model.objects.get(id=id)
    return render(request,'edit.html',{"res":data})

def updatedata(request,id):
    emp = Student_model.objects.get(id=id)
    data= Student_form(request.POST,instance=emp)
    if data.is_valid():
        data.save()
        return redirect("/display")


def deletedata(request,id):
    data = Student_model.objects.get(id=id)
    data.delete()
    return redirect("/display")

