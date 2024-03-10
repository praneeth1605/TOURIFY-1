from django.db import models

# Create your models here.
from django.db import models

class Tourist(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=20, blank=False)

    class Meta:
        db_table = 'Tourist_table'

    def __str__(self):
        return self.username


class TouristRegister(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255, blank=False)
    country = models.CharField(max_length=255, blank=False)
    state = models.CharField(max_length=255, blank=False)
    City = models.CharField(max_length=255, blank=False)
    postal_code = models.CharField(max_length=10, blank=False)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100,blank=False)
    confirmpassword = models.CharField(max_length=100,blank=False)


    class Meta:
        db_table = 'TouristRegister_table'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Userfeedback(models.Model):
    Hotel = models.CharField(max_length=100, blank=False)
    State = models.CharField(max_length=100, blank=False)
    City = models.CharField(max_length=100, blank=False)
    cleanliness = models.CharField(max_length=100, blank=False)
    service = models.CharField(max_length=100, blank=False)
    comfort = models.CharField(max_length=100, blank=False)
    amenities = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=100, blank=False)
    value = models.CharField(max_length=100, blank=False)
    comments = models.TextField()

    class Meta:
        db_table = 'Feedback_table'

    def __str__(self):
        return self.Hotel