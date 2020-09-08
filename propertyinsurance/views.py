from django.shortcuts import render
# from .forms import PropertyInsuranceForm
from .models import PropertyInsurance


# Create your views here.

from formtools.wizard.views import SessionWizardView

# Create your views here.

class PropertyInsuranceView(SessionWizardView):
	template_name = 'propinsu.html'


	def done(self, form_list, **kwargs):
		form_data = process_form_data(form_list)
		obj = CarInsurance()
		obj = form_data
		obj.save()
		return render(request,'success.html', {'form_data':form_data})



def process_form_data(form_list):
	form_data = [form.cleaned_data for form in form_list]
	return form_data



