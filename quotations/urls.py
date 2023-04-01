from django.urls import path
from .views import quote_list, quote_detail, quote_create

urlpatterns = [
    path('quotes/', quote_list, name='quote_list'),
    path('quote_detail/<int:pk>/', quote_detail, name='quote_detail'),
    path('create/', quote_create, name='quote_create'),
    # otras URLs
]
