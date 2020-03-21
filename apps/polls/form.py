from django import forms
from .models import Helper


class HelperForm(forms.ModelForm):
    class Meta:
        model = Helper
        fields = ('first_name', 'last_name')
