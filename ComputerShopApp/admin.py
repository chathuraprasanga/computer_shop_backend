from django.contrib import admin
from .models import Buyer,Category,Seller

# Register your models here.
admin.site.register(Buyer)
admin.site.register(Category)
admin.site.register(Seller)