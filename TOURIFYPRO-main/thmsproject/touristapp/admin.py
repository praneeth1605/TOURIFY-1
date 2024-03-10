from django.contrib import admin

# Register your models here.


# Register your models here.


from .models import Tourist,TouristRegister,Userfeedback
# Register your models here.

admin.site.register(Tourist)
admin.site.register(TouristRegister)
admin.site.register(Userfeedback)

