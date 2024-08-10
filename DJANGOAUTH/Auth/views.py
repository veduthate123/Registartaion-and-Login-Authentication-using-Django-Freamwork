from django.shortcuts import render ,redirect
from django.http import HttpResponse
from Auth.models import *
from django.contrib import messages
from django.contrib.auth.hashers import check_password , make_password


def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        
        role = request.POST.get("role",'default')
        firstname = request.POST.get("First_Name",'default')
        lastname = request.POST.get("Last_Name",'default')
        profilePicture = request.FILES.get("Profile_Picture")
        username = request.POST.get("Username",'default')
        email = request.POST.get("Email_Id",'default')
        password = request.POST.get("Password",'default')
        confirmPassword = request.POST.get("confirmPassword",'default')
        addressLine1 = request.POST.get("Address_Line1",'default')
        city = request.POST.get("City",'default')
        state = request.POST.get("State",'default')
        pincode = request.POST.get("Pincode",'default')
        # print(profilePicture)
        
        if password != confirmPassword:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
        
        hashed_password = make_password(password)
        
        registeration = Registerinfo(First_Name=firstname,Last_Name=lastname,Profile_Picture=profilePicture,Username=username,Email_Id=email,
                                     Password=hashed_password,Address_Line1=addressLine1,City=city,State=state,Pincode=pincode,role=role)
        
        registeration.save()
        messages.success(request, "Resgiter Successfully.")
        return redirect('login')
    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('Email_Id')
        password = request.POST.get('Password')
        
        if user := Registerinfo.objects.get(Email_Id=email):
            
            if check_password(password, user.Password):
                request.session['user_id'] = user.id
                messages.success(request, "Login successful!")
                return redirect('info')
            else:
                messages.error(request, "Invalid email or password.")
                return redirect('login')

        else:
            messages.error(request, "Invalid email or password.")
            return redirect('login')
    
    return render(request, 'login.html')


def info(request):
    user_id = request.session.get('user_id')
    
    if user := Registerinfo.objects.get(id=user_id):
        print(user)
    else:
        messages.error(request, "User not found.")
        return redirect('login')

    context = {
        'user': user
    }
    return render(request, 'info.html',context)