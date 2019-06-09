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
# 安装mysql-client
```shell
pip install mysqlclient
```

# 方法二
在settings.py所在的目录里寻找__init__.py<br>
pip install pymysql<br>
编写如下代码
```python
#__init__.py
import pymysql
pymysql.install_as_MySQLdb()

```