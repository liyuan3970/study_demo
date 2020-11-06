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
# echart的完整案例用法
def index_view(request):
    ## print(this is a index)
    return render(request,'index_view.html',locals())

def bar_data(request):
    data={
        'name':'zhangsan',
        'age':18,
        'data':[5, 20, 36, 10, 10, 20],
        'bar':["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"],
    }
    return JsonResponse(data)