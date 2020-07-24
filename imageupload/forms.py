from django.forms import ModelForm
from django import forms 
from .models import *

class ImageForm(forms.ModelForm): 
    image_upload=forms.ImageField(
        label='',
        widget=forms.ClearableFileInput(
           attrs={
               "class":"custom-file-input",
               "id":"customFile",
           }
       )
    )
    class Meta: 
        model = ImageUploading 
        fields = ['image_upload']