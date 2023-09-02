from.import views # to render templates 
from django.urls import path 

urlpatterns = [
    path('', views.home, name='home'), # home page
    # User login registration
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    # Buyers
    path('buyers/', views.buyers, name='buyers'),
    path('buyer_details/<int:pk>', views.buyer_details, name='buyer_details'),
    path('buyer_delete/<int:pk>', views.buyer_delete, name='buyer_delete'),
    path('buyer_add/', views.buyer_add, name='buyer_add'),
    path('buyer_update/<int:pk>', views.buyer_update, name='buyer_update'),
    # Categories
    path('categories', views.categories, name='categories'),
    path('category_add/', views.category_add, name='category_add'),
    path('category_details/<int:pk>', views.category_details, name='category_details'),
    path('category_update/<int:pk>', views.category_update, name='category_update'),
    path('category_delete/<int:pk>', views.category_delete, name='category_delete'),
    # Sellers
    path('sellers/', views.sellers, name='sellers'),
    path('seller_details/<int:pk>', views.seller_details, name='seller_details'),
    path('seller_delete/<int:pk>', views.seller_delete, name='seller_delete'),
    path('seller_add/', views.seller_add, name='seller_add'),
    path('seller_update/<int:pk>', views.seller_update, name='seller_update'),
]
