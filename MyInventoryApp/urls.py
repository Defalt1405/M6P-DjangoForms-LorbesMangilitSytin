"""
URL configuration for MyInventorySystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('view_supplier', views.view_supplier, name='view_suppliers'),
    path('view_bottles', views.view_bottles, name='view_bottles'),
    path('view_bottle_details/<int:pk>', views.view_bottle_details, name='view_bottle_details'),
    path('delete_bottle/<int:pk>', views.delete_bottle, name='delete_bottle'),
    path('add_bottle', views.add_bottle, name='add_bottles'),
    path('manage_account/<int:pk>', views.manage_account, name='manage_account'),
    path('change_password/<int:pk>', views.change_password, name='change_password'),
    path('delete_account/<int:pk>', views.delete_account, name='delete_account'),


]
