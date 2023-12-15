"""
URL configuration for receipt_tracker project.

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
# receipts/urls.py
from django.urls import path
from receipts.views import receipt_list, receipt_detail, receipt_form
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', receipt_list, name='receipt_list'),
    path('receipt/<int:pk>/', receipt_detail, name='receipt_detail'),
    path('receipt/new/', receipt_form, name='receipt_form'),
    path('receipt/<int:pk>/edit/', receipt_form, name='receipt_edit'),
    path('accounts/login/', LoginView.as_view(), name='login')
]
