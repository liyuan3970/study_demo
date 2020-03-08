from django.shortcuts import render

# Create your views here.

def index(request):
    ## print(this is a index)
    return render(request,'index.html',locals())

def geojson(request):
    ## print(this is a index)
    return render(request,'index.html',locals())