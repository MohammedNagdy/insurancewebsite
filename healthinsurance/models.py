from django.db import models

# Create your models here.
class PersonalInfoModel(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	phone = models.IntegerField()
	email = models.CharField(max_length=100)