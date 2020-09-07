from django.db import models

# Create your models here.
class PropertyInsurance(models.Model):
	house_type = models.CharField(max_length=100) # own or rent
	house_insurance = models.CharField(max_length=100) # building or building and contents or contents
	buildings_value = models.IntegerField()
	contents_value = models.IntegerField()
	personal_belongings_value = models.IntegerField() # personal belongings that you take with you
