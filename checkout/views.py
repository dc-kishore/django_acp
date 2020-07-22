from django.shortcuts import render
from django.contrib.auth import authenticate,login,get_user_model,logout
from django.contrib import messages,auth
from Damage_assesment.forms import LoginForm,RegisterForm
# Create your views here.
def checkout(request):
    return render(request,'checkout/checkout.html',{})

def logout_view(request):
    logout(request)
    messages.info(request,"Logged out successfully!")
    return render(request=request,template_name="index.html", context={
        "login_form":LoginForm
    }) 