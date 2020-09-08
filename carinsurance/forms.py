from django.forms import ModelForm
from django.conf import settings
from django import forms
import datetime as datetime
from .models import CarInsurance


class CarInsuranceForm6(forms.Form):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	phone = forms.IntegerField()
	email = forms.CharField(max_length=100)


class CarInsuranceForm1(forms.Form):
	car_make = forms.CharField(max_length=100)
	car_year = forms.IntegerField()
	car_model = forms.CharField(max_length=100)

class CarInsuranceForm2(forms.Form):
	brand_new = forms.BooleanField()
	registration_date = forms.DateField()
	registration_place = forms.CharField(max_length=100)

class CarInsuranceForm3(forms.Form):
	date_of_birth = forms.DateField()
	nationality = forms.CharField(max_length=100)
	international_experience = forms.IntegerField()

class CarInsuranceForm4(forms.Form):
	country_license = forms.CharField(max_length=100)
	insurance_claims_12_months = forms.BooleanField()

class CarInsuranceForm5(forms.Form):
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
				'international_experience',
				'country_license',
				'insurance_claims_12_months',
				'is_insured',
				'policy_ends',
				'comprehensive_insurance'
		]

		