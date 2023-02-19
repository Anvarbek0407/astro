from django.shortcuts import redirect,render
from .models import CustomUser
from django.contrib.auth import login, authenticate, logout


def sign_up(request):
    context = {}
   
    if request.method == "POST":
        
        post = request.POST
        phone = post.get('phone', False)
        first_name = post.get('first_name', False)
        last_name = post.get('last_name', False)
        middle_name = post.get('middle_name', False)
        email = post.get('email', False)
        password1 = post.get('password1',False)
        password2 = post.get('password2',False)
        if first_name and phone and last_name and middle_name and email and password1 and password2:
            if password1 == password2:
                if not CustomUser.objects.filter(phone=phone).exists():
                    user = CustomUser.objects.create(first_name=first_name,phone=phone,last_name=last_name, middle_name=middle_name,email=email)
                    user.set_password(password1)
                    user.save()
                    login(request,user)
                    return redirect('home')
                
                else:
                    context["error"] = "Bu telefon raqam egaasi oldin ro'yxatdan o'tgan" 
                
            else:
                context["error"] = "Qayta kiritlgan parol xato"
            
        else:
            context["error"] = "Malumotlarni to'liq to'ldiring"
    
    return render(request, 'register.html',context)
def sign_in(request):
    context = {}
    
    if request.method == "POST":
        
        post = request.POST
        phone = post.get('phone', False)
        password1 = post.get('password1',False)
        user = authenticate(request, phone=phone, password=password1)
        if user is not None:
            login(request,user)
            return redirect('home')
    
        else:
            context["error"] = "Bu telefon raqam egaasi oldin ro'yxatdan o'tgan" 
       
    return render(request, 'login.html',context)
     
def log_out(request):
    logout(request)
    return redirect('home')