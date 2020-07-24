from django.shortcuts import render,redirect
from .forms import ImageForm
from .models import ImageUploading
# Create your views here.



def image_upload(request):
    if request.method=='POST':
        image_form=ImageForm(request.POST, request.FILES)
        context={
            "image_form":image_form
        }
        if image_form.is_valid():
            image_form.save()
            img_obj=image_form.instance
            print(image_form.cleaned_data)
            return redirect('table')
            return render(request,'image/image_upload1.html',{"image_form":image_form,"img_obj":img_obj})
        else:
            image_form=ImageForm()
        return render(request,'image/image_upload1.html',context)

def image_display(request):
    if request.method=='GET':
        Image=ImageUploading.objects.all()
        return render(request, 'image_display/image_display.html',{'Images' : Image})