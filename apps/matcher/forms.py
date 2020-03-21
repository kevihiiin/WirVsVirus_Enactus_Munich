from django import forms
from .models import Helper


class HelperForm(forms.ModelForm):
    class Meta:
        model = Helper
        fields = ('first_name', 'last_name', 'e_mail', 'phone_nbr', 'skill_level', 'post_code', 'radius')
