from django.shortcuts import render
from django.http import HttpResponse
from .templates import *
def hello(request):
    return HttpResponse('Hello this is our new server')

def page1(request):
    people = [
        {'Name': 'Sahil', 'Roll_no': 11222641, 'age':19},
        {'Name': 'Tanuj Saini', 'Roll_no': 11222650,'age':20},
        {'Name': 'Vaishnavi', 'Roll_no': 11222657, 'age':20},
        {'Name': 'Ananaya Sharma', 'Roll_no': 11222507, 'age':20},
    ]   
    vegiies=[
        'lady-finger','loki','krela','kaadu'
    ]
    veg=None
    result=None
    if request.method =='POST':
        veg=str(request.POST.get('veg'))
        result=veg in vegiies

    return render(request, 'index.html', context={'peoples': people,'Vegetables': vegiies,'result':result,'veg':veg})


# def aboutv(request):
#     return render(request, 'about.html')