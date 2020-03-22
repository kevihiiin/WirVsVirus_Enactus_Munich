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
        labels = {'name' : 'Name des Krankenhauses', 'first_name_contact': 'Vorname der Kontaktperson',
                  'last_name_contact': 'Nachname der Kontaktperson', 'e_mail': 'E-Mail der Kontaktperson',
                  'phone_nbr': 'Telefonnummer der Kontaktperson', 'post_code': 'Postleitzahl des Krankenhauses',
                  'street': 'Straßenname', 'number_of_helpers':'Wie viele Helfer benötigen Sie?',
                  'skill_level':'Wie viel medizinische Vorerfahrung sollen die Helfer haben?',
                  'age_requirement':'Mindestalter der Helfer'
                }
