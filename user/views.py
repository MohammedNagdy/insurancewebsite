from django.shortcuts import render

# Create your views here.


# home view
def home_view(request):
	template = 'index.html'
	return render(request, template)