"""
URL configuration for pet_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from petapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register,name="register"),
    path('login/', views.user_login,name="user_login"),
    path('logout/', views.user_logout,name="user_logout"),
    path('list-pets/', views.list_pets,name="list_pets"),
    path('', views.list_pets,name="list_pets"),
    path('pet-details/<int:id>', views.pet_details,name="pet_details"),
    path('add-to-cart/<int:pet_id>', views.add_to_cart,name="add_to_cart"),
    path('dispaly-cart-items/', views.display_cart_items,name="display_cart_items"),
    path('remove-from-cart/<int:pet_id>', views.remove_from_cart,name="remove_from_cart"),
    path('manage-addresses/', views.manage_addresses,name="manage_addresses"),
    path('add-address/', views.add_address,name="add_address"),
    path('set-address/', views.set_address,name="set_address"),
    path('order-review/<int:sa_id>', views.order_review,name="order_review"),
    path('checkout-order/<int:sa_id>', views.checkout_order,name="checkout_order"),
    path('payment-order/', views.payment_order,name="payment_order"),
    path('payment-process/<int:order_id>/<int:amount>', views.payment_process,name="payment_process"),
    path('search-pets/', views.search_pets,name="search_pets"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)