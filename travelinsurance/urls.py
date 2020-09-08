from django.urls import path
from .views import TravelInsuranceView
from .forms import (TravelInsuranceForm1, TravelInsuranceForm2, TravelInsuranceForm3, TravelInsuranceForm4, TravelInsuranceForm5 )

urlpatterns = [
		path('travel-insurance', TravelInsuranceView.as_view([TravelInsuranceForm1, TravelInsuranceForm2, TravelInsuranceForm3, TravelInsuranceForm4, TravelInsuranceForm5 ]), name='travel-qoutes'),
	]
