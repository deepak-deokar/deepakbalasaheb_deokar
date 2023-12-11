from django import forms
from .models import Contact
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class ContactForm(forms.ModelForm):
    phone = PhoneNumberField(widget=PhoneNumberPrefixWidget, required=False)

    class Meta:
        model = Contact
        fields = ['name', 'email', 'country', 'phone', 'notes']
        widgets = {
            'country': forms.TextInput(attrs={'placeholder': 'Country'}),
        }
