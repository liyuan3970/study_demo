from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView, DetailView, TemplateView

# Create your views here.
def index(request):
    tag = Tag.objects.all()
    post = Post.objects.raw('select * from index_post')
    auther = Auther.objects.raw('select id,auther_name from index_auther')
    return render(request,'index.html',locals())

class Listviews(ListView):
    # 定义查询数据的数据表
    model = Post
    # queryset = Post.objects.all()
    # list的翻页功能
    paginate_by = 5
    # 对应查找的querset对象的名称
    context_object_name = 'post'
    # 模板的名称
    template_name = 'list.html'
    # 定义返回数据的querset的数据结构和内容
    def get_queryset(self):
        return Post.objects.all()

class Detailviews(ListView):
    # 定义查询数据的数据表
    model = Post
    # queryset = Post.objects.all()
    # list的翻页功能
    # paginate_by = 5
    # 对应查找的querset对象的名称
    context_object_name = 'post'
    # 模板的名称
    template_name = 'detail.html'
    # 定义返回数据的querset的数据结构和内容
    def get_queryset(self):
        return Post.objects.all()