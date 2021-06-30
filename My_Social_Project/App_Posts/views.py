from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return HttpResponse('Homepage')
