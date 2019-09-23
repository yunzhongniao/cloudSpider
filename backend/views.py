from django.shortcuts import render
from django.http import HttpResponse
from backend import models

# Create your views here.
def books(request):
    
    return HttpResponse("You're looking at question %s." % question_id)
