from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    names=['Oybek', 'Soli', 'Vali']
    name='Olim'
    return render(request, 'index.html', {'ism': name, 'ismlar': names})


def goodbye(request):
    return HttpResponse("Xayr")

def ism(request):
    return HttpResponse("<font color=red> Shokirov Jamshid </font>")






