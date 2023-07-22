from django.shortcuts import render,redirect
from django.contrib import messages,auth

# using Default Django User Model
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from contacts.models import Contact



def login(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"You Are Logged In")
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid Passowrd or Username")
            return redirect('login')    

   
    return render(request,'accounts/login.html')

def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password==confirm_password:
           if User.objects.filter(username=username).exists():
            messages.error(request,"User Already Exist")
            return redirect("register")
           else:
            if User.objects.filter(email=email).exists():
                messages.error(request,"Email Exists")
                return redirect('regiser')
            else:
                user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                auth.login(request,user)
                messages.success(request,"You Are Logged In")
                return redirect('dashboard')
                user.save()
                
                messages.success(request,"Register Successfully") 
                return redirect('login')
        
        else:
            messages.error(request,"Password do not matched")
            return redirect('register')

                            
    else:   
        return render(request,'accounts/register.html')
@login_required(login_url='login')       
def dashboard(request):

    user_inquiry=Contact.objects.order_by('-create_date').filter(user_id=request.user.id)

    data={
        'inquires':user_inquiry
    }  
    return render(request,'accounts/dashboard.html',data)
def logout(request):
    if request.method=='POST':
     auth.logout(request)
     
     return redirect('home')   
    return redirect('home')        
# Create your views here.
