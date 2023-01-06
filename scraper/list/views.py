from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    
    name = request.GET.get('name')
    return render(request, 'list/home.html', {'name':name})