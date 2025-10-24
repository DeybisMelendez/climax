from django.contrib import admin
from .models import Quote, Item


class ItemInline(admin.TabularInline):
    model = Item
    extra = 1


class QuoteAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    search_fields = ['number', 'customer__name',
                     'description',  "total"]
    list_display = ('number', 'customer', 'description',
                    'note', "currency_ref", "total")
    list_filter = ('customer',)
    ordering = ('-number',)


admin.site.register(Quote, QuoteAdmin)
