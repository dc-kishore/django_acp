from django.shortcuts import render

# Create your views here.
def image_upload(request):
    return render(request,'image/image_upload1.html',{})