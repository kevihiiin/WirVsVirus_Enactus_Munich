from django import forms
from .models import Helper, Hospital


class HelperForm(forms.ModelForm):
    class Meta:
        model = Helper
        fields = ('first_name', 'last_name', 'e_mail', 'phone_nbr', 'skill_level', 'post_code', 'radius')


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = (
        'name', 'e_mail', 'phone_nbr', 'first_name_contact', 'last_name_contact', 'post_code', 'street',
        'number_of_helpers', 'skill_level', 'age_requirement')
