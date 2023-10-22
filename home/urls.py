from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path("", views.index, name='home'),
   path("about", views.about, name='about'),
   path("services", views.services, name='services'),
   path("contact", views.contact, name='contact'),
   path("Clock", views.Clock, name='Clock'),
   path("To_Do_List", views.To_Do_List, name='To_Do_List'),
]
