from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'login.html')

def index_reg(request):
    return render(request, 'registration.html')