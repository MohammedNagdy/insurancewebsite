from django.shortcuts import render
from .forms import PersonalInfo
from .models import PersonalInfoModel


# Create your views here.

def get_qoutes_view(request):
	template = 'proindemnity.html'
	form = PersonalInfo(request.POST)

	if request.method == 'POST':
		if form.is_valid():
			obj = PersonalInfoModel()
			obj.first_name = form.cleaned_data.get('first_name')
			obj.last_name = form.cleaned_data.get('last_name')
			obj.phone = form.cleaned_data.get('phone')
			obj.email = form.cleaned_data.get('email')
			obj.save()

	context = {
	'form' : form
	}
	return render(request, template, context)