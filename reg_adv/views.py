from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse

# Create your views here.

def index_reg(request):
    return render(request, 'registration.html')