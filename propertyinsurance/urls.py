from django.urls import path
from .views import get_prop_insu

urlpatterns = [
		path('property-insurance', get_prop_insu, name='prop-qoutes'),
	]
