# 通过class-bass-view定义视图层
## 这样做的目的主要是为了方便定义Get和Post请求
```python 
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .form import StudentForm
from .models import Student

class IndexView(View):
    template_name = 'index.html'
    #查询数据库操作
    def get_context(self):
        students = Student.get_all()
        context = {'students':students,}
        return context
    # 定义ＧＥＴ请求
    def get(self,request):
        context = self.get_context()
        form = StudentForm()
        context.update({'form':form})
        return render(request,self.template_name,context=context)
    # 定义ＰＯＳＴ请求
    def post(self,request):
        form = StudentForm(request)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context.update({'form':form})
        return render(request,self.template_name,context=context)
```

配置url.py 函数
```python
from django.conf.urls import url
from django.contrib import admin 

from student.views import IndexView

urlpatterns = [
    url(r'^$',IndexView.as_view(),name = 'index'),
    url(r'^admin/',admin.site.urls),
]
```