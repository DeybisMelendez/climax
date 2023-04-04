from django.urls import path
from .views import quote_detail, quote_create, quote_update, quote_search, quote_delete, QuotePDFView

urlpatterns = [
    path('', quote_search, name='quote_search'),
    path('create/', quote_create, name='quote_create'),
    path('detail/<int:pk>/', quote_detail, name='quote_detail'),
    path("update/<int:pk>/", quote_update, name="quote_update"),
    path('delete/<int:pk>/', quote_delete, name='quote_delete'),
    path("pdf/<int:pk>/", QuotePDFView.as_view(), name="quote_pdf")
]
