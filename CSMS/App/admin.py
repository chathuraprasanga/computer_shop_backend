from django.contrib import admin
from . models import Category, Brand, Product, Supplier, Customer, SupplierInvoice,SupplierBill,CustomerInvoice, CustomerBill
# Register your models here.

# developer id = chathura prasanga
# date = 09/14/2023
# customize api interface
admin.site.site_header = "CSMS API"
admin.site.site_title = "CSMS API"

# developer id = chathura prasanga
# date = 09/14/2023
# register model to api
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(SupplierInvoice)
admin.site.register(SupplierBill)
admin.site.register(CustomerInvoice)
admin.site.register(CustomerBill)