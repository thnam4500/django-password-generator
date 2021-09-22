from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'generator/index.html')

def generator(request):
    length=int(request.GET.get('length'))
    password = ''

    character_set="abcdefghijklmnopqrstuvwxyz"

    if request.GET.get('uppercase'):
        character_set += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if request.GET.get('number'):
        character_set += "123456789"

    if request.GET.get('special'):
        character_set +="!@#$%^&*"


    for time in range(0,length):
        password += random.choice(character_set)

    return render(request,'generator/password.html',{'password':password})
