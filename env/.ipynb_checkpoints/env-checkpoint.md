# Python 创建虚拟环境
## 安装
```shell
pip install virtualenv
```
## 基本使用
```shell
#创建环境
cd my_project_dir
virtualenv venv　　#venv为虚拟环境目录名，目录名自定义
```
# 为环境指定python版本

```shell
virtualenv -p /home/liyuan3970/anaconda/bin/python3.7 venv# -p参数指定Python解释器程序路径
```

# 激活环境
```shell
source venv/bin/activate
```

# 停滞环境
```shell
. venv/bin/deactivate
```

# 安装各种包
```shell
pip3 install ...
```

# 启动python
```shell
python3 

```

# 利用python３自带的命令创建全新的环境

## 在制定目录下创建环境（这个环境是一个超级纯净的环境）
```python 
python -m venv /home/liyuan3970/data/git_project/blog/environment
```
## 激活环境
```shell 
source venv/bin/activate
```

## 停止环境
```shell
. venv/bin/deactivate
```