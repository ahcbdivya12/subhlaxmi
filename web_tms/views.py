from django.shortcuts import render,redirect

from django.contrib.auth import login as auth_login

from .models import reg,god,cont,inqu

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


from django.contrib import messages


@login_required(login_url='login')

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method=='POST':
            uname=request.POST.get('name')
            email=request.POST.get('email')
            subject=request.POST.get('subject')
            message=request.POST.get('message')
            if cont.objects.filter(email=email).exists():
                messages.warning(request,'email is already exists!')
                return redirect(contact)
            else:
                dbs_2 = cont(name=uname, email=email, subject=subject, message=message)
                dbs_2.save()
                return redirect('/')
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
def agent(request):
    return render(request, 'agent.html')
def list(request):
    return render(request, 'list.html')
def Inquiry(request):
    if request.method=='POST':
            uname=request.POST.get('name')
            lname=request.POST.get('lname')
            mobile=request.POST.get('mobile')
            email=request.POST.get('email')
            subject=request.POST.get('subject')
            message=request.POST.get('meg')
            if inqu.objects.filter(mobile=mobile).exists():
                messages.warning(request,'mobile is already exists!')
                return redirect(Inquiry)
            else:
                dbs_3 = inqu(name=uname,lname=lname, mobile=mobile, email=email, subject=subject, message=message)
                dbs_3.save()
                return redirect('/')
    return render(request, 'Inquiry.html')

def type(request):
    return render(request, 'type.html')

def book(request):
    if request.method=='POST':
            uname=request.POST.get('name')
            lname=request.POST.get('lname')
            mobile=request.POST.get('mobile')
            email=request.POST.get('email')
            t_type=request.POST.get('type')
            p_city=request.POST.get('p_city')
            d_city=request.POST.get('d_city')
            goods=request.POST.get('goods')

            if god.objects.filter(mobile=mobile).exists():
                messages.warning(request,'mobile is already exists!')
                return redirect(contact)
            else:
                dbs_1 = god(name=uname, lname=lname, mobile=mobile, email=email, truck_type=t_type,p_city=p_city,d_city=d_city ,goods=goods)
                dbs_1.save()
                return redirect('/')
    return render(request, 'book.html')

def sigin(request):
    if request.method=='POST':
        username=request.POST.get('name')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('http://127.0.0.1:8000/')
        else:
            #return HttpResponse("username and password incoreect !!")
            return redirect('../sigin')
    return render(request, 'sigin.html')

def sigup(request):
        if request.method=='POST':
            uname=request.POST.get('name')
            email=request.POST.get('email')
            pass1=request.POST.get('password')
            pass2=request.POST.get('cpassword')
            mobile=request.POST.get('mobile')
            city=request.POST.get('city')
            address=request.POST.get('address')
            gender= request.POST.get('gender') 
            if reg.objects.filter(email=email).exists():
                messages.warning(request,'email is already exists!')
                return redirect(sigup)
            elif pass1!=pass2:
                messages.warning(request,'password and confirm password does not match !')
                return redirect(sigup)
            else:
                dbs = reg(name=uname, email=email, password=pass1, cpassword=pass2, mobile=mobile, city=city, address=address, gender=gender)
                dbs.save()
                my_user = User.objects.create_user(uname,email,pass1)
                my_user.save()
                return redirect('../sigin')
        return render(request, 'sigup.html')

def LogoutPage(request):
    logout(request)
    return redirect('../sigin')
