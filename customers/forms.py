from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'ruc', 'email', 'phone', 'city', 'address']
        labels = {
            'name': 'Nombre',
            'ruc': 'RUC',
            'email': 'Correo',
            'phone': 'Teléfono',
            'address': 'Dirección',
            'city': 'Ciudad'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'full-width', 'placeholder': 'Nombre'}),
            'ruc': forms.TextInput(attrs={'class': 'full-width', 'placeholder': 'RUC'}),
            'email': forms.EmailInput(attrs={'class': 'full-width', 'placeholder': 'Correo'}),
            'phone': forms.TextInput(attrs={'class': 'full-width', 'placeholder': 'Teléfono'}),
            'address': forms.TextInput(attrs={'class': 'full-width', 'placeholder': 'Dirección'}),
            'city': forms.TextInput(attrs={'class': 'full-width', 'placeholder': 'Ciudad'}),
        }

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
