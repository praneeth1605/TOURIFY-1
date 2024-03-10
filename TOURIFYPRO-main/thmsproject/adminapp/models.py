from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Admin(models.Model):
    id = models.AutoField(primary_key="True")
    username = models.CharField(max_length=100,blank=False,unique=True)
    password = models.CharField(max_length=100,blank=False)

    class Meta:
        db_table = 'Admin_table'

