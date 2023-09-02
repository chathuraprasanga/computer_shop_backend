from django.db import models

# Create your models here.

# choices for status
STATUS_CHOICES =[
    ("ACTIVE","ACTIVE"),("DECATIVE","DEACTIVE")
]
   

# buyer model
class Buyer(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    organization_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    user_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="ACTIVE")

    def __str__(self):
        return(f"{self.first_name},{self.last_name},{self.organization_name}")