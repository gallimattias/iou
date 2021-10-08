from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here
# .

class Client(models.Model):
    """Obligor or Issuer information"""
    name_first = models.CharField(max_length=50, help_text="The first name of the client.")
    name_last = models.CharField(max_length=50, help_text="The last name of the client.")
    email = models.EmailField(help_text="The client e-mail")
    phone = PhoneNumberField(unique=True)
    ssnseo = models.CharField(max_length=12, help_text="Social security number, or organisation-number of client.")


class Agreement(models.Model):
    """Agreement information"""

    notional = models.FloatField(help_text='Outstanding notional of agreement')
    amortisation = models.BinaryField(help_text='1 translates into linear amortisation')
    perpetual = models.BinaryField(help_text='1 translates into a perpetual agreement (no end-date)')
    maturity = models.DateField(help_text='Last day of agreement')

    # IR-METHOD CATEGORICAL
    ir_methods_choices = [
        ('NONE', 'None'),
        ('FIX', 'Fixed Interest rate'),
        ('FLOAT', 'Floating Interest rate'),
        ('INDEX', 'Indexation'),
    ]
    ir_method = models.CharField(max_length=5, choices=ir_methods_choices, default='NONE', )

    # PAYMENT-FREQUENCY CATEGORICAL
    payment_frequency_choices = [
        ('M', 'Monthly'),
        ('Q', 'Quarterly'),
        ('A', 'Annually'),
        ('T', 'Maturity'),
    ]
    payment_frequency = models.CharField(max_length=1, choices=payment_frequency_choices, default='M', )
    signed_issuer = models.BinaryField(help_text='1 : Issuer has signed with BankID')
    signed_obligor = models.BinaryField(help_text='1 : Obligor has signed with BankID')