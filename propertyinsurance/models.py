from django.db import models

# Create your models here.
class PropertyInsurance(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	phone = models.IntegerField()
	email = models.CharField(max_length=100)
	house_type = models.CharField(max_length=100) # own or rent
	house_insurance = models.CharField(max_length=100) # building or building and contents or contents
	buildings_value = models.IntegerField()
	contents_value = models.IntegerField()
	personal_belongings_value = models.IntegerField() # personal belongings that you take with you
