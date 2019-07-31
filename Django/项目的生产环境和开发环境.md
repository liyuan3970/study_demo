# 自己配置生产环境和开发环境
1. 构建一个Django 的项目
2. 项目目录如下
**原始目录如下**
```
      ├── demo
      │   ├── __init__.py
      │   ├── settings.py
      │   ├── urls.py
      │   └── wsgi.py
      └── manage.py
```
**修改后的目录如下**
```

       ├── demo
       │   ├── __init__.py
       │   ├── settings
       │   │   ├── base.py
       │   │   ├── __init__.py
       │   │   ├── product.py
       │   │   └── develop.py
       │   ├── urls.py
       │   └── wsgi.py
       └── manage.py
```
3. 修改manage.py和wsgi.py文件<br>
**manage.py**
```python 
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    profile = os.environ.get('DEMO_PROFILE', 'product')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings.%s" % profile)
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "My_blog.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
```
**wsgi.py**
```python
"""
WSGI config for My_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
profile = os.environ.get('DEMO_PROFILE', 'product')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings.%s" % profile)
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "My_blog.settings")
application = get_wsgi_application()
```

# 注：　主要是修改manage和wsgi两个文件的如下代码
```python 
# 将原来的
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")
#修改为
profile = os.environ.get('DEMO_PROFILE', 'product')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings.%s" % profile)
```


