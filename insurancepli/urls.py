from django.urls import path
from .views import get_qoutes_view

urlpatterns = [
		path('insurance-pli', get_qoutes_view, name='pli-qoutes'),
	]
