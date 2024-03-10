from django.http import HttpResponse
from django.shortcuts import render
from providerapp.models import Services,Hotel

"""
def demofn(request):
    return HttpResponse("TOuRISM and hospitality management system")

def demofn1(request):
    return HttpResponse("<font color = 'blue'>TOuRISM and hospitality management system<font>")
"""


def adminhomefn(request):
    return render(request, "overallhome.html")

def mainhomefn(request):
    return render(request,"overallhome.html")


def indexfn(request):
    return render(request, "index.html")


def loginfn(request):
    return render(request, "login.html")


def reservationsfn(request):
    return render(request, "reservations.html")


def servicesfn(request):
    c = Services.objects.all()
    count = Services.objects.count()
    return render(request, "services.html",{"c":c})


def feedbackfn(request):
    return render(request, "feedback.html")

def adminlogoutfn(request):
    return render(request, "login.html")

def hotelhomefn(request):
    return render(request, "provlogin.html")


def userhomefn(request):
    return render(request, "userlogin.html")

def aboutsitefn(request):
    return render(request,"about.html")

def contactusfn(request):
    return render(request,"contactus.html")


# Create your views here.
