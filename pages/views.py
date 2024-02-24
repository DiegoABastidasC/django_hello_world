from django.shortcuts import render

# Create your views here.

#HttpResponse
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Bienvenido a tu servicio WEB')