from django.shortcuts import render, redirect

# Create your views here.
from apk.models import Clothing


def Index(request):
    return redirect('/admin')


def wash(request):
    if '_wash' in request.POST:
        print(request)
