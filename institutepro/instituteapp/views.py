from django.shortcuts import render,redirect
from .models import Courses,feedbackdata,ContactData
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
import datetime 
date1=datetime.datetime.now()
# Create your views here.

@login_required(login_url='loginpage')
def homepage(request):
    return render(request,'homepage.html')

@login_required(login_url='loginpage')
def contactpage(request):
    if request.method=='GET':
        return render(request,'contactpage.html')
    else:
        ContactData(first_name=request.POST['fname'],
            last_name=request.POST['lname'],
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            course=request.POST['cname'],
            location=request.POST['loc']).save()
        return render(request,'contactpage.html')

@login_required(login_url='loginpage')
def servicepage(request):
    courses=Courses.objects.all()
    return render(request,'servicepage.html',{'courses':courses})

@login_required(login_url='loginpage')
def feedbackpage(request):
    if request.method=='GET':
        data=reversed(feedbackdata.objects.all())
        return render(request,'feedbackpage.html',{'data':data})
    else:
        feedbackdata(
            content=request.POST['comment'],
            user_name=request.POST['user'],
            date=date1).save()
        data=reversed(feedbackdata.objects.all())
        return render(request,'feedbackpage.html',{'data':data})

@login_required(login_url='loginpage')
def gallerypage(request):
    return render(request,'gallerypage.html')

def loginpage(request):
    if request.method=='GET':
        return render(request,'loginpage.html')
    else:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(homepage)
        else:
            return HttpResponse("Invalid Details")
        
def logoutpage(request):
    logout(request)
    return redirect(loginpage)

def registerpage(request):
    if request.method=='GET':
        form=RegistrationForm()
        return render(request,'register.html',{'form':form})
    else:
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(user.password)
            form.save()
            return redirect(loginpage)
        else:
            return HttpResponse('Invlid form')


