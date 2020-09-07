from django.db import models

# Create your models here.
class CarInsurance(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	phone = models.IntegerField()
	email = models.CharField(max_length=100)
	car_make = models.CharField(max_length=100)
	car_year = models.IntegerField()
	car_model = models.CharField(max_length=100)
	brand_new = models.BooleanField(default=True)
	registration_date = models.DateField()
	registration_place = models.CharField(max_length=100)
	date_of_birth = models.DateField()
	nationality = models.CharField(max_length=100)
	international_exp = models.IntegerField()
	country_license = models.CharField(max_length=100)
	claims_12_months = models.BooleanField(default=False)
	is_insured = models.BooleanField(default=False)
	policy_ends = models.DateField()
	comprehensive_insurance = models.BooleanField(default=False)
