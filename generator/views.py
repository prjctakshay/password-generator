from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

# home page
def home(request):
    return render(request, 'generator/home.html',{'pass_flag': False,})  # ,{'pass':['inside request : ',request],})

# password generatoe code
def password(request):
    charectors = list('qwertyuiopasdfghjklzxcvbnm')
    numbs = '0123456789'
    special_char = '!@#$%^&*.,'
    uppercase = 'QWERTYUIOPASDFGHJKLZXCVBNM'

    # get lenght of password
    len = int(request.GET.get('len', 6))  # 6 is default
    # to add features of password
    if request.GET.get('numbers'):
        charectors.extend(numbs)
    if request.GET.get('uppercase'):
        charectors.extend(uppercase)
    if request.GET.get('special'):
        charectors.extend(special_char)

    password: str = ''
    for item in range(len):
        password += random.choice(charectors)

    return render(request, 'generator/home.html', {'pass': password,'pass_flag': True,})


