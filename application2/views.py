from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def func1_app2(request):
    return HttpResponse('func1_app2')

def func2_app2(request):
    return HttpResponse('func2_app2')

def func3_app2(request):
    return HttpResponse('func3_app2')