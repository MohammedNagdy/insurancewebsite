from django.shortcuts import render
from .forms import PropertyInsuranceForm
from .models import PropertyInsurance


# Create your views here.


def get_prop_insu(request):
	template = 'propinsu.html'
	form = PropertyInsuranceForm(request.POST)

	if request.method == 'POST':
		if form.is_valid():
			obj = PropertyInsurance()
			obj.first_name = form.cleaned_data.get('first_name')
			obj.last_name = form.cleaned_data.get('last_name')
			obj.phone = form.cleaned_data.get('phone')
			obj.email = form.cleaned_data.get('email')
			obj.house_type = form.cleaned_data.get('house_type')
			obj.house_insurance = form.cleaned_data.get('house_insurance')
			obj.buildings_value = form.cleaned_data.get('buildings_value')
			obj.contents_value = form.cleaned_data.get('contents_value')
			obj.personal_belongings_value = form.cleaned_data.get('personal_belongings_value')

			obj.save()

	context = {
		'form':form,
	}

	return render(request, template, context)

