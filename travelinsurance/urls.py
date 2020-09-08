from django.urls import path
from .views import get_travel_insu

urlpatterns = [
		path('travel-insurance', get_travel_insu, name='travel-qoutes'),
	]
