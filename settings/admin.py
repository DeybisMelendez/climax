from django.contrib import admin
from .models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', "symbol")
    list_filter = ('code', 'name', "symbol")
    search_fields = ('code', 'name', "symbol")
