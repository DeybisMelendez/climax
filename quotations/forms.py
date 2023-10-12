from django import forms
from .models import Quote, Item


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["date", 'customer', "contact", "currency", "unit",
                  'description', "note", "expiration", "discount"]
        labels = {
            "date": "Fecha",
            "customer": "Cliente",
            "contact": "Contacto",
            "currency": "Moneda",
            "unit": "Unidad de moneda",
            "description": "Descripción",
            "note": "Nota",
            "expiration": "Caduca (días)",
        }
        widgets = {
            "date": forms.DateInput(attrs={
                "placeholder": "Ej: 2022-01-01",
            }),
            "customer": forms.Select(attrs={
                "placeholder": "Seleccione un cliente",
            }),
            "contact": forms.TextInput(attrs={
                "placeholder": "Ej: Juan Pérez",
            }),
            "note": forms.Textarea(attrs={
                "placeholder": "Ej: Garantía por 30 días.",
                "rows": "5"
            }),
            "description": forms.Textarea(attrs={
                "placeholder": "Ej: Se realizó prueba de frío.",
                "rows": "10"
            }),
            "currency": forms.TextInput(attrs={
                "placeholder": "Ej: Córdobas",
            }),
            "unit": forms.TextInput(attrs={
                "placeholder": "Ej: C$",
            }),
            "expiration": forms.TextInput(attrs={
                "placeholder": "Ej: 15",
            }),
            "discount": forms.NumberInput(attrs={
                "size": "10",
                # "placeholder": "Por ej: 100",
                "step": "0.01",
                "id": "discount",
            }),
        }


class ItemForm(forms.ModelForm):
    DELETE = forms.BooleanField(required=False)

    class Meta:
        model = Item
        fields = ['quantity', 'description', 'price', "DELETE"]
        widgets = {
            "quantity": forms.NumberInput(attrs={
                "class": "quantity-input",
                "placeholder": "Por ej: 1",
                "step": "0.01",
            }),
            "description": forms.TextInput(attrs={
                "class": "description-input",
                "placeholder": "Por ej: Banda Triple",
                "maxlength": "255"
            }),
            "price": forms.NumberInput(attrs={
                "class": "price-input",
                "placeholder": "Por ej: 1",
                "step": "0.01"
            }),
            "DELETE": forms.CheckboxInput()
        }


ItemFormset = forms.inlineformset_factory(
    Quote, Item, form=ItemForm, extra=0, can_delete=True
)
