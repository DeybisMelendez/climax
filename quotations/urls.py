from django.urls import path
from .views import quote_detail, quote_create, quote_update, quote_search, quote_delete

urlpatterns = [
    path('quotes/', quote_search, name='quote_search'),
    path('quote_detail/<int:pk>/', quote_detail, name='quote_detail'),
    path('create/', quote_create, name='quote_create'),
    path("update/<int:pk>/", quote_update, name="quote_update"),
    path('delete/<int:pk>/', quote_delete, name='quote_delete'),
]
