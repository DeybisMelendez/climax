from django import forms
from .models import Quote, Item


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["date", 'customer', "contact", "currency", "unit",
                  'description', "note"]
        labels = {
            "date": "Fecha",
            "customer": "Cliente",
            "contact": "Contacto",
            "currency": "Moneda",
            "unit": "Unidad de moneda",
            "description": "Descripción",
            "note": "Nota",
        }
        widgets = {
            "date": forms.DateInput(attrs={
                "class": "full-width",
                "placeholder": "Ej: 2022-01-01",
            }),
            "customer": forms.Select(attrs={
                "class": "full-width",
                "placeholder": "Seleccione un cliente",
            }),
            "contact": forms.TextInput(attrs={
                "class": "full-width",
                "placeholder": "Ej: Juan Pérez",
            }),
            "note": forms.Textarea(attrs={
                "class": "full-width",
                "placeholder": "Ej: Garantía por 30 días.",
                "rows": "4"
            }),
            "description": forms.Textarea(attrs={
                "class": "full-width",
                "placeholder": "Ej: Se realizó prueba de frío.",
                "rows": "4"
            }),
            "currency": forms.TextInput(attrs={
                "class": "full-width",
                "placeholder": "Ej: Córdobas",
            }),
            "unit": forms.TextInput(attrs={
                "class": "full-width",
                "placeholder": "Ej: C$",
            }),
        }


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['quantity', 'description', 'price']


ItemFormset = forms.inlineformset_factory(
    Quote, Item, form=ItemForm, extra=0
)
