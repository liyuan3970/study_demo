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
from django.conf.urls import url,include
from django.contrib import admin
from index.views import Listviews,Detailviews,MainList,PostCreate,PostUpdate,funcpost

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('index.urls')),
    url(r'^list$', Listviews.as_view()),
    url(r'^detail$', Detailviews.as_view()),
    url(r'^main$', MainList.as_view(), name='main'),
    url(r'^add', PostCreate.as_view(), name='post_add'),
    url(r'^post_update/(?P<pk>\d+)$', PostUpdate.as_view(), name='post_update'),
    # url(r'^delete/(?P<pk>\d+)$', views.PostDelete.as_view(), name='post_delete'),
    # post的函数版url
    url(r'^funcpost/$',funcpost),
]
