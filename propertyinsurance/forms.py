from django.forms import ModelForm
from django.conf import settings
from django import forms
import datetime as datetime
from .models import PropertyInsurance


class PropertyInsuranceForm(forms.Form):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	phone = forms.IntegerField()
	email = forms.CharField(max_length=100)
	house_type = forms.CharField(max_length=100) # own or rent
	house_insurance = forms.CharField(max_length=100) # building or building and contents or contents
	buildings_value = forms.IntegerField()
	contents_value = forms.IntegerField()
	personal_belongings_value = forms.IntegerField() # personal belongings that you take with you


	class Meta:
		model = PropertyInsurance
		fields = [
				'first_name',
				'last_name',
				'phone',
				'email',
				'house_type',
				'house_insurance',
				'buildings_value',
				'contents_value',
				'personal_belongings_value'
		]

		