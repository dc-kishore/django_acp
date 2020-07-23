from django.shortcuts import render,redirect
from django.template import RequestContext
from django.contrib.auth import authenticate,login,get_user_model
from .forms import LoginForm,RegisterForm
from Policy.forms import InsuranceForm,PolicyForm
from django.views.generic import CreateView, FormView, DetailView, View, UpdateView
from django.contrib import messages
import pymongo 
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        policy_form=PolicyForm(request.POST or None)
        context={
                 "policy_form":policy_form
            }
        print("hai")
        if policy_form.is_valid():
            print("hai1")
            print(policy_form.cleaned_data)
            context['policy_form']=PolicyForm()
            policy_form.save()
            return redirect('insurance')
             
    else:
        login_form=LoginForm(request.POST or None)
    # uri="mongodb+srv://m001-student:m001-mongodb-basics@cluster0-du7ul.mongodb.net/<dbname>?retryWrites=true&w=majority"
    # client = pymongo.MongoClient(uri)
    # db= client.video
    # print(db.collection)
        context={
            "login_form":login_form
        }
        print("User logged in")
        if login_form.is_valid():
            
            print(login_form.cleaned_data)
            context['login_form']=LoginForm()
            username=login_form.cleaned_data.get("username")
            password=login_form.cleaned_data.get("password")

            user=authenticate(request,username=username,password=password)
            print(user)
            if user is not None:
                login(request,user)
                messages.info(request, "Logged in successfully!")
                context['login_form']=LoginForm()
                print(request.user.is_authenticated)
           # login_form.save()
                return redirect("/")
            else:
                print("error")
    return render(request,'index.html',context)

User=get_user_model()
def register_page(request):
    register_form=RegisterForm(request.POST or None)
    context={
        "form":register_form
    }
    print("User registered") 
    if register_form.is_valid():
        print(register_form.errors)
        # print("User:",register_form.cleaned_data)
        context['form']=RegisterForm()
        username=register_form.cleaned_data.get("username")
        password=register_form.cleaned_data.get("password")
        password1=register_form.cleaned_data.get("password1")
        email=register_form.cleaned_data.get("Email")
        new_user=User.objects.create_user(username=username,password=password1,email=email)
        new_user.save()
        print(username)
        return redirect("/login")
    return render(request,'register/registar.html',context)

def estimate(request):
    return render(request,'estimation/estimation.html',{})

def about(request):
    return render(request,'about/about.html',{})
