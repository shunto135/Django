from django.http import request
from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm

def welcome(request):
    return render(request,"welcome.html")

def load_form(request):
    form = StudentForm
    return render(request,"index.html", {'form':form})

def add(request):
    form = StudentForm(request.POST)
    form.save()
    return redirect('/show')
    
def show(request):
    student = Student.objects.all
    return render(request, 'show.html', {'student': student})

def edit(request,id):
    student= Student.objects.get(id=id)
    return render(request, 'edit.html', {'student':student})

def update(request,id):
    student= Student.objects.get(id=id)
    form=StudentForm(request.POST,instance=student)
    form.save()
    return redirect('/show')

def delete(request,id):
    student= Student.objects.get(id=id)
    student.delete()
    return redirect('/show')

def search(request):
    given_name=request.POST['name']
    student= Student.objects.filter(sname__icontains=given_name)
    return render(request, 'show.html', {'student': student})