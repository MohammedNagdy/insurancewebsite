from django.urls import path
from .views import get_car_insurance

urlpatterns = [
		path('car-insurance', get_car_insurance, name='car-qoutes'),
	]
