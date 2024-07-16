from django import forms
from .models import CONTACT

class Contacts(forms.ModelForm): 
    class Meta: 
        model = CONTACT
        fields = ['name', 'phone', 'email', 'address']