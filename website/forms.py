from django.forms import ModelForm
from website.models import Client, Agreement


# Create the form class.
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name_first', 'name_last', 'email', 'phone', 'ssnseo']



# Creating a form to add an article.
form = ClientForm()

# Creating a form to change an existing article.
client= Client.objects.get(pk=1)
form = ClientForm(instance=client)
