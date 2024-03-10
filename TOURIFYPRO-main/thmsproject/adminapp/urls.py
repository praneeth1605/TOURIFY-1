"""
URL configuration for thmsproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.adminhomefn, name=""),
    # path('demo', views.demofn, name='demo'),
    # path('demo1', views.demofn1, name='demo1'),
    # path('adminhome', views.adminhomefn, name="home"),
    path('mainhome',views.mainhomefn,name="mainhome"),
    path('', views.indexfn, name="index"),
    path('login', views.loginfn, name="login"),
    path('reservations', views.reservationsfn, name="reservations"),
    path('services', views.servicesfn, name="services"),
    path('feedback', views.feedbackfn, name="feedback"),
    path("logout", views.adminlogoutfn, name="logout"),
    path("hotel", views.hotelhomefn, name="hotel"),
    path("user", views.userhomefn, name="user"),
    path("about", views.aboutsitefn, name="about"),
    path("contactus", views.contactusfn, name="contactus")

]
