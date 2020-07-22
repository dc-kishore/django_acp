from django import forms
from django.contrib.auth import get_user_model


User=get_user_model()

class LoginForm(forms.Form):
    username=forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Your Username",
            }
        ))
    password=forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"your password"
            }
        )
    )

class RegisterForm(forms.Form):
    username=forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Your Username",
            }
        ))
    Email=forms.EmailField(
        label='',
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Email",
            }
        )
    )
    password=forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"your password"
            }
        ))    
    password1=forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Confirm password"
            }
        ))

    def clean_username(self):
        username=self.cleaned_data.get('username')
        qs=User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username
    
    def clean(self):
        data=self.cleaned_data
        password=self.cleaned_data.get("password")
        password1=self.cleaned_data.get("password1")
        if password1 != password:
            raise forms.ValidationError("Passwords must match")
        return data
    
    def clean_email(self):
        email=self.cleaned_data.get('Email')
        try:
            match=User.objects.get(email=email)
        except:
            return email
        raise forms.ValidationError("email is taken")


