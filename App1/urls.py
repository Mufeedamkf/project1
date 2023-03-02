from django.urls import path
from . import views

app_name='App1'

urlpatterns=[
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    
]