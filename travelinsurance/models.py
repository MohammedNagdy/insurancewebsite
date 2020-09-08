from django.db import models

# Create your models here.
class TravelInsurance(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	phone = models.IntegerField()
	email = models.CharField(max_length=100)
	insurance_type = models.CharField(max_length=100) # single trip or semi annual or annual
	insurance_start_date = models.DateField()
	insurance_end_date = models.DateField()
	country = models.CharField(max_length=100)