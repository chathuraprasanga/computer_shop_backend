from rest_framework import serializers
from .models import Category, Brand, Product, Supplier, Customer, SupplierInvoice, CustomerInvoice, SupplierBill, CustomerBill, SystemUser


# developer id = chathura prasanga
# date = 09/14/2023
# serialize model to connect through api
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'created_at', 'brand_name', 'brand_description', 'brand_country', 'brand_status']


# developer id = chathura prasanga
# date = 09/14/2023
# serialize model to connect through api
class CategorySerializer(serializers.ModelSerializer):

    # functions for show names 
    brand_names = BrandSerializer(source='category_brands', required=False, many= True)

    class Meta:
        model = Category
        fields = ['id', 'created_at','category_name','category_description', 'brand_names', 'category_status']


# developer id = chathura prasanga
# date = 09/15/2023
# serialize model to connect through api
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


# developer id = chathura prasanga
# date = 09/15/2023
# serialize model to connect through api
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


# developer id = chathura prasanga
# date = 09/15/2023
# serialize model to connect through api
class ProductSerializer(serializers.ModelSerializer):

    # functions for show names 
    brand_name = BrandSerializer(source='product_brand', required=False, many = False)
    category_name = CategorySerializer(source='product_category', required = False, many = False  )
    supplier_company = SupplierSerializer(source='product_supplier', required=False, many = False)

    class Meta:
        model = Product
        fields = ['id', 'created_at','product_name','brand_name', 'category_name','supplier_company', 'product_buying_price', 'product_selling_price', 'product_status']


# developer id = chathura prasanga
# date = 09/15/2023
# serialize model to connect through api
class SupplierInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierInvoice
        fields = '__all__'


# developer id = chathura prasanga
# date = 09/15/2023
# serialize model to connect through api
class CustomerInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInvoice
        fields = '__all__'


# developer id = chathura prasanga
# date = 09/15/2023
# serialize model to connect through api
class SupplierBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierBill
        fields = '__all__'

# developer id = chathura prasanga
# date = 09/15/2023
# serialize model to connect through api
class CustomerBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerBill
        fields = '__all__'


# developer id = chathura prasanga
# date = 09/15/2023
# serialize model to connect through api
class SystemUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemUser
        fields = '__all__'



