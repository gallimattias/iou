from django.forms import ModelForm
from website.models import Client, Agreement


# Create the form class.
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name_first', 'name_last', 'email', 'phone', ]
        labels = {'name_first': 'Förnamn', \
                  'name_last': 'Efternamn', \
                  'email': 'E-mail', \
                  'phone': 'Telefonnummer'}


# Create the form class.
class AgreementForm(ModelForm):
    class Meta:
        model = Agreement
        fields = ['notional', 'amortisation', 'maturity',
                  'ir_method', 'payment_frequency']
        labels = {'notional': 'Belopp',
                  'amortisation': 'Amortering',
                  'maturity': 'Slutdatum',
                  'ir_method': 'Räntemetod',
                  'payment_frequency': 'Betalningsfrekvens'}
