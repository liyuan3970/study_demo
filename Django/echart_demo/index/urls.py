"""blogdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # 首页的配置方法
    url(r'^$',views.index),
    url(r'index_demo',views.index_view),
    url(r'json_respone',views.geojson),
    # echart的完整案例用法
    url(r'index3',views.index3),
    url(r'bar_data',views.bar_data),

    url(r'json_reback',views.rjson),
]
