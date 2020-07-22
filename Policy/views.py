from django.shortcuts import render,redirect
from django.template import RequestContext
from django.contrib.auth import authenticate,login,get_user_model
from .forms import PolicyForm,InsuranceForm
# Create your views here.

def insurance(request):
        insurance_form=InsuranceForm(request.POST or None)
        context={
            "insurance_form":insurance_form
        }
        if insurance_form.is_valid():
            print(insurance_form.cleaned_data)
            context['insurance_form']=InsuranceForm()
            return redirect("/#policy")

        return render(request,'insurance/insurance.html',context)

def policy(request):
        policy_form=PolicyForm(request.POST or None)
        context={
                "policy_form":policy_form
            }
        print("hai")
        if policy_form.is_valid():
            print("hai1")
            print(policy_form.cleaned_data)
            context['policy_form']=PolicyForm()
            return redirect("insurance")
        return render(request,'policy/policy_register.html',context)        