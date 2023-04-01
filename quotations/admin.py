from django.contrib import admin
from .models import Customer, Quote, Item


class ItemInline(admin.TabularInline):
    model = Item
    extra = 1


class QuoteAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    search_fields = ['number', 'customer__name', 'description', "note"]
    list_display = ('number', 'customer', 'description', 'note')
    list_filter = ('customer',)
    ordering = ('-number',)


admin.site.register(Customer)
admin.site.register(Quote, QuoteAdmin)
