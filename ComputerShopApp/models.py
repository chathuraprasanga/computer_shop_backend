from django.db import models

# Create your models here.


# creating user model
class User(models.Model):
    USERROLE = (
        ('Admin', 'Admin'),  # admin role
        ("User", "User"),   # normal user role
    )
    username = models.CharField( max_length=20)
    password = models.CharField( max_length=20)
    # userRole = models.CharField(choices=USERROLE)
