from.import views # to render templates 
from django.urls import path 

urlpatterns = [
    path('', views.home, name='home'), # home page
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('buyers/', views.buyers, name='buyers'),
    path('buyer_details/<int:pk>', views.buyer_details, name='buyer_details'),
    path('buyer_delete/<int:pk>', views.buyer_delete, name='buyer_delete'),
    path('buyer_add/', views.buyer_add, name='buyer_add'),
    path('buyer_update/<int:pk>', views.buyer_update, name='buyer_update'),
]
