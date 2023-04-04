from django import forms
from .models import Quote, Item


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['customer', 'description', 'note', "contact"]


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['quantity', 'description', 'price']


ItemFormset = forms.inlineformset_factory(
    Quote, Item, form=ItemForm, extra=0
)
