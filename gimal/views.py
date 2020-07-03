from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse("Hello, fockin gimal")

def index(request):
	return render(request, 'index.html')