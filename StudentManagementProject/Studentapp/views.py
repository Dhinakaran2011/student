from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control, never_cache

from Studentapp.models import Student, City, Course


# Create your views here.

@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def reg_fun(request):
    return render(request,'register.html',{'data':''})

@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def regdata_fun(request):
    user_name=request.POST['txt_user']
    user_email=request.POST['email']
    user_pswd=request.POST['pass']
    if User.objects.filter(Q(username=user_name)|Q(email=user_email)).exists():
        return render(request,'register.html',{'data':'username,email and password are already exists'})
    else:
        u1=User.objects.create_superuser(username=user_name,email=user_email,password=user_pswd)
        u1.save()
        return redirect('log')

@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def log_fun(request):
    return render(request,'login.html',{'data':''})


@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def logdata_fun(request):
    user_name=request.POST['txt_user']
    user_pswd=request.POST['pass']
    user1=authenticate(username=user_name,password=user_pswd)

    if user1 is not None:
        if user1.is_superuser:
            login(request,user1)
            return redirect('home')
        else:
            return render(request,'login.html',{'data':'User is not a superuser'})
    else:
        return render(request,'login.html',{'data':'enter proper username and password'})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def home_fun(request):
    return render(request,'home.html')

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def addstudent_fun(request):
    city = City.objects.all()
    course = Course.objects.all()
    return render(request,'addstudents.html',{'City_Data':city,'Course_Data':course})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def readdata_fun(request):
    s1 = Student()
    s1.Stud_Name = request.POST["uname"]
    s1.Stud_Age = request.POST["age"]
    s1.Stud_Phno = request.POST["phno"]
    s1.Stud_City=City.objects.get(City_Name=request.POST['city'])
    s1.Stud_Course=Course.objects.get(Course_Name=request.POST['course'])
    s1.save()
    return redirect('add')

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def display_fun(request):
    s1 = Student.objects.all()
    return render(request,'display.html',{'data': s1})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def update_fun(request,id):
    s1 = Student.objects.get(id=id)
    city = City.objects.all()
    course = Course.objects.all()
    if request.method == 'POST':
        s1.Stud_Name = request.POST["uname"]
        s1.Stud_Age = request.POST["age"]
        s1.Stud_Phno = request.POST["phno"]
        s1.Stud_City = City.objects.get(City_Name=request.POST['city'])
        s1.Stud_Course = Course.objects.get(Course_Name=request.POST['course'])
        s1.save()
        return redirect('dis')
    else:
        return render(request,'update.html',{'data':s1,'City_Data':city,'Course_Data':course})

@login_required
@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def delete_fun(request,id):
    s2 = Student.objects.get(id=id)
    s2.delete()
    return redirect('dis')

@cache_control(no_cache=True,revalidate=True,nostore=True)
@never_cache
def log_out_fun(request):
    logout(request)
    return redirect('log')