from django.shortcuts import render
from .forms import TravelInsuranceForm
from .models import TravelInsurance


# Create your views here.


def get_travel_insu(request):
	template = 'travelinsu.html'
	form = TravelInsuranceForm(request.POST)

	if request.method == 'POST':
		if form.is_valid():
			obj = TravelInsurance()
			obj.first_name = form.cleaned_data.get('first_name')
			obj.last_name = form.cleaned_data.get('last_name')
			obj.phone = form.cleaned_data.get('phone')
			obj.email = form.cleaned_data.get('email')
			obj.insurance_type = form.cleaned_data.get('insurance_type')
			obj.insurance_start_date = form.cleaned_data.get('insurance_start_date')
			obj.insurance_end_date = form.cleaned_data.get('insurance_end_date')
			obj.country = form.cleaned_data.get('country_destination')
			obj.save()

	context = {
		'form':form,
	}

	return render(request, template, context)

