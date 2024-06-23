from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        print((request.user))
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
       
        if user is not None:
            login(request,user)
            messages.success(request,"You have been Logged in")
            return redirect('website:home')
        else:
            
            messages.success(request,"You didn't login")
            return redirect('website:home')
      
    return render(request,'home.html',{})
def loginUser(request):
    pass
def logoutUser(request):
    logout(request)
    messages.success(request,"You have been logged out")
    redirect('website:home')   
def registerUser(request):
    return render(request,"register.html")