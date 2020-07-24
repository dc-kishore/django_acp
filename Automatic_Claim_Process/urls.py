"""Automatic_Claim_Process URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from Damage_assesment.views import index,register_page,about
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings 
from django.conf.urls.static import static 
from Policy.views import insurance,policy
from imageupload.views import image_upload,image_display
from checkout.views import checkout,logout_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name="home"),
    path('register/',register_page,name='register'),
    path('upload/',image_upload,name="image"),
    path('image/',image_display,name="table"),
    path('checkout/',checkout,name='checkout'),
    path('insurance/',insurance,name='insurance'),
    path('estimate/',include("Damage_assesment.urls"),name="estimate"),
    path('logout/', logout_view, name='logout'),
    path('policy/',policy,name="policy"),
    

]
urlpatterns+= staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,
                               document_root=settings.MEDIA_ROOT)