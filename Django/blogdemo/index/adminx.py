from django.contrib import admin
from .models import *
# Register your models here.
import xadmin
class PostAdmin(object):
    #显示所有文章的字段
    list_display = ('post_name', 'time', 'auther','tag')
    # 对应的字段可以作为超链接进去
    list_display_links = ('auther', 'tag')
    # 自爱文章列表中可以修改的字段，和link不能重叠
    list_editable = ('time',)


    # 在文章列表右侧添加一个过滤的选项
    list_filter = ('auther',)
    # 在文章列表顶部添加一个搜索狂，方便用户查找，里面的字段是查询的关键字
    search_fields = ('post_name', 'time')

    # 这个编辑页面的基本布局
    fieldsets = (
        #组1-基本选项,包含post_name和auther两个列
        ('基本选项',{
            'fields':('post_name','auther')
        }),
        #组2-高级选项,包含tag和time和content
        ('高级选项',{
            'fields':('tag','time','content'),
            'classes':('content',)
        })
    )





xadmin.site.register(Auther)
xadmin.site.register(Post,PostAdmin)
xadmin.site.register(Tag)