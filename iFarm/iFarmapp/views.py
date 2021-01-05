from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_P(request):
    return HttpResponse("THIS IS THE HOMW PAGE")