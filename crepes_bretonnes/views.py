from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import Http404
from datetime import datetime
from django.shortcuts import render

def home(request):
    request 
    return render(request,'base.html')