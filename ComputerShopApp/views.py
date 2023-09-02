from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout #adding for user loging authenticate
from django.contrib import messages #for sent frontend messages
from .forms import SignUpForm, BuyerAddForm, CategoryAddForm, SellerAddForm
from .models import Buyer, Category, Seller

# Create your views here.

# when frontend request home
def home(request):
    return render(request, 'home.html',{})

#login user function
def login_user(request):
    # check if to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # ?authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Successfully Logged In.!")
            return redirect('dashboard')
        else :
            messages.error(request,"There Was a Error In Login.!")
            return redirect('login')
    else:
        return render(request, 'login.html',{})

#logout user function
def logout_user(request):
    logout(request)
    messages.success(request, "You Have Successfully Loged Out.!")
    return redirect('home')

# register user function
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate( username=username,password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Logged In.!")
            return redirect('home')
    else:
         form = SignUpForm()
         return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})

# dashboard function
def dashboard(request):
    return render(request, 'dashboard.html', {})

# buyers page functions
def buyers(request):
    buyers = Buyer.objects.all()
    return render(request, 'buyers.html', {'buyers':buyers})

# buyers details functions
def buyer_details(request, pk):
    if request.user.is_authenticated:
        # look up buyers
        buyer_detail = Buyer.objects.get(id=pk)
        return render(request, 'buyer_details.html', {'buyer_detail':buyer_detail})
    else:
        messages.success("Something Went Wrong.!")
        buyers = Buyer.objects.all()
        return render(request, 'buyers.html', {'buyers':buyers})

# delete buyer function
def buyer_delete(request,pk):
    if request.user.is_authenticated:
        delete_it = Buyer.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Buyer Deleted Successfully.!")
        return redirect ('buyers') 
    else:
        messages.success(request, "Something Went Wrong.!")
        return redirect ('buyers')
    
# add buyer function
def buyer_add(request):
    form = BuyerAddForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                buyer_add = form.save()
                messages.success(request, "Buyer Added Successfully.!")
                return redirect( 'buyers' )
        return render(request, 'buyer_add.html', {"form":form,"title":"add"})
    else:
        messages.success(request, "Something Went Wrong.!")
        return redirect ('buyers')
    
# Buyer Update function 
def buyer_update(requset, pk):
    if requset.user.is_authenticated:
        update_it = Buyer.objects.get(id=pk)
        form = BuyerAddForm(requset.POST or None, instance=update_it)
        if form.is_valid():
            form.save()
            messages.success(requset, "Buyer Updated Successfully.!")
            return redirect( 'buyers' )
        return render(requset, 'buyer_update.html', {"form":form,"title":"update"})
    else:
        messages.success(requset, "Something Went Wrong.!")
        return redirect ('buyers')
    
# Category Part Starts from here

# categories page view
def categories(request):
    categories = Category.objects.all()
    return render (request, 'categories.html', {'categories':categories})

# add category function
def category_add(request):
    form = CategoryAddForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                category_add = form.save()
                messages.success(request, "Category Added Successfully.!")
                return redirect( 'categories' )
        return render(request, 'category_add.html', {"form":form,})
    else:
        messages.success(request, "Something Went Wrong.!")
        return redirect ('categories')
    

# category details functions
def category_details(request, pk):
    if request.user.is_authenticated:
        # look up buyers
        category_detail = Category.objects.get(id=pk)
        return render(request, 'category_details.html', {'category_detail':category_detail})
    else:
        messages.success("Something Went Wrong.!")
        categories = Category.objects.all()
        return render(request, 'categories.html', {'categories':categories})
    
# Category Update function 
def category_update(requset, pk):
    if requset.user.is_authenticated:
        update_it = Category.objects.get(id=pk)
        form = CategoryAddForm(requset.POST or None, instance=update_it)
        if form.is_valid():
            form.save()
            messages.success(requset, "Category Updated Successfully.!")
            return redirect( 'categories' )
        return render(requset, 'category_update.html', {"form":form,})
    else:
        messages.success(requset, "Something Went Wrong.!")
        return redirect ('categories')
    
# category delete function
def category_delete(request,pk):
    if request.user.is_authenticated:
        delete_it = Category.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Category Deleted Successfully.!")
        return redirect ('categories') 
    else:
        messages.success(request, "Something Went Wrong.!")
        return redirect ('categories')
    

# Seller Functions Starts from here

# seller page functions
def sellers(request):
    sellers = Seller.objects.all()
    return render(request, 'sellers.html', {'sellers':sellers})

# seller details functions
def seller_details(request, pk):
    if request.user.is_authenticated:
        # look up buyers
        seller_details = Seller.objects.get(id=pk)
        return render(request, 'seller_details.html', {'seller_details':seller_details})
    else:
        messages.success("Something Went Wrong.!")
        sellers = Seller.objects.all()
        return render(request, 'sellers.html', {'sellers':sellers})

# delete seller function
def seller_delete(request,pk):
    if request.user.is_authenticated:
        delete_it = Seller.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Seller Deleted Successfully.!")
        return redirect ('sellers') 
    else:
        messages.success(request, "Something Went Wrong.!")
        return redirect ('sellers')
    
# add buyer function
def seller_add(request):
    form = SellerAddForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                seller_add = form.save()
                messages.success(request, "Seller Added Successfully.!")
                return redirect( 'sellers' )
        return render(request, 'seller_add.html', {"form":form,})
    else:
        messages.success(request, "Something Went Wrong.!")
        return redirect ('sellers')

# Seller Update function 
def seller_update(requset, pk):
    if requset.user.is_authenticated:
        update_it = Seller.objects.get(id=pk)
        form = SellerAddForm(requset.POST or None, instance=update_it)
        if form.is_valid():
            form.save()
            messages.success(requset, "Seller Updated Successfully.!")
            return redirect( 'sellers' )
        return render(requset, 'seller_update.html', {"form":form,})
    else:
        messages.success(requset, "Something Went Wrong.!")
        return redirect ('sellers')