from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from App.serializer import CategorySerializer, BrandSerializer, ProductSerializer, SupplierSerializer, CustomerSerializer, SupplierInvoiceSerializer, SupplierBillSerializer, CustomerBillSerializer, CustomerInvoiceSerializer, UserSerializer
from App.models import Category, Brand, Product, Supplier, Customer, SupplierInvoice, SupplierBill, CustomerInvoice, CustomerBill, SystemUser
# from rest_framework.authtoken.models import Token
# from django.contrib.auth import authenticate
# from rest_framework.response import Response
# from rest_framework import status
# from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

# Create your views here.


# developer id = chathura prasanga
# date = 09/14/2023
# create end point to get all categories, get details, update details and delete categories
# functions = get all categoris/ serialize them / return json (in post method these steps are reverse)
# (all the two functions are run by same function)
@api_view(['GET','POST','PUT','DELETE'])
@csrf_exempt
def categoryApi(request,id=0):
    if request.method=='GET':
        category = Category.objects.all()
        categorySerializer=CategorySerializer(category,many=True)
        return JsonResponse(categorySerializer.data,safe=False)
    
    elif request.method=='POST':
        category_data=JSONParser().parse(request)
        category_serializer=CategorySerializer(data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        category_data=JSONParser().parse(request)
        category = Category.objects.get(id=id)
        category_serializer = CategorySerializer(category, data = category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
        category = Category.objects.get(id=id)        
        category.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    

# developer id = chathura prasanga
# date = 09/14/2023
# create end point to dashboard functions
# functions = count categoris/ serialize them / return json (in post method these steps are reverse)
# (all table may countn)
# update date = 15/09 add product count
def dashboardApi(request):
    categoryCount = Category.objects.count()
    brandCount = Brand.objects.count()
    productCount = Product.objects.count()
    supplierCount = Supplier.objects.count()
    customerCount = Customer.objects.count()
    supplierInvoiceCount = SupplierInvoice.objects.count()
    supplierBillCount = SupplierBill.objects.count()
    customerInvoicecount = CustomerInvoice.objects.count()
    customerBillCount = CustomerBill.objects.count()


    return JsonResponse({
        "categoryCount":categoryCount,
        "brandCount":brandCount,
        "productCount":productCount,
        "supplierCount":supplierCount,
        "customerCount":customerCount,
        "supplierInvoiceCount":supplierInvoiceCount,
        "supplierBillCount":supplierBillCount,
        "customerInvoiceCount":customerInvoicecount,
        "customerBillCount":customerBillCount,
        }, safe=False)


# developer id = chathura prasanga
# date = 09/14/2023
# create end point to get all brands, get details, update details and delete brands
# functions = get all brands/ serialize them / return json (in post method these steps are reverse)
# (all the two functions are run by same function)
@api_view(['GET','POST','PUT','DELETE'])
@csrf_exempt
def brandApi(request,id=0):
    if request.method=='GET':
        brand = Brand.objects.all()
        brand_serializer=BrandSerializer(brand,many=True)
        return JsonResponse(brand_serializer.data,safe=False)
    
    elif request.method=='POST':
        brand_data=JSONParser().parse(request)
        brand_serializer=BrandSerializer(data=brand_data)
        if brand_serializer.is_valid():
            brand_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        brand_data=JSONParser().parse(request)
        brand = Brand.objects.get(id=id)
        brand_serializer = BrandSerializer(brand, data = brand_data)
        if brand_serializer.is_valid():
            brand_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
        brand = Brand.objects.get(id=id)        
        brand.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    
    
# developer id = chathura prasanga
# date = 09/15/2023
# create end point to get all product, get details, update details and delete product
# functions = get all product/ serialize them / return json (in post method these steps are reverse)
# (all the two functions are run by same function)
@api_view(['GET','POST','PUT','DELETE'])
@csrf_exempt
def productApi(request,id=0):
    if request.method=='GET':
        product = Product.objects.all()
        product_serializer=ProductSerializer(product,many=True)
        return JsonResponse(product_serializer.data,safe=False)
    
    elif request.method=='POST':
        product_data=JSONParser().parse(request)
        product_serializer=ProductSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        product_data=JSONParser().parse(request)
        product = Product.objects.get(id=id)
        product_serializer = ProductSerializer(product, data = product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
        product = Product.objects.get(id=id)        
        product.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    


# developer id = chathura prasanga
# date = 09/15/2023
# create end point to get all supplier, get details, update details and delete supplier
# functions = get all supplier/ serialize them / return json (in post method these steps are reverse)
# (all the two functions are run by same function)
@api_view(['GET','POST','PUT','DELETE'])
@csrf_exempt
def supplierApi(request,id=0):
    if request.method=='GET':
        supplier = Supplier.objects.all()
        supplier_serializer=SupplierSerializer(supplier,many=True)
        return JsonResponse(supplier_serializer.data,safe=False)
    
    elif request.method=='POST':
        supplier_data=JSONParser().parse(request)
        supplier_serializer=SupplierSerializer(data=supplier_data)
        if supplier_serializer.is_valid():
            supplier_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        supplier_data=JSONParser().parse(request)
        supplier = Supplier.objects.get(id=id)
        supplier_serializer = SupplierSerializer(supplier, data = supplier_data)
        if supplier_serializer.is_valid():
            supplier_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
        supplier = Supplier.objects.get(id=id)        
        supplier.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    


# developer id = chathura prasanga
# date = 09/15/2023
# create end point to get all customer, get details, update details and delete customer
# functions = get all customer/ serialize them / return json (in post method these steps are reverse)
# (all the two functions are run by same function)
@api_view(['GET','POST','PUT','DELETE'])
@csrf_exempt
def customerApi(request,id=0):
    if request.method=='GET':
        customer = Customer.objects.all()
        customer_serializer=CustomerSerializer(customer,many=True)
        return JsonResponse(customer_serializer.data,safe=False)
    
    elif request.method=='POST':
        customer_data=JSONParser().parse(request)
        customer_serializer=CustomerSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        customer_data=JSONParser().parse(request)
        customer = Customer.objects.get(id=id)
        customer_serializer = CustomerSerializer(customer, data = customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
        customer = Customer.objects.get(id=id)        
        customer.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    

# developer id = chathura prasanga
# date = 09/16/2023
# create end point to get all supplier_invoice, get details, update details and delete supplier_invoice
# functions = get all supplier_invoice/ serialize them / return json (in post method these steps are reverse)
# (all the two functions are run by same function)
@api_view(['GET','POST','PUT','DELETE'])
@csrf_exempt
def supplierInvoiceApi(request,id=0):
    if request.method=='GET':
        supplier_invoice = SupplierInvoice.objects.all()
        supplier_invoice_serializer=SupplierInvoiceSerializer(supplier_invoice,many=True)
        return JsonResponse(supplier_invoice_serializer.data,safe=False)
    
    elif request.method=='POST':
        supplier_invoice_data=JSONParser().parse(request)
        supplier_invoice_serializer=SupplierInvoiceSerializer(data=supplier_invoice_data)
        if supplier_invoice_serializer.is_valid():
            supplier_invoice_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        supplier_invoice_data=JSONParser().parse(request)
        supplier_invoice = SupplierInvoice.objects.get(id=id)
        supplier_invoice_serializer = SupplierInvoiceSerializer(supplier_invoice, data = supplier_invoice_data)
        if supplier_invoice_serializer.is_valid():
            supplier_invoice_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
        supplier_invoice = SupplierInvoice.objects.get(id=id)        
        supplier_invoice.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    

# developer id = chathura prasanga
# date = 09/16/2023
# create end point to get all supplierBill, get details, update details and delete supplierBill
# functions = get all supplierBill/ serialize them / return json (in post method these steps are reverse)
# (all the two functions are run by same function)
@api_view(['GET','POST','PUT','DELETE'])
@csrf_exempt
def supplierBillApi(request,id=0):
    if request.method=='GET':
        supplier_bill = SupplierBill.objects.all()
        supplier_bill_serializer=SupplierBillSerializer(supplier_bill,many=True)
        return JsonResponse(supplier_bill_serializer.data,safe=False)
    
    elif request.method=='POST':
        supplier_bill_data=JSONParser().parse(request)
        supplier_bill_serializer=SupplierBillSerializer(data=supplier_bill_data)
        if supplier_bill_serializer.is_valid():
            supplier_bill_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        supplier_bill_data=JSONParser().parse(request)
        supplier_bill = SupplierBill.objects.get(id=id)
        supplier_bill_serializer = SupplierBillSerializer(supplier_bill, data = supplier_bill_data)
        if supplier_bill_serializer.is_valid():
            supplier_bill_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
        supplier_bill = SupplierBill.objects.get(id=id)        
        supplier_bill.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    


# developer id = chathura prasanga
# date = 09/16/2023
# create end point to get all customer invoice, get details, update details and delete customer invoice
# functions = get all customer invoice/ serialize them / return json (in post method these steps are reverse)
# (all the two functions are run by same function)
@api_view(['GET','POST','PUT','DELETE'])
@csrf_exempt
def customerInvoiceApi(request,id=0):
    if request.method=='GET':
        customer_invoice = Customer.objects.all()
        customer_invoice_serializer=CustomerInvoiceSerializer(customer_invoice,many=True)
        return JsonResponse(customer_invoice_serializer.data,safe=False)
    
    elif request.method=='POST':
        customer_invoice_data=JSONParser().parse(request)
        customer_invoice_serializer=CustomerInvoiceSerializer(data=customer_invoice_data)
        if customer_invoice_serializer.is_valid():
            customer_invoice_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        customer_invoice_data=JSONParser().parse(request)
        customer_invoice = CustomerInvoice.objects.get(id=id)
        customer_invoice_serializer = CustomerInvoiceSerializer(customer_invoice, data = customer_invoice_data)
        if customer_invoice_serializer.is_valid():
            customer_invoice_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
        customer_invoice = CustomerBill.objects.get(id=id)        
        customer_invoice.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    


# developer id = chathura prasanga
# date = 09/16/2023
# create end point to get all customer bill, get details, update details and delete customer bill
# functions = get all customer bill/ serialize them / return json (in post method these steps are reverse)
# (all the two functions are run by same function)
@api_view(['GET','POST','PUT','DELETE'])
@csrf_exempt
def customerBillApi(request,id=0):
    if request.method=='GET':
        customer_bill = CustomerBill.objects.all()
        customer_bill_serializer=CustomerBillSerializer(customer_bill,many=True)
        return JsonResponse(customer_bill_serializer.data,safe=False)
    
    elif request.method=='POST':
        customer_bill_data=JSONParser().parse(request)
        customer_bill_serializer=CustomerBillSerializer(data=customer_bill_data)
        if customer_bill_serializer.is_valid():
            customer_bill_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    elif request.method=='PUT':
        customer_bill_data=JSONParser().parse(request)
        customer_bill = CustomerInvoice.objects.get(id=id)
        customer_bill_serializer = CustomerBillSerializer(customer_bill, data = customer_bill_data)
        if customer_bill_serializer.is_valid():
            customer_bill_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method=='DELETE':
        customer_bill = CustomerBill.objects.get(id=id)        
        customer_bill.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = SystemUser.objects.all()
