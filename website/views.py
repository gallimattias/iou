from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ClientForm1,ClientForm2, AgreementForm
from formtools.wizard.views import SessionWizardView

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class ContactWizard(SessionWizardView):
    template_name = 'multiform_wizard.html'
    def done(self, form_list, **kwargs):
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })


def multiform(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form1 = ClientForm(request.POST)
        form2 = ClientForm(request.POST)
        agreement = ClientForm(request.POST)
        # Creating a form to add an article.


        # Creating a form to change an existing article.
        # client = Client.objects.get(pk=1)
        # form = ClientForm(instance=client)
        # check whether it's valid:
        if form1.is_valid() and form2.is_valid and agreement.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form1.save()
            form2.save()
            agreement.save()
            return HttpResponseRedirect('multiform')


    # if a GET (or any other method) we'll create a blank form
    else:
        form1 = ClientForm(prefix='form1')
        form2 = ClientForm(prefix='form2')
        agreement = AgreementForm()

    return render(request, 'multiform.html', {'form1': form1, 'form2': form2, 'agreement':agreement})
