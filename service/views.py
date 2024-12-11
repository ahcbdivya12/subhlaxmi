from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required

from web_tms.models import reg,cont,inqu,god

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,logout,login

from django.contrib.auth.decorators import login_required

from django.contrib import messages

@login_required(login_url='login')

# Create your views here.
def service_index(request):
	return render(request,"service_index.html",{})

def form(request):
	return render(request,"service_form.html",{})

def table(request):
	database_data = cont.objects.all()
	return render(request,"service_table.html",{'database_data': database_data})

def service_inquiry(request):
	database_data = inqu.objects.all()
	return render(request,"service_inquiry.html",{'database_data': database_data})


def service_book(request):
	database_data = god.objects.all()
	return render(request,"service_book.html",{'database_data': database_data})


def admin_users(request):
	database_data = reg.objects.all()
	return render(request,"admin_users.html",{'database_data': database_data})

def service_invoice(request, column_id):
	try:
		data = god.objects.get(id=column_id)
	except god.DoesNotExist:
		data = None
	return render(request, "service_invoice.html", {'data': data})



def signin(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('http://127.0.0.1:8000/admin/home')
        else:
            #return HttpResponse("username and password incoreect !!")
            return redirect('../admin/')
    return render(request,"service_signin.html",{})

def LogoutPage(request):
    logout(request)
    return redirect('../admin/')
