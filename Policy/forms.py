from django.forms import ModelForm
from django import forms
from django.contrib.auth import get_user_model
from .models import Policy,Insurance

User=get_user_model()
class PolicyForm(ModelForm):
    policy_choices=(
        ("Motor Insurance","Motor Insurance"),
        ("Other","Other")
    )
    Firstname=forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Firstname",
            }
        )
        )
    Lastname=forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Lastname",
            }
        )
        )    
    Email=forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Email",
            }
        )
    )
    Insurance_type=forms.ChoiceField(
        label='',
        choices=policy_choices,
        widget=
            forms.Select(
                attrs={
                    "class":"form-control",
                        })
    )
    Address=forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Address",
            }
        )
       
    )
    
    Phone=forms.CharField(
        label='',
        widget=forms.NumberInput(
            attrs={
                "class":"form-control",
                "placeholder":"Phone number",
            }
        )
    )
    
    def clean_email(self):
        email=self.cleaned_data.get('Email')
        try:
            match=User.objects.get(email=email)
        except:
            return email
        raise forms.ValidationError("email is taken")
    
    class Meta:
        model=Policy
        fields=('Firstname','Lastname','Email','Insurance_type','Address','Phone')

class InsuranceForm(ModelForm):
    Email=forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Email",
            }
        )
    )
    
    Price=forms.CharField(
        label='',
        widget=forms.NumberInput(
            attrs={
                "class":"form-control",
                "placeholder":"Price",
            }
        ),
        
    )

    Estimated_amount=forms.CharField(
        label='',
        widget=forms.NumberInput(
            attrs={
                "class":"form-control",
                "placeholder":"Estimated amount",
            }
        )
     
    )

    class Meta:
        model=Insurance
        fields=('Email','Price','Estimated_amount')