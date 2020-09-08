from django.forms import ModelForm
from django.conf import settings
from django import forms
import datetime as datetime
from .models import CarInsurance


class CarInsuranceForm(forms.Form):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	phone = forms.IntegerField()
	email = forms.CharField(max_length=100)
	car_make = forms.CharField(max_length=100)
	car_year = forms.IntegerField()
	car_model = forms.CharField(max_length=100)
	brand_new = forms.BooleanField()
	registration_date = forms.DateField()
	registration_place = forms.CharField(max_length=100)
	date_of_birth = forms.DateField()
	nationality = forms.CharField(max_length=100)
	international_exp = forms.IntegerField()
	country_license = forms.CharField(max_length=100)
	claims_12_months = forms.BooleanField()
	is_insured = forms.BooleanField()
	policy_ends = forms.DateField()
	comprehensive_insurance = forms.BooleanField()

	class Meta:
		model = CarInsurance
		fields = [
				'first_name',
				'last_name',
				'phone',
				'email',
				'car_make',
				'car_year',
				'car_model',
				'brand_new',
				'registration_date',
				'registration_place',
				'date_of_birth',
				'nationality',
				'international_exp',
				'country_license',
				'claims_12_months',
				'is_insured',
				'policy_ends',
				'comprehensive_insurance'
		]

		