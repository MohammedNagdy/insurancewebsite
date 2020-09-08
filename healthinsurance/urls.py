from django.urls import path
from .views import get_qoutes_view

urlpatterns = [
		path('health-insurance', get_qoutes_view, name='health-qoutes'),
	]
