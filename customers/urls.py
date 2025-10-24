from django.urls import path
from .views import customer_search, customer_create, customer_delete, customer_update

urlpatterns = [
    path('', customer_search, name='customer_search'),
    path('create/', customer_create, name='customer_create'),
    path("update/<int:pk>/", customer_update, name="customer_update"),
    path('delete/<int:pk>/', customer_delete, name='customer_delete'),
]
