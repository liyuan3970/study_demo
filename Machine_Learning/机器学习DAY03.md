## 机器学习DAY03

### 决策树

#### 集合算法

根据多个不同的模型给出的预测结果, 利用平均(回归) 或者投票(分类) 的方法, 得出最终的结果.

基于决策树的集合算法, 就是按照某种规则, 构建多颗彼此不同的决策树模型, 分别给出针对未知样本的预测结果, 最后通过平均或投票的方式得到相对综合的结论.

##### 正向激励

首先为样本矩阵中的样本随机分配初始权重, 由此构建一颗带有权重的决策树, 在由该决策树提供预测输出时, 通过加权平均或加权投票的方式产生预测值. 将训练样本带入模型, 预测其输出, 针对那些预测值与实际值不同的样本, 提高其权重, 由此形成第二棵决策树. 重复以上过程, 构建出不同权重的若干棵决策树. 最终使用时, 由这些决策树通过平均/投票的方式得到相对综合的输出.

正向激励相关API:

```python
import sklearn.tree as st
import sklearn.ensemble as se

t_model = st.DecisionTreeRegressor(...)
model = se.AdaBoostRegressor(
    t_model,	# 正向激励内部的模型
	n_estimators=400, # 构建400棵树
	random_state=7	# 随机种子
)
model.fit(..)
model.predict(..)
```

案例: 基于正向激励, 预测房屋价格.

```python
"""
demo01_adaboost.py  正向激励
"""
import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.tree as st
import sklearn.ensemble as se
import sklearn.metrics as sm


# 读取数据  加载波士顿房屋价格
boston = sd.load_boston()
print(boston.data.shape)	# 数据的维度
print(boston.feature_names) # 数据的特征名
print(boston.target.shape)

# 划分测试集与训练集
# 打乱数据集 
# 以random_state随机种子作为参数生成数据集
x, y=su.shuffle(boston.data, boston.target, 
				random_state=7)
train_size = int(len(x)*0.8)
train_x, test_x, train_y, test_y = \
    x[:train_size], x[train_size:], \
    y[:train_size], y[train_size:]

# 创建决策树回归器模型,使用训练集训练模型, 
# 测试集测试模型
t_model=st.DecisionTreeRegressor(max_depth=4)
# 基于正向激励  搞出多颗树
model = se.AdaBoostRegressor(t_model, 
	n_estimators=400, random_state=7)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
```

**特征重要性**

作为决策树模型训练过程中的副产品, 根据每个特征划分子表前后信息熵的减少量得到该特征的重要程度, 此即为该特征重要性指标.  可以通过model.feature_importances_ 来获取每个特征的特征重要性值.

案例:

```python
"""
demo01_adaboost.py  正向激励
"""
import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.tree as st
import sklearn.ensemble as se
import sklearn.metrics as sm
import matplotlib.pyplot as mp
import numpy as np

# 读取数据  加载波士顿房屋价格
boston = sd.load_boston()
print(boston.data.shape)	# 数据的维度
print(boston.feature_names) # 数据的特征名
print(boston.target.shape)

# 划分测试集与训练集
# 打乱数据集 
# 以random_state随机种子作为参数生成数据集
x, y=su.shuffle(boston.data, boston.target, 
				random_state=7)
train_size = int(len(x)*0.8)
train_x, test_x, train_y, test_y = \
    x[:train_size], x[train_size:], \
    y[:train_size], y[train_size:]

# 创建决策树回归器模型,使用训练集训练模型, 
# 测试集测试模型
t_model=st.DecisionTreeRegressor(max_depth=4)
# 基于正向激励  搞出多颗树
model = se.AdaBoostRegressor(t_model, 
	n_estimators=400, random_state=7)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
fi_ab = model.feature_importances_
print(fi_ab)

# 使用决策树训练模型
model=st.DecisionTreeRegressor(max_depth=4)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
fi_t = model.feature_importances_


# 绘制特征重要性柱状图
mp.figure('feature_importances',facecolor='lightgray')
mp.subplot(211)
mp.title('feature_importances',fontsize=16)
mp.ylabel('Feature Importances', fontsize=12)
mp.grid(linestyle=':')
sorted_indices = fi_ab.argsort()[::-1]
x = np.arange(fi_ab.size)
mp.xticks(x, boston.feature_names[sorted_indices])
mp.bar(x, fi_ab[sorted_indices], 
	color='dodgerblue', label='fi_ab')
mp.legend()

mp.subplot(212)
mp.title('feature_importances',fontsize=16)
mp.ylabel('Feature Importances', fontsize=12)
mp.grid(linestyle=':')
sorted_indices = fi_t.argsort()[::-1]
x = np.arange(fi_t.size)
mp.xticks(x, boston.feature_names[sorted_indices])
mp.bar(x, fi_t[sorted_indices], 
	color='orangered', label='fi_t')
mp.legend()

mp.show()
```

##### 自助聚合

每次从总样本矩阵中以有放回抽样的方式,随机抽取部分样本构建决策树, 这样形成多颗包含不同训练本的决策树. 以削弱某些强势样本对模型预测结果的影响. 提高模型的泛化特性.

##### 随机森林

在自助聚合的基础上, 每次构建决策树模型时, 不仅随机选择部分样本, 而且还随机选择部分特征, 这样的集合算法, 不仅规避了强势样本对预测结果的影响, 而且也削弱了强势特征的影响, 是模型的预测能力更加泛化.

随机森林相关API:

```python
import sklearn.ensemble as se
# 构建随机森林回归器模型
model = se.RandomForestRegressor(
    max_depth=4, 		# 最大深度
    n_estimators=1000, 	# 构建1000棵决策树
    # 子表中最小样本数 若<=这个数字则不再继续划分
	min_samples_slit=2  
)
```

案例: 分析共享单车的需求, 从而判断如何投放.

```python
"""
demo02_bike.py  共享单车案例   随机森林
"""
import numpy as np
import sklearn.utils as su
import sklearn.ensemble as se
import sklearn.metrics as sm
import matplotlib.pyplot as mp

data = np.loadtxt('../ml_data/bike_day.csv', 
	delimiter=',', unpack=False, 
	dtype='U20')
# 获取输入集与输出集
header = data[0, 2:13]
x = np.array(data[1:, 2:13], dtype=float)
y = np.array(data[1:, -1], dtype=float)
# 打乱数据集
x, y = su.shuffle(x, y, random_state=7)
# 拆分训练集,测试集
train_size = int(len(x)*0.9)
train_x, test_x, train_y, test_y = \
	x[:train_size], x[train_size:], \
	y[:train_size], y[train_size:]
# 随机森林模型训练
model=se.RandomForestRegressor(max_depth=10, 
	n_estimators=1000, min_samples_split=2)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
# 使用r2得分验证预测结果
print(sm.r2_score(test_y, pred_test_y))
# 输出特征重要性
fi_day = model.feature_importances_
print(fi_day)
print(header)

# 绘制特征重要性柱状图
mp.figure('Bike', facecolor='lightgray')
mp.subplot(211)
mp.title('Day', fontsize=16)
mp.ylabel('Importances', fontsize=12)
mp.tick_params(labelsize=8)
mp.grid(linestyle=':')
pos = np.arange(fi_day.size)
sorted_i = fi_day.argsort()[::-1]
mp.xticks(pos, header[sorted_i])
mp.bar(pos, fi_day[sorted_i], 
	   color='dodgerblue', label='Bike_Day')
mp.legend()


data = np.loadtxt('../ml_data/bike_hour.csv', 
	delimiter=',', unpack=False, 
	dtype='U20')
# 获取输入集与输出集
header = data[0, 2:14]
x = np.array(data[1:, 2:14], dtype=float)
y = np.array(data[1:, -1], dtype=float)
# 打乱数据集
x, y = su.shuffle(x, y, random_state=7)
# 拆分训练集,测试集
train_size = int(len(x)*0.9)
train_x, test_x, train_y, test_y = \
	x[:train_size], x[train_size:], \
	y[:train_size], y[train_size:]
# 随机森林模型训练
model=se.RandomForestRegressor(max_depth=10, 
	n_estimators=1000, min_samples_split=2)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
# 使用r2得分验证预测结果
print(sm.r2_score(test_y, pred_test_y))
# 输出特征重要性
fi_hour = model.feature_importances_
print(fi_hour)
print(header)

mp.subplot(212)
mp.title('Hour', fontsize=16)
mp.ylabel('Importances', fontsize=12)
mp.tick_params(labelsize=8)
mp.grid(linestyle=':')
pos = np.arange(fi_hour.size)
sorted_i = fi_hour.argsort()[::-1]
mp.xticks(pos, header[sorted_i])
mp.bar(pos, fi_hour[sorted_i], 
	   color='orangered', label='Bike Hour')
mp.legend()
mp.show()
```

### 简单分类(人工分类)

| 特征1 | 特征2 | 输出 |
| ----- | ----- | ---- |
| 3     | 1     | 0    |
| 2     | 5     | 1    |
| 1     | 8     | 1    |
| 6     | 4     | 0    |
| 5     | 2     | 0    |
| 3     | 5     | 1    |
| 4     | 7     | 1    |
| ...   | ...   | ...  |
| 6     | 8     | ?    |

案例:

```python
"""
demo03_sc.py  简单分类
"""
import numpy as np
import matplotlib.pyplot as mp

x = np.array([
	[3, 1],
	[2, 5],
	[1, 8],
	[6, 4],
	[5, 2],
	[3, 5],
	[4, 7],
	[4, -1]])
y = np.array([0, 1, 1, 0, 0, 1, 1, 0])
# 把样本绘制出来
mp.figure('Simple Classification', facecolor='lightgray')
mp.title('Simple Classification', fontsize=16)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')


# 绘制分类边界线
l, r = x[:, 0].min()-1, x[:, 0].max()+1
b, t = x[:, 1].min()-1, x[:, 1].max()+1
n = 500
grid_x, grid_y = np.meshgrid(
	np.linspace(l, r, n),
	np.linspace(b, t, n))
grid_z = np.piecewise(grid_x, 
	[grid_x >= grid_y, grid_y > grid_x], 
	[0, 1])
mp.pcolormesh(grid_x,grid_y,grid_z,cmap='gray')

mp.scatter(x[:, 0], x[:, 1], s=60, c=y,
	marker='o', label='Points', cmap='jet')

mp.legend()
mp.show()
```

### 逻辑分类

| 特征1 | 特征2 | 输出 |
| ----- | ----- | ---- |
| 3     | 1     | 0    |
| 2     | 5     | 1    |
| 1     | 8     | 1    |
| 6     | 4     | 0    |
| 5     | 2     | 0    |
| 3     | 5     | 1    |
| 4     | 7     | 1    |
| ...   | ...   | ...  |
| 6     | 8     | ?    |

通过输入的样本数据, 基于多元线性回归模型求出线性预测方程:

y = w<sub>0</sub> + w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub>

基于损失函数最小化做梯度下降后,得到最优的模型参数: w<sub>0</sub>  w<sub>1</sub> w<sub>2</sub> .  通过得到的线性回归方程进行类别预测, 把x1与x2带入方程得到最终"类别".  但是方程返回的结果是连续值, 不可以直接用于分类业务模型,  所以急需一种方式实现: 连续的预测值 -> 离散的预测值 之间的一个转换. [-∞, ∞] -> {0, 1}
$$
逻辑函数 sigmoid: y= \frac{1}{1+e^{-x}}
$$
该逻辑函数当x>0时, y>0.5;  当x<0时, y<0.5; 可以把样本数据经过线性预测模型求得的值带入逻辑函数的x, 这样的话就可以逻辑函数的返回值看做预测输出被划分为1类别的概率.择概率大的类别作为预测结果. 可以根据该逻辑函数划分2个类别.  

这也是线性函数离散化的一种方式.

逻辑函数的相关API:

```python
import sklearn.linear_model as lm
model = lm.LogisticRegression(
    solver='liblinear', C=正则强度)
model.fit(x, y)
pred_test_y = model.predict(test_x)
```

案例:

```python
"""
demo05_lc.py  逻辑分类  
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.linear_model as lm

x = np.array([
	[3, 1],
	[2, 5],
	[1, 8],
	[6, 4],
	[5, 2],
	[3, 5],
	[4, 7],
	[4, -1]])
y = np.array([0, 1, 1, 0, 0, 1, 1, 0])
# 把样本绘制出来
mp.figure('Simple Classification', facecolor='lightgray')
mp.title('Simple Classification', fontsize=16)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')

# 绘制分类边界线
l, r = x[:, 0].min()-1, x[:, 0].max()+1
b, t = x[:, 1].min()-1, x[:, 1].max()+1
n = 500
grid_x, grid_y = np.meshgrid(
	np.linspace(l, r, n),
	np.linspace(b, t, n))

# 构建逻辑分类器
model = lm.LogisticRegression(
	solver='liblinear', C=10)
model.fit(x, y)
# 把grid_x与grid_y抻平了组成模型的输入,预测输出
test_x = np.column_stack(
	(grid_x.ravel(), grid_y.ravel()))
pred_test_y = model.predict(test_x)
grid_z = pred_test_y.reshape(grid_x.shape)

mp.pcolormesh(grid_x,grid_y,grid_z,cmap='gray')

mp.scatter(x[:, 0], x[:, 1], s=60, c=y,
	marker='o', label='Points', cmap='jet')

mp.legend()
mp.show()
```

**多元分类**

通过多个二元分类器解决多元分类问题.

| 特征1 | 特征2 | ==>  | 所属类别 |
| ----- | ----- | ---- | -------- |
| 4     | 7     | ==>  | A        |
| 3.5   | 8     | ==>  | A        |
| 1.2   | 1.9   | ==>  | B        |
| 5.4   | 2.2   | ==>  | C        |

若拿到一组新的样本, 可以基于二元逻辑分类训练出一个模型, 判断属于A类别的概率. 再基于同样的方法训练处两个模型,分别判断属于B类别/ 属于C类别的概率, 最终选择概率最高的作为新样本的分类结果.

案例:

```python
"""
demo06_mlc.py  多元逻辑分类  
"""
import numpy as np
import matplotlib.pyplot as mp
import sklearn.linear_model as lm

x = np.array([
	[4, 7],
	[3.5, 8],
	[3.1, 6.2],
	[0.5, 1],
	[1, 2],
	[1.2, 1.9],
	[6, 2],
	[5.7, 1.5],
	[5.4, 2.2]])
y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])
# 把样本绘制出来
mp.figure('Logistic Classification', facecolor='lightgray')
mp.title('Logistic Classification', fontsize=16)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')

# 绘制分类边界线
l, r = x[:, 0].min()-1, x[:, 0].max()+1
b, t = x[:, 1].min()-1, x[:, 1].max()+1
n = 500
grid_x, grid_y = np.meshgrid(
	np.linspace(l, r, n),
	np.linspace(b, t, n))

# 构建逻辑分类器
model = lm.LogisticRegression(
	solver='liblinear', C=1000)
model.fit(x, y)
# 把grid_x与grid_y抻平了组成模型的输入,预测输出
test_x = np.column_stack(
	(grid_x.ravel(), grid_y.ravel()))
pred_test_y = model.predict(test_x)
grid_z = pred_test_y.reshape(grid_x.shape)

mp.pcolormesh(grid_x,grid_y,grid_z,cmap='gray')

mp.scatter(x[:, 0], x[:, 1], s=60, c=y,
	marker='o', label='Points', cmap='jet')

mp.legend()
mp.show()
```

### 朴素贝叶斯分类

朴素贝叶斯分类是一种依据统计理论而实现的一种分类方式. 观察一组数据:

| 天气情况 | 穿衣风格 | 约女朋友 | ==>  | 心情    |
| -------- | -------- | -------- | ---- | ------- |
| 0(晴天)  | 0(休闲)  | 0(约了)  | ==>  | 0(高兴) |
| 0        | 1(风骚)  | 1(没约)  | ==>  | 0       |
| 1(多云)  | 1        | 0        | ==>  | 0       |
| 0        | 2(破旧)  | 1        | ==>  | 1(郁闷) |
| 2(下雨)  | 2        | 0        | ==>  | 0       |
| ...      | ...      | ...      | ...  | ...     |
| 0        | 1        | 0        | ==>  | ?       |

通过上述训练样本如何预测:010的心情? 可以依照决策树的方式找相似输入预测输出. 但是如果在样本空间中没有完全匹配的相似样本该如何预测?

**贝叶斯公式:**
$$
P(A,B) = P(A)P(B|A) = P(B)P(A|B) \\
\Downarrow \Downarrow \Downarrow \\
P(A|B) = \frac{P(A)P(B|A)}{P(B)}
$$
例如:

假设一个学校中有60%男生和40%女生. 女生穿裤子的人数和穿裙子的人数相等. 所有男生都穿裤子. 一人在远处随机看到了一个穿裤子的学生, 那么这个学生是女生的概率是多少?

```
P(女) = 0.4
P(裤子|女) = 0.5
P(裤子) = 0.8
P(女|裤子) = P(女)*P(裤子|女)/P(裤子)
          = 0.4 * 0.5 / 0.8 = 0.25
```

根据贝叶斯定理, 如何预测: 晴天并且休闲并且没约并且高兴的概率?

```
P(晴天,休闲,没约,高兴)
P(晴天|休闲,没约,高兴)P(休闲,没约,高兴)
P(晴天|休闲,没约,高兴)P(休闲|没约,高兴)P(没约,高兴)
P(晴天|休闲,没约,高兴)P(休闲|没约,高兴)P(没约|高兴)P(高兴)
(朴素: 条件独立, 特征值之间没有任何关系)
P(晴天|高兴)P(休闲|高兴)P(没约|高兴)P(高兴)
```

朴素贝叶斯相关API:

```python
import sklearn.naive_bayes as nb
# 构建高斯朴素贝叶斯
model = nb.GaussianNB()
model.fit(x, y)
pred_test_y = model.predict(test_x)
```

案例: multiple1.txt

```python
"""
demo07_nb.py  朴素贝叶斯分类
"""
import numpy as np
import sklearn.naive_bayes as nb
import matplotlib.pyplot as mp

data = np.loadtxt('../ml_data/multiple1.txt', 
	unpack=False, delimiter=',')
print(data.shape, data.dtype)
# 获取输入与输出
x = np.array(data[:, :-1])
y = np.array(data[:, -1])

# 绘制这些点, 点的颜色即是点的类别
mp.figure('Naive Bayes', facecolor='lightgray')
mp.title('Naive Bayes', fontsize=16)
mp.xlabel('X', fontsize=14)
mp.ylabel('Y', fontsize=14)
mp.tick_params(labelsize=10)
# 通过样本数据,训练朴素贝叶斯分类模型
model = nb.GaussianNB()
model.fit(x, y)
# 绘制分类边界线
l, r = x[:, 0].min()-1, x[:, 0].max()+1
b, t = x[:, 1].min()-1, x[:, 1].max()+1
n = 500
grid_x, grid_y = np.meshgrid(
	np.linspace(l, r, n),
	np.linspace(b, t, n))
test_x = np.column_stack(
	(grid_x.ravel(), grid_y.ravel()))
pred_test_y = model.predict(test_x)
grid_z = pred_test_y.reshape(grid_x.shape)
mp.pcolormesh(grid_x,grid_y,grid_z,cmap='gray')

mp.scatter(x[:,0], x[:,1], s=60, c=y, 
	cmap='jet', label='Points')
mp.legend()
mp.show()
```

#### 数据集的划分

对于分类问题训练集和测试集的划分不应该用整个样本空间的特定百分比作为训练数据, 而应该在其每一个类别的样本中抽取特定百分比作为训练数据. 最终提高分类的可信度.

sklearn提供了数据集划分的相关API:

```python
import sklearn.model_selection as ms
# 训练集测试集划分
ms.train_test_split(
    输入集, 输出集, 
	test_size=测试集占比,
	random_state=7
)
返回: train_x, test_x, train_y, test_y
```

案例:

```python
"""
demo08_ms.py  训练集测试集划分
"""
import numpy as np
import sklearn.naive_bayes as nb
import matplotlib.pyplot as mp
import sklearn.model_selection as ms

data = np.loadtxt('../ml_data/multiple1.txt', 
	unpack=False, delimiter=',')
print(data.shape, data.dtype)
# 获取输入与输出
x = np.array(data[:, :-1])
y = np.array(data[:, -1])

# 绘制这些点, 点的颜色即是点的类别
mp.figure('Naive Bayes', facecolor='lightgray')
mp.title('Naive Bayes', fontsize=16)
mp.xlabel('X', fontsize=14)
mp.ylabel('Y', fontsize=14)
mp.tick_params(labelsize=10)

# 训练集测试集划分
train_x, test_x, train_y, test_y = \
	ms.train_test_split(
	x, y, test_size=0.25, random_state=7)

# 通过训练样本,训练朴素贝叶斯分类模型
model = nb.GaussianNB()
model.fit(train_x, train_y)
# 对测试样本进行预测, 输出预测精确度
pred_test_y = model.predict(test_x)
# 精确度 = 预测正确的个数/总个数
print((test_y==pred_test_y).sum()/test_y.size)


# 绘制分类边界线
l, r = x[:, 0].min()-1, x[:, 0].max()+1
b, t = x[:, 1].min()-1, x[:, 1].max()+1
n = 500
grid_x, grid_y = np.meshgrid(
	np.linspace(l, r, n),
	np.linspace(b, t, n))
mesh_x = np.column_stack(
	(grid_x.ravel(), grid_y.ravel()))
pred_mesh_y = model.predict(mesh_x)
grid_z = pred_mesh_y.reshape(grid_x.shape)
mp.pcolormesh(grid_x,grid_y,grid_z,cmap='gray')

mp.scatter(test_x[:,0], test_x[:,1], s=60, 
	c=test_y, cmap='jet', label='Train Points')
mp.legend()
mp.show()
```

#### 交叉验证

由于数据集的划分有不确定性, 若随机划分的样本证号处于某类特殊样本, 则得到的训练模型所预测的结果的可信度会受到质疑. 所以要进行多次**交叉验证**, 把样本空间中的所有样本均分成n份, 使用不同的训练集训练模型, 对不同的测试集进行测试并输出指标得分.

交叉验证相关API:

```python
import sklearn.model_selection as ms
# 使用给出的模型,针对输入与输出进行5次交叉验证
# 把每次交叉验证得到的精准度得分以数组的方式返回
score = ms.cross_val_score(
    模型, 输入集, 输出集,
    cv=5,          	   # 交叉验证的次数
    scoring='accuracy' # 指标名称 (精准度)
)
```

案例:

```python
# 通过训练样本,训练朴素贝叶斯分类模型
model = nb.GaussianNB()
# 到底用不用这个模型呢? 交叉验证看一下分数吧
score = ms.cross_val_score(
	model, train_x, train_y, cv=5, 
	scoring='accuracy')
print('CV Accuracy:', score)
```

















