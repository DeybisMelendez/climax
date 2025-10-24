from django import forms
from .models import Product, Entry, Exit


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'


class ExitForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = '__all__'
