from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records=Record.objects.all()
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
      
    return render(request,'home.html',{'records':records    })
def loginUser(request):
    pass
def logoutUser(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect('website:home')   
def registerUser(request):
    
    if request.method == 'POST':
        print("registr")
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password1"]
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"you logged in successfully")
                return redirect('website:home')    
    else:
                form=SignUpForm()
                print("form")
                return render(request,"register.html",{'form':form })    
    return render(request,"register.html",{'form':form })   
def record(request,pk):
     
     if request.user.is_authenticated:
          try:
           customerRecord=Record.objects.get(id=pk)
           return render (request,'record.html',{'record':customerRecord})
          except:
               return redirect('website:home')
     messages.success(request,"you are not logged in successfully")
     return redirect('website:home')
def deleteRecord(request,pk):
   if request.user.is_authenticated:  
     deleteRecord=Record.objects.get(id=pk)
     deleteRecord.delete()
     messages.success(request,"Delete record successfully")
   else:
       messages.success(request,"You are not logged in successfully")
   return redirect('website:home')

def addRecord(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				addRecord = form.save()
				messages.success(request, "Record Added...")
				return redirect('website:home')
		return render(request, 'addRecord.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('website:home')
    

def updateRecord(request,pk):
     if request.user.is_authenticated:
          currenteRecord=Record.objects.get(id=pk)
          form=AddRecordForm(request.POST or None,instance=currenteRecord)
          if form.is_valid():
           form.save()
           messages.success(request, "form is saved successfully")
           return redirect('website:home')
          return render(request, 'updateRecord.html',{'form':form})
     else:
          messages.error(request,"you must be logged in")
          return redirect(request,'website:home')