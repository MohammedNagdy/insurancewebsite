from django.forms import ModelForm
from django.conf import settings
from django import forms
import datetime as datetime
from .models import PersonalInfoModel


class PersonalInfo(forms.Form):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	phone = forms.IntegerField()
	email = forms.CharField(max_length=100)

	class Meta:
		model = PersonalInfoModel
		fields = [
				'first_name',
				'last_name',
				'phone',
				'email'
		]

		