from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('team', views.team, name='team'),
    path('forms', views.forms, name='forms'),
    path('mmis', views.mmis, name='mmis'),
    path('testpage', views.testpage),
]
