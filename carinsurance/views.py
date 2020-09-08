from django.shortcuts import render
# from .forms import CarInsuranceForm
from django.http import HttpResponse
from .models import CarInsurance

from formtools.wizard.views import SessionWizardView

# Create your views here.

class CarInsuranceView(SessionWizardView):
	template_name = 'carinsu.html'


	def done(self, form_list, **kwargs):
		form_data = process_form_data(form_list)
		obj = CarInsurance()
		obj = form_data
		obj.save()
		return render(request,'success.html', {'form_data':form_data})



def process_form_data(form_list):
	form_data = [form.cleaned_data for form in form_list]
	return form_data



# def get_car_insurance(request):
# 	template = 'carinsu.html'
# 	form = CarInsuranceForm()
# 	if request.method == 'POST':
# 		if form.is_valid():
# 			obj = CarInsurance()
# 			obj.first_name = form.cleaned_data.get('first_name')
# 			obj.last_name = form.cleaned_data.get('last_name')
# 			obj.phone = form.cleaned_data.get('phone')
# 			obj.email = form.cleaned_data.get('email')
# 			obj.car_make = form.cleaned_data.get('car_make')
# 			obj.car_year = form.cleaned_data.get('car_year')
# 			obj.car_model = form.cleaned_data.get('car_model')
# 			obj.brand_new = form.cleaned_data.get('brand_new')
# 			obj.registration_date = form.cleaned_data.get('registration_date')
# 			obj.registration_place = form.cleaned_data.get('registration_place')
# 			obj.date_of_birth = form.cleaned_data.get('date_of_birth')
# 			obj.nationality = form.cleaned_data.get('nationality')
# 			obj.international_exp = form.cleaned_data.get('international_exp')
# 			obj.country_license = form.cleaned_data.get('country_license')
# 			obj.claims_12_months = form.cleaned_data.get('claims_12_months')
# 			obj.is_insured = form.cleaned_data.get('is_insured')
# 			obj.policy_ends = form.cleaned_data.get('policy_ends')
# 			obj.comprehensive_insurance = form.cleaned_data.get('comprehensive_insurance')

# 			obj.save()

# 	context = {
# 		'form' : form,
# 	}

# 	return render(request, template, context)