from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.

STATUS_CHOICE = [
    ("ACTIVE","ACTIVE"),
    ("DEACTIVE","DEACTIVE")
]

PAYMENT_METHOD = [
    ("CASH","CASH"),
    ("CHQ","CHQ"),
    ("CREDIT","CREDIT")
]

PAYMENT_STATUS = [
    ("PAID","PAID"),
    ("NOT PAID","NOT PAID")
]


# developer id = chathura prasanga
# date = 09/14/2023
# create model to api Brand
class Brand(models.Model):
    created_at = models.DateField(auto_now_add=True)
    brand_name = models.CharField(max_length=255)
    brand_description = models.TextField(max_length=255)
    brand_country = models.CharField(max_length=255,null=True, blank=True )
    brand_status = models.CharField(max_length=8, choices=STATUS_CHOICE, default="DEACTIVE")

    def __str__(self):
        return self.brand_name

# developer id = chathura prasanga
# date = 09/14/2023
# create model to api Category
class Category(models.Model):
    created_at = models.DateField(auto_now_add=True)
    category_name = models.CharField(max_length=255)
    category_description = models.TextField(max_length=255)
    category_brands = models.ManyToManyField(Brand)
    category_status = models.CharField(max_length=8, choices=STATUS_CHOICE, default="DEACTIVE")

    def __str__(self):
        return self.category_name
    
    
# developer id = chathura prasanga
# date = 09/16/2023
# create model to api Supplier
class Supplier(models.Model):
    created_at = models.DateField(auto_now_add=True)
    supplier_name = models.CharField(max_length=255, unique=True)
    supplier_company = models.CharField(max_length=255)
    supplier_phone = models.CharField(max_length=10)
    supplier_email = models.CharField(max_length=255)
    supplier_address = models.TextField(max_length=255)
    supplier_status = models.CharField(max_length=8, choices=STATUS_CHOICE, default="DEACTIVE")

    def __str__(self):
        return self.supplier_company
    


# developer id = chathura prasanga
# date = 09/16/2023
# create model to api Customer
class Customer(models.Model):
    created_at = models.TimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=10)
    customer_email = models.CharField(max_length=255, null=True, blank=True)
    customer_address = models.TextField(max_length=255, null=True, blank=True)
    customer_status = models.CharField(max_length=8, choices=STATUS_CHOICE, default="DEACTIVE")

    def __str__(self):
        return self.customer_name


# developer id = chathura prasanga
# date = 09/15/2023
# create model to api Product
# updated date = 16/09 add supplier 
class Product(models.Model):
    created_at = models.TimeField(auto_now_add=True)
    product_name = models.CharField(max_length=255)
    product_brand = models.ForeignKey(Brand, on_delete=models.CASCADE, )
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, )
    product_supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE, )
    product_buying_price = models.PositiveIntegerField()
    product_selling_price = models.PositiveIntegerField()
    product_status = models.CharField(max_length=8, choices=STATUS_CHOICE, default="DEACTIVE")

    def __str__(self):
        return self.product_name
    

# developer id = chathura prasanga
# date = 09/16/2023
# create model to api supplier invoice
class SupplierInvoice(models.Model):
    created_at = models.DateField(auto_now_add=True)
    # supplier_name = models.ForeignKey(Supplier, on_delete=models.CASCADE) #this will use in suppplier bill model
    product_details = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quantity = models.PositiveIntegerField()
    product_unit_price = models.PositiveIntegerField()
    product_total_price = models.PositiveIntegerField()

    def __Str__(self):
        return self.id+' \t'+self.created_at+' \t'+' \t'+self.product_details+' \t'+self.product_quantity+' \t'+self.product_unit_price+' \t'+self.product_total_price
    

# developer id = chathura prasanga
# date = 09/16/2023
# create model to api supplier bill
class SupplierBill(models.Model):
    created_at = models.DateField(auto_now_add=True)
    supplier_details = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    invoices = models.ManyToManyField(SupplierInvoice)
    sub_total = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(null=True,blank=True)
    net_total = models.PositiveIntegerField()
    payment_method = models.CharField(max_length=6,choices=PAYMENT_METHOD, default="CREDIT")
    payment_status = models.CharField(max_length=8, choices=PAYMENT_STATUS, default="NOT PAID" )

    def __str__(self):
        return self.created_at+' \t'+self.supplier_details+' \t'+self.invoices+' \t'+self.sub_total+' \t'+self.discount+' \t'+self.net_total+' \t'+self.payment_method+' \t'+self.payment_status


# developer id = chathura prasanga
# date = 09/16/2023
# create model to api Customer invoice
class CustomerInvoice(models.Model):
    created_at = models.DateField(auto_now_add=True)
    product_details = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quantity = models.PositiveIntegerField()
    product_unit_price = models.PositiveIntegerField()
    product_total_price = models.PositiveIntegerField()

    def __Str__(self):
        return self.id+' \t'+self.created_at+' \t'+' \t'+self.product_details+' \t'+self.product_quantity+' \t'+self.product_unit_price+' \t'+self.product_total_price


# developer id = chathura prasanga
# date = 09/16/2023
# create model to api customer bill
class CustomerBill(models.Model):
    created_at = models.DateField(auto_now_add=True)
    customer_details = models.ForeignKey(Customer, on_delete=models.CASCADE)
    invoices = models.ManyToManyField(CustomerInvoice)
    sub_total = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(null=True,blank=True)
    net_total = models.PositiveIntegerField()
    payment_method = models.CharField(max_length=6,choices=PAYMENT_METHOD, default="CREDIT")
    payment_status = models.CharField(max_length=8, choices=PAYMENT_STATUS, default="NOT PAID" )

    def __str__(self):
        return self.created_at+' \t'+self.customer_details+' \t'+self.invoices+' \t'+self.sub_total+' \t'+self.discount+' \t'+self.net_total+' \t'+self.payment_method+' \t'+self.payment_status

    
# developer id = chathura prasanga
# date = 09/17/2023
# create model to api user
class SystemUser(models.Model):

    USER_TYPE = [
        ("ADMIN","ADMIN"),
        ("USER","USER")
    ]

    created_at = models.DateField(auto_now_add=True)
    system_user_first_name = models.CharField(max_length=255)
    system_user_last_name = models.CharField(max_length=255)
    system_user_username = models.CharField(max_length=255, unique=True)
    system_user_phone = models.CharField(max_length=10)
    system_user_email = models.CharField(max_length=255, unique=True)
    system_user_nic_number = models.CharField(max_length=20)
    system_user_password = models.CharField(max_length=255)
    system_user_type = models.CharField(max_length=5, choices=USER_TYPE, default="USER")
    system_user_status =  models.CharField(max_length=8, choices=STATUS_CHOICE, default="DEACTIVE")

    def __str__(self):
        return self.system_user_user_name

