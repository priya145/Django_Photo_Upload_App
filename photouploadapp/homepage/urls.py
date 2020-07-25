from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from homepage import views as user_views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

path('index/', user_views.mainhome, name="mainhome"),
path('model_form_upload/',user_views.model_form_upload,name="upload")



]



