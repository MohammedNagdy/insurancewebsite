from django.forms import ModelForm
from django.conf import settings
from django import forms
import datetime as datetime
from .models import TravelInsurance


class TravelInsuranceForm5(forms.Form):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	phone = forms.IntegerField()
	email = forms.CharField(max_length=100)


class TravelInsuranceForm1(forms.Form):
	insurance_period_single_trip_or_annual_or_semi_annual = forms.CharField(max_length=100) # single trip or semi annual or annual

class TravelInsuranceForm2(forms.Form):
	insurance_start_date = forms.DateField()

class TravelInsuranceForm3(forms.Form):
	insurance_end_date = forms.DateField()

class TravelInsuranceForm4(forms.Form):
	country_destination = forms.CharField(max_length=100)

	class Meta:
		model = TravelInsurance
		fields = [
				'first_name',
				'last_name',
				'phone',
				'email',
				'insurance_period_single_trip_or_annual_or_semi_annual',
				'insurance_start_date',
				'insurance_end_date',
				'country_destination'
		]