from django.contrib import admin

from django.urls import path, re_path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

from App import views


urlpatterns = [
    # re_path(r'^category$',views.categoryApi),
    # re_path(r'^category$',views.categoryApi),



    # developer id = chathura prasanga
    # date = 09/14/2023
    # re path for Category
    re_path('category/([0-9]+)$',views.categoryApi),
    re_path('category/',views.categoryApi),

    # developer id = chathura prasanga
    # date = 09/14/2023
    # re path for Brand
    re_path('brand/([0-9]+)$',views.brandApi),
    re_path('brand/',views.brandApi),

    # developer id = chathura prasanga
    # date = 09/15/2023
    # re path for Product
    re_path('product/([0-9]+)$',views.productApi),
    re_path('product/',views.productApi),

    # developer id = chathura prasanga
    # date = 09/16/2023
    # re path for supplier
    re_path('supplier/([0-9]+)$',views.supplierApi),
    re_path('supplier/',views.supplierApi),

    # developer id = chathura prasanga
    # date = 09/16/2023
    # re path for customer
    re_path('customer/([0-9]+)$',views.supplierApi),
    re_path('customer/',views.supplierApi),

     # developer id = chathura prasanga
    # date = 09/16/2023
    # re path for supplier invoice api
    re_path('supplierinvoice/([0-9]+)$',views.supplierInvoiceApi),
    re_path('supplierinvoice/',views.supplierInvoiceApi),

    # developer id = chathura prasanga
    # date = 09/16/2023
    # re path for supplier bill api
    re_path('supplierbill/([0-9]+)$',views.supplierBillApi),
    re_path('supplierbill/',views.supplierBillApi),

    # developer id = chathura prasanga
    # date = 09/16/2023
    # re path for customer invoice api
    re_path('customerinvoice/([0-9]+)$',views.customerInvoiceApi),
    re_path('customerinvoice/',views.customerInvoiceApi),

    # developer id = chathura prasanga
    # date = 09/16/2023
    # re path for customer bill api
    re_path('customerbill/([0-9]+)$',views.customerBillApi),
    re_path('customerbill/',views.customerBillApi),

    # developer id = chathura prasanga
    # date = 09/27/2023
    # re path for system user register and login
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('dashboard/',views.dashboardApi)
]

router = DefaultRouter()
router.register('user',UserViewSet, basename='user')

urlpatterns += router.urls