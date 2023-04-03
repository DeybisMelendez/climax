from django.urls import path
from .views import customer_search, customer_detail, customer_create, customer_delete

urlpatterns = [
    path('', customer_search, name='customer_search'),
    path('detail/<int:pk>/', customer_detail, name='customer_detail'),
    path('create/', customer_create, name='customer_create'),
    path('delete/<int:pk>/', customer_delete, name='customer_delete'),
]
