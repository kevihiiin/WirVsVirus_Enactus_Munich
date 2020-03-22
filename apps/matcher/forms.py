from django import forms
from .models import Helper, Hospital


class HelperForm(forms.ModelForm):
    class Meta:
        model = Helper
        fields = ('first_name', 'last_name', 'e_mail', 'phone_nbr', 'skill_level', 'post_code', 'radius')
        labels = {'first_name' :'Dein Vorname', 'last_name' : 'Dein Nachname', 'e_mail': 'Deine E-Mail',
                  'phone_nbr': 'Deine Handynummer - damit das Krankenhaus dich erreichen kann',
                  'post_code': "Deine Postleitzahl - damit wir Krankenhäuser in deiner Nähe finden",
                  'radius': "Wie weit bist bereit zu fahren (in km)"}


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = (
        'name', 'e_mail', 'phone_nbr', 'first_name_contact', 'last_name_contact', 'post_code', 'street',
        'number_of_helpers', 'skill_level', 'age_requirement')
