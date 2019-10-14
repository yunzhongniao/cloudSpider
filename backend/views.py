from django.shortcuts import render
from django.http import HttpResponse
from backend import models

# Create your views here.
def get_books(request):
    
    return HttpResponse("You're looking at question %s." % question_id)

def get_spiders(request):
    spider_list = [
        {
            'spider_name':'alibaba',
            'spider_id':'alibaba',
        },
        {
            'spider_name':'credit_info',
            'spider_id':'credit_info'
        }
    ]
    return HttpResponse(spider_list)