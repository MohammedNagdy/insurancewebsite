from django.forms import ModelForm
from django.conf import settings
from django import forms
import datetime as datetime
from .models import TravelInsurance


class TravelInsuranceForm(forms.Form):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	phone = forms.IntegerField()
	email = forms.CharField(max_length=100)
	insurance_type = forms.CharField(max_length=100) # single trip or semi annual or annual
	insurance_start_date = forms.DateField()
	insurance_end_date = forms.DateField()
	country_destination = forms.CharField(max_length=100)

	class Meta:
		model = TravelInsurance
		fields = [
				'first_name',
				'last_name',
				'phone',
				'email',
				'insurance_type',
				'insurance_start_date',
				'insurance_end_date',
				'country_destination'
		]