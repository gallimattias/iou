from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ClientForm1, ClientForm2, AgreementForm
from formtools.wizard.views import SessionWizardView

WIZARD_FORMS = [("ClientForm1", ClientForm1),
                ("ClientForm2", ClientForm2),
                ("AgreementForm", AgreementForm),
                ]

TEMPLATES = {"ClientForm1": "forms/clientform.html",
             "ClientForm2": "forms/clientform.html",
             "AgreementForm": "forms/agreementform.html",
             }


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class ContactWizard(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        # do_something_with_the_form_data(form_list)
        return HttpResponseRedirect('<h1>Done</h1>')
