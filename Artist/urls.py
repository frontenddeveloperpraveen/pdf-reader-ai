from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
path('',v.Home,name='home'),
path('upload',v.Upload,name='Upload')
]
