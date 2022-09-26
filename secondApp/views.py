from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def fecha(request):
    dt=datetime.datetime.now()
    sc="<i>La fecha y hora son: </i><br>"+str(dt)
    return HttpResponse(sc)
