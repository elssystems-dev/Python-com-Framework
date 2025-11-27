from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
a = 10
def home(request):
    return render(request, "home.html", context={'nome': a})