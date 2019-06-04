# 在settings里面配置mysql数据库
```python 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'FruitDay',  #数据库的名称
        'USER': 'root',      #用户名
        'PASSWORD':123456,   #密码
        'HOST': 'localhost', #ip
        'PORT':3306,         #端口
    }
}
```