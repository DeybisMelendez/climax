from django.urls import path
from .views import product_list, entry_list, add_product, product_detail, exit_list, add_entry, add_exit
urlpatterns = [
    path('', product_list, name='product_list'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('product/entries/<int:product_id>',
         entry_list, name='product_entries'),
    path('product/exits/<int:product_id>', exit_list, name='product_exits'),
    path("product/update/<int:product_id>",
         add_product, name="product_update"),
    path("product/create", add_product, name="product_create"),
    path("entry/create", add_entry, name="entry_create"),
    path("exit/create", add_exit, name="exit_create"),
    path("entry/update/<int:entry_id>",
         add_entry, name="entry_update"),
]
