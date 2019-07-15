# 机器学习DAY02

### 线性回归

````python
"""
demo01_linear.py 线性回归
实现线性回归模型梯度下降过程
"""
import numpy as np
import matplotlib.pyplot as mp
import mpl_toolkits.mplot3d as axes3d

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
	losses.append(loss)
	# 把梯度下降的过程进行输出
	print(
		'{:4}> w0={:.8f}, w1={:.8f}, loss={:.8f}'.format(
			epoches[-1], w0[-1], 
			w1[-1], losses[-1]))
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

#绘制随着每次梯度下降过程, w0 w1 loss函数的变化曲线
mp.figure('Training Progress', facecolor='lightgray')
mp.subplot(311)
mp.title('Training W0', fontsize=14)
mp.ylabel('w0', fontsize=12)
mp.grid(linestyle=':')
mp.tick_params(labelsize=10)
mp.plot(epoches, w0[:-1], c='dodgerblue',
	label='w0 Progress')
mp.legend()
mp.subplot(312)
mp.title('Training W1', fontsize=14)
mp.ylabel('w1', fontsize=12)
mp.grid(linestyle=':')
mp.tick_params(labelsize=10)
mp.plot(epoches, w1[:-1], c='orangered',
	label='w1 Progress')
mp.legend()
mp.subplot(313)
mp.title('Training Loss', fontsize=14)
mp.ylabel('loss', fontsize=12)
mp.grid(linestyle=':')
mp.tick_params(labelsize=10)
mp.plot(epoches, losses, c='deepskyblue',
	label='loss Progress')
mp.legend()

# 在三维曲面中绘制梯度下降的过程
grid_w0, grid_w1 = np.meshgrid(
	np.linspace(0, 9, 500), 
	np.linspace(0, 3.5, 500))

grid_loss = np.zeros_like(grid_w0)
for x, y in zip(train_x, train_y):
	grid_loss+=(grid_w0+x*grid_w1 - y)**2 / 2

mp.figure('Loss Function')
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('w0', fontsize=14)
ax3d.set_ylabel('w1', fontsize=14)
ax3d.set_zlabel('loss', fontsize=14)
ax3d.plot_surface(grid_w0, grid_w1, grid_loss,
	rstride=10, cstride=10, cmap='jet')
ax3d.plot(w0[:-1], w1[:-1], losses, 
	'o-', c='orangered', label='BGD', zorder=3)

# 以等高线的方式绘制梯度下降的过程
mp.figure('BGD Contour', facecolor='lightgray')
mp.title('BGD Contour', fontsize=16)
mp.xlabel('w0', fontsize=12)
mp.ylabel('w1', fontsize=12)
mp.tick_params(labelsize=10)
mp.contourf(grid_w0,  grid_w1, grid_loss, 
	10, cmap='jet')
cntr = mp.contour(grid_w0, grid_w1, grid_loss, 
	10, color='black')
mp.clabel(cntr, inline_spacing=0.1, fmt='%.2f',
	fontsize=8)
mp.plot(w0, w1, 'o-', c='red')
mp.tight_layout()
mp.show()
````

**sklearn提供的线性回归相关API:**

```python
import sklearn.linear_model as lm
# 获取线性回归模型
model = lm.LinearRegression()
# 模型训练 
# 输入集: x数据样本矩阵   
# 输出集: 列向量
model.fit(输入集, 输出集)
# 通过输入样本得到预测输出
预测输出 = model.predict(输入样本)
```

案例: single.txt

```python
"""
demo02_lr.py  线性回归
"""
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp

x ,y = np.loadtxt('../ml_data/single.txt', 
	delimiter=',', usecols=(0,1), 
	unpack=True)
# 把x改为n行1列  这样才可以作为输入交给模型训练
x = x.reshape(-1, 1)
# 训练模型
model = lm.LinearRegression()
model.fit(x, y)
pred_y = model.predict(x)

mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=18)
mp.xlabel('X', fontsize=16)
mp.ylabel('Y', fontsize=16)
mp.tick_params(labelsize=12)
mp.grid(linestyle=':')
mp.scatter(x, y, s=60, c='dodgerblue', 
	label='Points')
mp.plot(x, pred_y, c='orangered', linewidth=2,
	label='Regression Line')
mp.legend()
mp.show()
```

#### 评估训练结果误差(metrics)

线性回归模型训练完毕后, 可以利用测试集评估训练结果的误差. sklearn.metrics模块提供了计算模型误差的几个常用算法:

```python
import slearn.metrics as sm
# 平均绝对值误差  1/m∑|预测输出-真实输出|
sm.mean_absolute_error(y, pred_y)
# 平均平方误差  sqrt(1/m∑(预测输出-真实输出)^2)
sm.mean_squared_error(y, pred_y)
# 中位数绝对值误差  median(|预测输出-真实输出|)
sm.median_absolute_error(y, pred_y)
# r2得分 (0,1]的一个分值,分数越高,误差越小
sm.r2_score(y, pred_y)
```

#### 模型的保存和加载

模型训练是一个耗时的过程, 一个优秀的机器学习模型是非常宝贵的. 所以当模型训练完毕后,可以把模型保存在磁盘中, 在需要的时候可以从磁盘中重新加载模型. 不再需要重新训练.

```python
import pickle
# 保存模型
pickle.dump(model, 磁盘文件)
# 加载模型
model = pickle.load(磁盘文件)
```

案例: 把训练好的模型持久化.

```python
# 从文件中加载模型对象
with open('../ml_data/linear.pkl', 'rb') as f:
	model = pickle.load(f)
	print('load success.')

pred_y = model.predict(x)
```

### 岭回归

普通的线性回归模型使用基于梯度下降的最小二乘法, 在最小化损失函数的前提下, 寻找最优模型参数. 在此过程中, 包括少数的异常样本在内的全部训练数据都会对最终的模型参数造成相等程度的影响, 并且异常值对模型所带来的影响无法在训练过程中被识别出来. 为此, 岭回归在模型迭代过程中增加了正则项, 用来限制模型参数对异常样本的匹配程度, 进而提高模型面对大多数正常样本的拟合精度.

```python
import sklearn.linear_model as lm
model = lm.Ridge(
    正则强度, 
    fit_intercept=是否训练截距, 
	max_iter=最大迭代次数
)
model.fit(输入,输出)
预测输出 = model.predict(输入)
```

案例: abnormal.txt

```python
"""
demo05_ridge.py  岭回归
"""
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp
import sklearn.metrics as sm

x ,y = np.loadtxt('../ml_data/abnormal.txt', 
	delimiter=',', usecols=(0,1), 
	unpack=True)
# 把x改为n行1列  这样才可以作为输入交给模型训练
x = x.reshape(-1, 1)
mp.figure('Ridge Regression', facecolor='lightgray')
mp.title('Ridge Regression', fontsize=18)
mp.xlabel('X', fontsize=16)
mp.ylabel('Y', fontsize=16)
mp.tick_params(labelsize=12)
mp.grid(linestyle=':')
mp.scatter(x, y, s=60, c='dodgerblue', 
	label='Points')

# 使用线性回归, 绘制回归线
model = lm.LinearRegression()
model.fit(x, y)
pred_y = model.predict(x)
mp.plot(x, pred_y, c='orangered', 
		label='Linear Regression Line')

# 使用岭回归, 绘制回归线
model = lm.Ridge(150, fit_intercept=True, 
	    max_iter=1000)
model.fit(x, y)
pred_y = model.predict(x)
mp.plot(x, pred_y, c='limegreen', 
		label='Ridge Regression Line')

mp.legend()
mp.show()
```

#### 多项式回归

一元多项式的一般形式:

y = w<sub>0</sub> + w<sub>1</sub> x +  w<sub>2</sub> x<sup>2</sup> + w<sub>3</sub> x<sup>3</sup> + ...  w<sub>d</sub> x<sup>d</sup>

把一元多项式函数看做多元线性方程:

y = w<sub>0</sub> + w<sub>1</sub> x<sub>1</sub> +  w<sub>2</sub> x<sub>2</sub> + w<sub>3</sub> x<sub>3</sub> + ...  w<sub>d</sub> x<sub>d</sub> 

所以一元多项式回归即可以看做多元线性回归, 可以使用LinearRegression模型对样本数据进行模型训练.

1. 将一元多项式回归问题转换为多元线性回归问题.(只需给出最高次项的次数即可).
2. 将1步骤中得到结果中w<sub>1</sub> w<sub>2</sub>  .. 当做样本特征, 交给线性回归器训练多元线性模型. 最终得到一组w<sub>0</sub> w<sub>1</sub> ...使得损失函数接近极小值.

```python
import sklearn.pipeline as pl
import sklearn.preprocessing as sp
import sklearn.linear_model as lm
# 通过管线(pipeline)把两个步骤连在一起执行
# 1. 多项式特征扩展器
# 2. 多元线性模型
model = pl.make_pipeline(
	sp.PolynomialFeatures(4),
    lm.LinearRegression()
)
```

案例: single.txt

```python
"""
demo06_polyfit.py  多项式回归
"""
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp
import sklearn.metrics as sm
import sklearn.preprocessing as sp
import sklearn.pipeline as pl

x ,y = np.loadtxt('../ml_data/single.txt', 
	delimiter=',', usecols=(0,1), 
	unpack=True)
# 把x改为n行1列  这样才可以作为输入交给模型训练
x = x.reshape(-1, 1)
# 训练多项式回归模型
model = pl.make_pipeline(
	sp.PolynomialFeatures(10), 
	lm.LinearRegression()
)
model.fit(x, y)
pred_y = model.predict(x)
# 为了绘制多项式模型曲线, 构建1000个点
test_x = np.linspace(x.min(), x.max(), 1000)
test_x = test_x.reshape(-1, 1)
pred_test_y = model.predict(test_x)


# 评估回归模型的误差
# 平均绝对值误差  1/m∑|预测输出-真实输出|
print(sm.mean_absolute_error(y, pred_y))
# 平均平方误差  sqrt(1/m∑(预测输出-真实输出)^2)
print(sm.mean_squared_error(y, pred_y))
# 中位数绝对值误差  median(|预测输出-真实输出|)
print(sm.median_absolute_error(y, pred_y))
# r2得分 (0,1]的一个分值,分数越高,误差越小
print(sm.r2_score(y, pred_y))

mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=18)
mp.xlabel('X', fontsize=16)
mp.ylabel('Y', fontsize=16)
mp.tick_params(labelsize=12)
mp.grid(linestyle=':')
mp.scatter(x, y, s=60, c='dodgerblue', 
	label='Points')
mp.plot(test_x, pred_test_y, c='orangered', 
	linewidth=2, label='Regression Line')
mp.legend()
mp.show()
```

过于简单的模型, 无论对于训练数据还是测试数据都无法给出足够高的预测精度, 这种现象称为欠拟合.

过于复杂的模型, 对于训练数据可以给出足够高的预测精度, 但是对于测试数据精度反而低. 这种现象称为过拟合.(模型训练过于依赖训练集)

所以一个性能可以接受的模型应该对训练集与测试集数据都有接近的预测精度, 而且精度不能太低.

### 决策树

#### 基本算法原理

核心思想: 相似的输入必会产生相似的输出. 

年龄:   1-青年,  2-中年,  3-老年

学历:   1-本科,  2-硕士,  3-博士

经历:   1-出道,  2-一般,  3-老手,  4-骨灰

性别:   1-男性,  2-女性

| 年龄 | 学历 | 经历 | 性别 | 薪资  |
| ---- | ---- | ---- | ---- | ----- |
| 1    | 1    | 1    | 1    | 6000  |
| 2    | 1    | 3    | 1    | 10000 |
| 3    | 3    | 4    | 1    | 50000 |
| ...  | ...  | ...  | ...  | ...   |
| 1    | 3    | 2    | 2    | ?     |

为了提高搜索效率, 使用树形数据结构处理样本数据:
$$
年龄=1 \left\{
\begin{aligned}
学历=1 \\
学历=2 \\
学历=3 \\
\end{aligned}
\right.
年龄=2 \left\{
\begin{aligned}
学历=1 \\
学历=2 \\
学历=3 \\
\end{aligned}
\right.
年龄=3 \left\{
\begin{aligned}
学历=1 \\
学历=2 \\
学历=3 \\
\end{aligned}
\right.
$$
首先从训练样本矩阵中选择第一个特征进行子表划分, 使每个子表中该特征的值全部相同. 然后再在每个子表中选择下一个特征, 按照同样的规则继续划分更小的子表, 不断重复直到所有的特征用完为止.  此时便得到叶级子表, 其中所有样本的特征值完全相同.  

对于待预测样本, 根据每一个特征值, 选择对应的子表, 逐一匹配, 直到找到与之完全匹配的叶级子表, 用该子表中样本的输出, 通过平均(回归) 或者投票(分类) 为待预测样本提供输出.

决策树相关API:

```python
import sklearn.tree as st
# 创建决策树模型 
# max_depth: 树的最大深度
model=st.DecisionTreeRegressor(max_depth=4)
model.fit(x, y)
pred_y = model.predict(test_x)
```

案例: 预测波士顿房屋价格.

```python
"""
demo07_house.py  预测房屋价格
"""
import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.tree as st
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
model=st.DecisionTreeRegressor(max_depth=6)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
```

**工程优化**

决策树在使用时不必用尽所有的特征, 叶级子表中允许混杂不同的特征值, 以此降低决策树的高度.所以在精度牺牲可接受的情况下, 可以降低决策树的高度, 提高模型的性能. 

通常情况下,可以优先选择使**信息熵**减少量最大的特征作为划分子表的依据.







































