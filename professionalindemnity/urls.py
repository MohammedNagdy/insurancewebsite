from django.urls import path
from .views import get_qoutes_view

urlpatterns = [
		path('professional', get_qoutes_view, name='pro-qoutes'),
	]
