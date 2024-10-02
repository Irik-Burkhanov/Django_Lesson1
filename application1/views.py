from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def func1_app1(request):
    return HttpResponse('func1_app1')

def func2_app1(request):
    return HttpResponse('func2_app1')

def func3_app1(request):
    return HttpResponse('func3_app1')