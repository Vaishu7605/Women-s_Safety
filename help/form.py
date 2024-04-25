from django import forms 
from .models import *

class helpform(forms.ModelForm):
    class Meta:
        model = clients
        fields= '__all__'