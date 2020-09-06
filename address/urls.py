from django.urls import path

from .views import (
    AddressCreateView,
    AddressDetailView
)

from . import views

urlpatterns = [  
    path('', AddressCreateView.as_view(),name='address-home'),
    path('<int:pk>/', AddressDetailView.as_view(), name='address-detail'), #pk = primary key
    path('<str:shortCode>/', views.get_address_detail, name='get-address-detail'),
    path('counter/<str:code>/', views.view_counter, name='counter'),
]