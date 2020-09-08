from django.urls import path
from .views import PropertyInsuranceView
from .forms import  (PropertyInsuranceForm1, PropertyInsuranceForm2, PropertyInsuranceForm3, PropertyInsuranceForm4, PropertyInsuranceForm5, PropertyInsuranceForm6)


urlpatterns = [
		path('property-insurance', PropertyInsuranceView.as_view([PropertyInsuranceForm1, PropertyInsuranceForm2, PropertyInsuranceForm3, PropertyInsuranceForm4, PropertyInsuranceForm5, PropertyInsuranceForm6]), name='prop-qoutes'),
	]
