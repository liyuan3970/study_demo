# 注册所需要的model
在app对应目录下的admin.py里面编写如下代码

## 方法一@常见的字段显示设置
```python
#核心引用
from django.contrib import admin
#引用对应app下面所需的
from .models import *
# 声明高级管理类
class AuthorAdmin(admin.ModelAdmin):
    #1. 定义在列表页上显示的字段们
    # 属性:list_display
    # 取值:由属性名组成的元组或列表
    list_display = ('name','age','email')

    #2. 定义在列表页上就能链接到详情页的字段们
    # 属性:list_display_links
    # 取值:由属性名组成的元组或列表
    # 注意:取值必须出现在list_display中
    list_display_links = ('name','email')

    #3. 定义在列表页中就允许被编辑的字段们
    # 属性:list_editable
    # 取值:由属性名组成的元组或列表
    # 注意:取值必须出现在list_display中但不能出现在list_display_links中
    list_editable = ('age',)

    #4. 定义在列表页的右侧增加过滤器实现快速筛选
    # 属性:list_filter
    # 取值:由属性名组成的元组或列表
    list_filter = ('isActive',)

    #5. 添加搜索字段
    # 属性:search_fields
    # 取值:由属性名组成的元组或列表
    search_fields = ('name','email')

    #7. 在详情页中,指定要显示的字段以及顺序
    # 属性:fields
    # 取值:由属性名组成的元组或列表
    # 注意:元组或列表中所写的内容会显示在详情页中,编写的顺序决定了显示的顺序
    # fields = ('name','email','age')

    #8. 在详情页中对字段们进行分组
    # 属性:fieldsets
    # 注意:fields和fieldsets是不能共存的
    fieldsets = (
        #组1-基本选项,包含name和age两个列
        ('基本选项',{
            'fields':('name','age')
        }),
        #组2-高级选项,包含email和isActive两个列
        ('高级选项',{
            'fields':('email','isActive','publishers'),
            'classes':('collapse',)
        })
    )

class BookAdmin(admin.ModelAdmin):
    #6. 指定时间分层选择器
    # 属性:date_hierarchy
    # 取值:必须为DateField或DateTimeField的
    date_hierarchy = 'publicate_date'

#注册对应的model在后台中显示
# Register your models here.
admin.site.register(Author,AuthorAdmin)
admin.site.register(Publisher)
admin.site.register(Book,BookAdmin)
admin.site.register(Wife)

```
## ** 方法二**
**利用装饰器**
```python
from django.contrib import admin
from .models import *
from django.urls import reverse
from django.utils.html import format_html
from .adminforms import PostAdminForm
# 用来配置对应站点的数据
from My_blog.custom_site import custom_site
from My_blog.base_admin import BaseOwnerAdmin
from django.contrib.admin.models import LogEntry
##################################################################################################################################################################

#一个model的内容在另一个model的编辑页面上展示
#e.g在分类的页面上展示编辑新的文章
class PostInline(admin.TabularInline):  # StackedInline  样式不同
    #编辑另一个页面展示可以编辑的字段
    fields = ('title', 'desc','owner','content')
    extra = 10  # 控制额外多几个
    model = Post
#利用装饰器
@admin.register(Category)
#继承的BaseOwnerAdmin来源于admin.ModelAdmin
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline, ]
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')
    fields = ('name', 'status', 'is_nav')
    #这是一个自定义的方法，用来展示文章的数量 obj时具体的分类
    def post_count(self, obj):
        print(obj)
        return obj.post_set.count()

    post_count.short_description = '文章数量'
    #设置request的用户名称（登录到后台的用户名称）
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)
@admin.register(Tag,site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)

# 这个类是用来定义过滤器的，（admin的右侧），使其只显示当前用户的分类，相当于重写PostAdmin的list_filter-->详见PostAdmin
class CategoryOwnerFilter(admin.SimpleListFilter):
    """ 自定义过滤器只展示当前用户分类 """

    title = '分类过滤器'
    parameter_name = 'owner_category'
    # 返回要展示的内容和查询用的id
    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Post ,site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    # operator是字段外的字段，这个定义意味着可以相admin后台自定义显示的字段
    list_display = [
        'title', 'category', 'status', 'created_time', 'operator', 'owner'
    ]
    list_display_links = []
    list_filter = [CategoryOwnerFilter, ]
    search_fields = ['title', 'category_name']
    actions_on_top = True
    actions_on_bottom = True

    save_on_top = True
    ##########################################################################################################################################################
    ##定义model字段中显示的布局方式
    # fields = (
    #     ('category', 'title'),
    #     #'desc',
    #     'status',
    #     'content',
    #     'tag',
    #     'desc',
    # )
    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            ),
        }),
        ('内容', {
            'fields': (
                'desc',
                'content',
            ),
        }),
        ('额外信息', {
            'classes': ('wide',),
            'fields': ('tag',),
        })
    )
    filter_horizontal = ('tag',)
    ##########################################################################################################################################################
    # filter_vertical = ('tag',)
    def operator(self, obj):
        return format_html(
            '<a herf="{}">编辑</a>',

            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = '操作'

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(PostAdmin, self).save_model(request, obj, form, change)
    # 通过重写admin.ModelAdmin的get_queryset方法用来自定义后台展示的列表页
    # def get_queryset(self, request):
    #     qs = super(PostAdmin, self).get_queryset(request)
    #     return qs.filter(owner=request.user)
    


    ##########################################################################################################################################################
    #定义后台的引入css资源，这点本次没有明确表明用法，后续后更新
    class Media:
        css = {
            'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)
@admin.register(LogEntry, site=custom_site)
##################################################################################################################################################################
# 定义后台的日志文件
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']
```

# 配置多个后台，不同后台展示不同的内容
## 修改urls.py
```python 
from django.conf.urls import url
from django.contrib import admin
# 在urls.py对应的目录下新建的custom_site类
from .custom_site import custom_site
urlpatterns = [
    # 两个后台站点对应如下url
    url(r'^super_admin/', admin.site.urls),
    url(r'^admin/', custom_site.urls),
]

```
## 配置对应的admin站点后台展示
```python 
from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    #后台展示头部的相关信息修改
    site_header = '小飞侠'
    site_title = '我的博客后台'
    index_title = '首页'

#这一句的意思就是指明站点归属
custom_site = CustomSite(name='cus_admin')

```