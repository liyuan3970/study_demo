# coding:utf-8
from setuptools import setup, find_packages


setup(
    name='mypack',
    version=1.0,
    description='test packeges',
    author='liyuan3970',
    author_email='857956255@qq.com',
    packages=['mypack',],
    #package_dir={'': 'mypack'},
    # package_data={'': [    # 打包数据文件，方法一
        # 'themes/*/*/*/*',  # 需要按目录层级匹配
    # ]},
    install_requires=[
        'numpy',
        'matplotlib',
    ],
)
