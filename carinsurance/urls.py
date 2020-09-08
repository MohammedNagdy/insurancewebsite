from django.urls import path
from .views import CarInsuranceView
from .forms import ( CarInsuranceForm1, CarInsuranceForm2,CarInsuranceForm3,CarInsuranceForm4,CarInsuranceForm5,CarInsuranceForm6)

urlpatterns = [
		path('car-insurance', CarInsuranceView.as_view([CarInsuranceForm1, CarInsuranceForm2,CarInsuranceForm3,CarInsuranceForm4,CarInsuranceForm5,CarInsuranceForm6]), name='car-qoutes'),
	]
