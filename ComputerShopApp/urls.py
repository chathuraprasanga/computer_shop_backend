from.import views # to render templates 
from django.urls import path 

urlpatterns = [
    path('', views.home, name='home'), # home page
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('dashboard/', views.dashboard, name='dashboard')
]
