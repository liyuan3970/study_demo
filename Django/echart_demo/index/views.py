from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def index(request):
    ## print(this is a index)
    return render(request,'index.html',locals())

def geojson(request):
    ## print(this is a index)
    return render(request,'index2.html',locals())

def index3(request):
    ## print(this is a index)
    return render(request,'index3.html')

def rjson(request):
    data={
        'name':'zhangsan',
        'age':18,
    }
    return JsonResponse(data)