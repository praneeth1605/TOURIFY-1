from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from providerapp.models import Services,Hotel, Places, ProvPlaces,Hotel,Register,Provservices
from .models import TouristRegister,Tourist,Userfeedback




"""
def demofn(request):
    return HttpResponse("TOuRISM and hospitality management system")

def demofn1(request):
    return HttpResponse("<font color = 'blue'>TOuRISM and hospitality management system<font>")
"""

def mainhomefn(request):
    return render(request,"overallhome.html")
def userindexfn(request):
    return render(request, "index3.html")

def userhomefn(request):
    return render(request, "userhome.html")


def userloginfn(request):
    return render(request, "userlogin.html")


def userregisterfn(request):
    return render(request, "userRegister.html")

def bookingsuccessfn(request):
    return render(request, "booksuccess.html")


def userBookroomsfn(request):
    return render(request, "BookRooms.html")


def touristviewplacesfn(request):
    return render(request, "touristviewPlaces.html")

def userfeedbackfn(request):
    return render(request,'userfeedback.html')


def userlogoutfn(request):
    return render(request, "userlogin.html")



def registertouristfn(request):
    if request.method == "POST":
        first_name = request.POST.get("Firstname", "")
        last_name = request.POST.get("LastName", "")
        age = request.POST.get("Age", "")
        gender = request.POST.get("Gender", "")
        dob = request.POST.get("dob", "")
        email = request.POST.get("Email", "")
        mobile_number = request.POST.get("Mobile", "")
        address = request.POST.get("address", "")
        country = request.POST.get("country", "")
        state = request.POST.get("state", "")
        city = request.POST.get("City", "")
        postal_code = request.POST.get("postal_code", "")
        username = request.POST.get("Username", "")
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm", "")
        # Your existing code to retrieve form data

        # Check if passwords match
        if password != confirm_password:
            message = "Passwords do not match. Please re-enter."
        # Check password conditions
        elif len(password) < 8 or not (any(c.isalpha() for c in password) and any(c.isdigit() for c in password)):
            message = "Invalid password. Password must be 8 characters or more and contain alphabets, numbers, and special characters."
        else:
            # Save data to the database
            touristregister = TouristRegister(
                first_name=first_name,
                last_name=last_name,
                age=age,
                gender=gender,
                dob=dob,
                email=email,
                mobile_number=mobile_number,
                address=address,
                country=country,
                state=state,
                City=city,
                postal_code=postal_code,
                username=username,
                password=password,
                confirmpassword=confirm_password
            )
            touristregister.save()

            tourist = Tourist(username=username, password=password)
            tourist.save()

            message = "Tourist registration successful"
            return render(request, "userlogin.html", {"msg": message})

    else:
        message = "Please enter valid credentials"
        return render(request, "userRegister.html", {"msg": message})

    return render(request, "userRegister.html", {"msg": message})




def checkuserloginfn(request):
    uname = request.POST.get('username', '')  # Use request.GET to access GET data
    provpwd = request.POST.get('password', '')

    flag = Tourist.objects.filter(Q(username=uname) & Q(password=provpwd))
    print(flag)

    if flag:
        message = "Login Succesful"
        return render(request, "userhome.html", {"msg": message})

    else:
        message = "Invalid Username or password"
        return render(request, "userlogin.html", {"msg": message})


    return render(request, "userRegister.html", {"msg": message})


def viewplacesfn(request):
    p = ProvPlaces.objects.all()
    count = ProvPlaces.objects.count()
    return render(request, "touristviewPlaces.html", {"p": p})

def bookroomsfn(request):
    c = Provservices.objects.all()
    count = Provservices.objects.count()
    return render(request, "BookRooms.html", {"c": c})


def registeruserfeedback(request):
    if request.method == 'POST':
        # Create a form instance (if you have a form)
        # form = YourFormName(request.POST)

        # Check if the form is valid (if you have a form)
        # if form.is_valid():
            # You can access the form fields and save them to the database
            hotel = request.POST.get('Hotel')
            state = request.POST.get('State')
            city = request.POST.get('City')
            cleanliness = request.POST.get('cleanliness')
            service = request.POST.get('service')
            comfort = request.POST.get('comfort')
            amenities = request.POST.get('amenities')
            location = request.POST.get('location')
            value = request.POST.get('value')
            comments = request.POST.get('comments')

            # Create and save a new Userfeedback instance
            user_feedback = Userfeedback(
                Hotel=hotel,
                State=state,
                City=city,
                cleanliness=cleanliness,
                service=service,
                comfort=comfort,
                amenities=amenities,
                location=location,
                value=value,
                comments=comments
            )
            user_feedback.save()

    message = "Feedback Saved Successfully"
    return render(request, "userfeedback.html", {"msg": message})



            # You can also save the form instance if you are using a form
            # form.save()








