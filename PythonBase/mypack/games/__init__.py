# mypack/games/__init__.py

'''这是games子包里的文档字符串标题

...
...
...
'''

# 此__all__列表,会影响 from mypack.games import *
# 当用上述语句导入时,只导入 contra 和tanks
# 默认所有的包内模块都不导入

__all__ = ['contra', 'tanks']



print("mypack/games/__init__.py 被加载执行")