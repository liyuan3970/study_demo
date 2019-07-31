# 机器学习DAY01

## 机器学习

### 概述

#### 什么是机器学习

机器学习是一门能够让编程计算机从数据中**学习**的计算机科学.

一个计算程序在完成任务T之后,获得经验E, 表现效果为P. 如果任务T的性能表现(衡量效果P的标准) 随着E的增加而增加. 那么这样的计算机程序就被称为机器学习程序.

#### 为什么需要机器学习

自动化升级与维护

解决那些算法过于复杂, 甚至根本没有已知算法的问题.

在机器学习的过程中协助人类对未知事物的洞察.

#### 机器学习的问题

1. 建模问题

   所谓机器学习, 在形式上可以这样理解: 在数据对象中通过统计或推理等方法, 寻找一个接收特定输入x, 并给出预期输出y的功能函数f.  y=f(x)

2. 评估问题

   针对已知的输入, 函数给出的输出(预测值)与实际输出(目标值)之间存在一定的误差, 因此需要构建一个评估体系, 根据误差的大小判定函数的优劣.

3. 优化问题

   学习的核心在于改善模型性能, 通过数据对算法的反复锤炼, 不断提升函数预测的准确性, 直到获得能够满足业务要求的最优解, 这个过程就是机器学习过程.

#### 机器学习的种类

**监督学习  无监督学习   半监督学习   强化学习**

1. 有监督学习: 用已知输出评估模型的性能.
2. 无监督学习: 在没有已知输出的情况下,仅仅根据输入信息的相关性, 进行类别的划分.
3. 半监督学习: 先通过无监督学习划分类别, 再根据人工标记, 通过有监督学习预测输出.
4. 强化学习: 通过对不同决策结果的奖励和惩罚, 使机器学习系统在经过足够长时间的训练之后, 越来越倾向于期望的结果.

**批量学习  增量学习**

1. 批量学习: 将学习的过程和应用的过程截然分开, 用全部的训练数据训练模型, 然后在应用场景中实现预测. 当预测结果不够理想时, 重新回到学习过程, 如此循环.
2. 增量学习: 将学习的过程和应用的过程统一起来, 在应用的同时以增量的方式, 不断学习新内容, 边训练边预测.

**基于实例的学习   基于模型的学习**

1. 根据以往的经验, 寻找与待预测输入最接近的样本, 以其输出作为预测结果.

   | 年龄 | 学历 | 经验 | 性别 | 月薪  |
   | ---- | ---- | ---- | ---- | ----- |
   | 25   | 硕士 | 2    | 女   | 10000 |
   | 20   | 本科 | 1    | 男   | 8000  |
   | ...  | ...  | ...  | ...  | ...   |
   | 20   | 本科 | 3    | 女   | ?     |

2. 基于模型的学习: 根据以往经验, 建立用于联系输出和输入的某种数学模型, 将带预测的输入带入该模型, 预测其结果.

#### 机器学习的一般过程

**数据处理**

1. 数据收集(数据检索/数据挖掘/爬虫)
2. 数据清洗

**机器学习**

1. 选择模型(算法)
2. 训练模型(算法)
3. 评估/优化模型 (工具, 框架, 算法知识)
4. 测试模型

**业务运维**

1. 应用模型

2. 维护模型

#### 机器学习的典型应用

股价预测  推荐引擎  自然语言识别  语音识别  图像识别  人脸识别

#### 机器学习的基本问题

1. 回归问题

   根据已知的输入和输出寻找某种性能最佳的模型, 将未知输出的输入代入模型, 得到连续的输出.

2. 分类问题

   根据已知的输入和输出寻找某种性能最佳的模型, 将未知输出的输入代入模型, 得到离散的输出.

3. 聚类问题

   根据已知输入的相似程度, 将输入数据划分为不同的群落.

4. 降维问题

   在性能损失尽可能小的前提下, 降低数据的复杂度.



### 数据预处理

数据预处理的过程: 输入数据 -> 模型 -> 输出数据

通用数据样本矩阵结构:

| 年龄 | 学历 | 经验 | 性别 | 月薪  |
| ---- | ---- | ---- | ---- | ----- |
| 25   | 硕士 | 2    | 女   | 10000 |
| 20   | 本科 | 1    | 男   | 8000  |
| ...  | ...  | ...  | ...  | ...   |
| 20   | 本科 | 3    | 女   | ?     |

一行一样本, 一列一特征.

**数据预处理相关库**

```python
import sklearn.preprocessing as sp
```

#### 均值移除(标准化)

由于一个样本的不同特征差异较大, 不利于使用现有的机器学习算法进行样本处理.均值移除可以让样本矩阵中的每一列的平均值为0, 标准差为1.

```python
例如有一列数据表示年龄: 17  20  23
mean = (17+20+23)/3 = 20
17 - 20 = -3
20 - 20 = 0
23 - 20 = 3
```

如何使这组数据的标准差为1呢?

```
a = -3
b = 0
c = 3
s = std([a, b, c])
[a/s, b/s, c/s]
```

均值移除相关API:

```python
import sklearn.preprocessing as sp
# array: 一行一样本 一列一特征
# 对array数组执行均值移除, 返回处理后的结果
A = sp.scale(array)
```

案例:

```python
"""
demo01_scale.py 均值移除
"""
import numpy as np
import sklearn.preprocessing as sp

samples = np.array([
		[17., 100., 4000],
		[20., 80.,  5000],
		[23., 70.,  5500]])

return_samples = sp.scale(samples)
print(return_samples)
print(np.mean(return_samples, axis=0))
print(np.std(return_samples, axis=0))
```

#### 范围缩放

将样本矩阵中的每一列的最小值和最大值设定为相同的区间, 统一各列特征值的范围. 一般情况下,会把特征区间缩放至[0,1].

```
[17, 20, 23]
如何使这组数据的最小值等于0: [0, 3, 6]
如何使这组数据的最大值等于1: [0, 1/2, 1]
```

范围缩放相关API:

```python
# 创建MinMaxScaler缩放器对象
mms = sp.MinMaxScaler(feature_range=(0, 1))
# 调用方法执行范围缩放
结果矩阵 = mms.fit_transform(原始矩阵)
```

案例:

```python
"""
demo02_scaler.py 范围缩放
"""
import numpy as np
import sklearn.preprocessing as sp

samples = np.array([
		[17., 100., 4000],
		[20., 80.,  5000],
		[23., 70.,  5500]])
# 范围缩放器
mms = sp.MinMaxScaler(feature_range=(0,1))
r_samples = mms.fit_transform(samples)
print(r_samples)

# 基于他们之间的线性关系  实现范围缩放
linear_samples = samples.copy()
for col in linear_samples.T:
	# 一个col就是原始样本数组中的一列
	col_min = col.min()
	col_max = col.max()
	A = np.array([  [col_min, 1],
					[col_max, 1]])
	B = np.array([0, 1])
	x = np.linalg.lstsq(A, B)[0]
	col *= x[0]
	col += x[1]
print(linear_samples)
```

#### 归一化

有些情况每个样本的每个特征值具体值并不重要,但是每个样本特征值的占比更加重要.

|      | python | java | php  |
| ---- | ------ | ---- | ---- |
| 2017 | 10     | 20   | 8    |
| 2018 | 5      | 3    | 0    |
| 2019 | ...    | ...  | ...  |

归一化即是用每个样本的每个特征值除以该样本的各个特征值绝对值总和. 变换后的样本矩阵每个样本的特征值绝对值之和为1.

归一化相关API:

```python
# norm  范数
# l1  - l1范数   向量中每个元素绝对值之和
# l2  - l2范数   向量中每个元素平方之和
r = sp.normalize(array, norm='l1')
```

案例:

```python
"""
demo03_normalize.py 归一化
"""
import numpy as np
import sklearn.preprocessing as sp

samples = np.array([
		[17., 100., 4000],
		[20., 80.,  5000],
		[23., 70.,  5500]])

r = sp.normalize(samples, norm='l1')
print(r)
```

#### 二值化

有些业务并不需要分析矩阵详细完整的数据(例如:图像的边缘识别, 只需要分析出边缘即可), 可以根据事先给定的阈值, 用0和1表示特征值不高于/高于阈值. 二值化后, 矩阵中每个元素非0即1, 达到简化数学模型的目的.

二值化相关API:

```python
# 获取二值化器对象
bin = sp.Binarizer(threshold=阈值)
# 基于二值化器转换原始样本矩阵
result = bin.transform(原始样本矩阵)
```

案例:

```python
"""
demo04_binarizer.py 二值化
"""
import numpy as np
import sklearn.preprocessing as sp

samples = np.array([
		[17., 100., 4000],
		[20., 80.,  5000],
		[23., 70.,  5500]])

bin = sp.Binarizer(threshold=80)
r_samples = bin.transform(samples)
print(r_samples)
```

#### 独热编码 (One-Hot)

为样本特征的每个值建立一个由一个1和若干个0组成的序列, 用该序列对所有的特征值进行编码.

```
1		3		2
7		5		4	
1		8		6	
7		3		9
为每一个数字进行独热编码:
1-10    3-100	2-1000
7-01    5-010   4-0100
        8-001   6-0010
                9-0001
使用上述码表, 对原始矩阵编码过后的结果为:
101001000
010100100
100010010
011000001
```

独热编码相关API:

```python
# 获取独热编码器对象
ohe = sp.OneHotEncoder(sparse=是否采用紧缩格式)
# 对原始样本矩阵进行处理
result = ohe.fit_transform(原始样本矩阵)
```

 

```python
# 获取独热编码器对象
ohe = sp.OneHotEncoder(sparse=是否采用紧缩格式)
# 对原始样本矩阵进行训练,得到编码字典
encode_dict = ohe.fit(原始样本矩阵)
# 根据字典对样本矩阵执行独热编码
result = encode_dict.transform(样本矩阵)
```

案例:

```python
# 构建独热编码器
ohe = sp.OneHotEncoder(sparse=False, dtype=int)
r = ohe.fit_transform(samples)
print(r)
```

#### 标签编码

根据字符串形式的特征值在特征序列中的位置, 为其指定一个数字标签, 用于提供给基于数值算法的学习模型.

标签编码相关API:

```python
# 创建标签编码器
lbe = sp.LabelEncoder()
# 执行标签编码
result = lbe.fit_transform(原始样本矩阵)
# 标签解码, 通过result矩阵回推样本矩阵
样本矩阵 = lbe.inverse_transform(result)
```

案例:

```python
"""
demo06_lbe.py  标签编码器
"""
import numpy as np
import sklearn.preprocessing as sp

samples = np.array(['audi', 'ford', 'audi',
	'toyota', 'ford', 'bmw', 'toyota',
	'ford', 'audi'])

# 标签编码器
lbe = sp.LabelEncoder()
r_samples = lbe.fit_transform(samples)
print(r_samples)

inv_samples = lbe.inverse_transform(r_samples)
print(inv_samples)
```

### 线性回归

```
输入     输出
0.5		5.0
0.6		5.5
0.8		6.0
1.1		6.8
1.4		7.0
...
y=f(x)    f(x)=kx+b
```

预测函数:  y = w<sub>0</sub>+w<sub>1</sub>x

x : 输入

y : 输出

w<sub>0</sub>  w<sub>1</sub> : 模型参数

**所谓的模型训练, 就是根据已知的x与y, 找到最佳的模型参数w<sub>0</sub> w<sub>1</sub> , 使得尽可能精确的描述出输入和输出的关系.**

5.0 =  w<sub>0</sub>+w<sub>1</sub> x 0.5

5.5 =  w<sub>0</sub>+w<sub>1</sub> x 0.6

**单样本误差:**

根据预测函数求出输入为x时的预测值: y' = w<sub>0</sub>+w<sub>1</sub>x

单样本误差则为: 1/2 (y' - y) <sup>2</sup>

**总样本误差:**

把所有的单样本误差相加即为总样本误差:1/2 &Sigma;  (y' - y) <sup>2</sup>

**损失函数:**

loss = 1/2 &Sigma;  (w<sub>0 </sub> + w<sub>1</sub>x - y) <sup>2</sup>

所以损失函数就是总样本误差关于模型参数w<sub>0 </sub>  w<sub>1</sub>的函数, 该函数属于三维数学模型, 即需要找到一组w<sub>0 </sub>  w<sub>1</sub> 使得loss取最小值.

案例: 实现线性回归模型梯度下降过程

```python
"""
demo07_linear.py 线性回归
实现线性回归模型梯度下降过程
"""
import numpy as np
import matplotlib.pyplot as mp

train_x = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])

times = 1000 # 存储梯度下降的次数
rate = 0.01 # 记录每次梯度下降模型参数变化率
epoches = [] # 记录每次梯度下降的索引
w0, w1, losses = [1], [1], []
# 模拟梯度下降的过程
for i in range(1, times+1):
	epoches.append(i)
	loss = ((w0[-1] + w1[-1]*train_x \
				- train_y) ** 2).sum() / 2
	# 根据偏导数公式, 求得w0与w1方向上的梯度值
	d0=((w0[-1]+w1[-1]*train_x)-train_y).sum()
	d1=(((w0[-1]+w1[-1]*train_x)-train_y)*\
			train_x).sum()
	w0.append(w0[-1] - rate*d0)
	w1.append(w1[-1] - rate*d1)
# 经过1000次下降,
# 最终得到的w0与w1使得loss函数值接近最小

pred_y = w0[-1] + w1[-1]*train_x

# 绘制训练数据
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=16)
mp.xlabel('x', fontsize=12)
mp.ylabel('y', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(train_x, train_y, marker='o',
	s = 60, c='dodgerblue', 
	label='Train Points')
mp.plot(train_x, pred_y, c='orangered',
	linewidth=2, label='Regression Line')
mp.legend()
mp.show()






```



















