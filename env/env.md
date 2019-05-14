#Python 创建虚拟环境
##安装
```shell
pip install virtualenv
```
##基本使用
```shell
#创建环境
cd my_project_dir
virtualenv venv　　#venv为虚拟环境目录名，目录名自定义
```
#为环境指定python版本

```shell
virtualenv -p /usr/bin/python2.7 venv# -p参数指定Python解释器程序路径
```

#激活环境
```shell
source venv/bin/activate
```

#停滞环境
```shell
. venv/bin/deactivate
```

#安装各种包
```shell
pip3 install ...
```

#启动python
```shell
python3 

```

