from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "mainapp/index.html", {'start_time': start_time})

import time
start_time = time.strftime('Start time: %H:%M:%S %b %d, %Y')