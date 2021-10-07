# Generated by Django 3.2.7 on 2021-10-07 09:10

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notional', models.FloatField(help_text='Outstanding notional of agreement')),
                ('amortisation', models.BinaryField(help_text='1 translates into linear amortisation')),
                ('perpetual', models.BinaryField(help_text='1 translates into a perpetual agreement (no end-date)')),
                ('maturity', models.DateField(help_text='Last day of agreement')),
                ('ir_method', models.CharField(choices=[('NONE', 'None'), ('FIX', 'Fixed Interest rate'), ('FLOAT', 'Floating Interest rate'), ('INDEX', 'Indexation')], default='NONE', max_length=5)),
                ('payment_frequency', models.CharField(choices=[('M', 'Monthly'), ('Q', 'Quarterly'), ('A', 'Annually'), ('T', 'Maturity')], default='M', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_first', models.CharField(help_text='The first name of the client.', max_length=50)),
                ('name_last', models.CharField(help_text='The last name of the client.', max_length=50)),
                ('email', models.EmailField(help_text='The client e-mail', max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('ssnseo', models.CharField(help_text='Social security number, or organisation-number of client.', max_length=12)),
            ],
        ),
    ]
