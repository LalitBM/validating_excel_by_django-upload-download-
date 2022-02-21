
from unicodedata import name
from django.urls import path
from app1 import views

urlpatterns = [
    path('up/',views.upload_check,name="up"),
]
