# 机器学习DAY04

#### 交叉验证

由于数据集的划分有不确定性, 若随机划分的样本正好处于某类特殊样本, 则得到的训练模型所预测的结果的可信度会受到质疑. 所以要进行多次**交叉验证**, 把样本空间中的所有样本均分成n份, 使用不同的训练集训练模型, 对不同的测试集进行测试并输出指标得分.

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

**交叉验证的指标**

1. 精准度(accuracy): 分类正确的样本数/总样本数
2. 查准率(precision_weighted): 针对每一类别, 预测正确的样本数 / 预测出来的样本数
3. 召回率(recall_weighted): 针对每一类别, 预测正确的样本数 / 实际存在的样本数

4. f1得分(f1_weighted): 2x查准率x召回率/(查准率+召回率)

案例:

```python
# 到底用不用这个模型呢? 交叉验证看一下分数吧
ac = ms.cross_val_score(
	model, train_x, train_y, cv=5, 
	scoring='accuracy')
print('CV Accuracy:', ac)
pw = ms.cross_val_score(
	model, train_x, train_y, cv=5, 
	scoring='precision_weighted')
print('CV PW:', pw)
rw = ms.cross_val_score(
	model, train_x, train_y, cv=5, 
	scoring='recall_weighted')
print('CV RW:', rw)
fw = ms.cross_val_score(
	model, train_x, train_y, cv=5, 
	scoring='f1_weighted')
print('CV FW:', fw)
```

#### 混淆矩阵

混淆矩阵中每一行和每一列分别对应样本输出中的每一个类别, 行表示实际类别, 列表示预测类别.

|       | A类别 | B类别 | C类别 |
| ----- | ----- | ----- | ----- |
| A类别 | 5     | 0     | 0     |
| B类别 | 0     | 6     | 0     |
| C类别 | 0     | 0     | 7     |

上述的混淆矩阵, 是一个理想的混淆矩阵, 不理想的如下:

|       | A类别 | B类别 | C类别 |
| ----- | ----- | ----- | ----- |
| A类别 | 3     | 1     | 1     |
| B类别 | 0     | 4     | 2     |
| C类别 | 0     | 0     | 7     |

查准率 = 主对角线上的值 /  该值所在列的和

召回率 = 主对角线上的值 / 该值所在行的和 

```python
import sklearn.metrics as sm
# 返回混淆矩阵
m = sm.confusion_matrix(实际输出, 预测输出)
```

案例:

```python
# 输出混淆矩阵
m = sm.confusion_matrix(test_y, pred_test_y)
print(m)

mp.figure('CM')
mp.imshow(m, cmap='gray')
```

#### 分类报告

sklearn提供了分类报告, 不仅可以得到混淆矩阵, 还可以得到交叉验证的查准率/ 召回率/f1得分的结果, 可以方便的分析出哪些样本是异常样本.

```python
cr=sm.classification_report(实际输出, 预测输出)
print(cr)
```

### 决策树分类

决策树分类模型会找到与样本特征匹配的叶子节点然后以投票的方式进行分类. 

在car.txt样本文件中统计小汽车的常见特征信息及小汽车的分类, 使用这些数据可以预测小汽车的等级.

案例: car.txt  基于决策树分类,预测小汽车等级.

1. 读取文本数据, 对每列进行标签编码, 基于随机森林分类器进行模型训练, 进行交叉验证.

```python
"""
demo02_car.py  预测小汽车的等级
"""
import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms

data = np.loadtxt('../ml_data/car.txt', 
	dtype='U20', delimiter=',')
data = data.T
encoders = []
train_x, train_y = [], []
for row in range(len(data)):
	# 创建适用于当前特征的标签编码器
	encoder = sp.LabelEncoder()
	if row < len(data)-1:
		train_x.append(
			encoder.fit_transform(data[row]))
	else:
		train_y = \
			encoder.fit_transform(data[row])
	encoders.append(encoder)
train_x = np.array(train_x).T

# 模型训练
model = se.RandomForestClassifier(max_depth=6, 
	n_estimators=200, random_state=7)
# 交叉验证
print(train_x.shape, train_y.shape)
score = ms.cross_val_score(model, train_x, 
	train_y, cv=4, scoring='f1_weighted')
print(score.mean())
model.fit(train_x, train_y)
```

1. 自定义测试集, 使用模型进行预测.

```python
# 自定义测试集  进行预测
data = [
['high','med','5more','4','big','low','unacc'],
['high','high','4','4','med','med','acc'],
['low','low','2','4','small','high','good'],
['low','med','3','4','med','high','vgood']]
# 训练时如何做的标签编码, 测试时需要使用相同的
# 标签编码器进行编码
data = np.array(data).T
test_x, test_y = [], []
for row in range(len(data)):
	encoder = encoders[row] # 得到标签编码器
	if row < len(data)-1:
		test_x.append(
			encoder.transform(data[row]))
	else:
		test_y = encoder.transform(data[row])
test_x = np.array(test_x).T
pred_test_y = model.predict(test_x)
enc = encoders[-1]
print(enc.inverse_transform(test_y))
print(enc.inverse_transform(pred_test_y))
```

#### 验证曲线

验证曲线:  模型性能(得分) = f(超参数)

```python
train_score,test_score=ms.validation_curve(
	model, 		# 需要验证的模型对象
    输入集, 输出集,  
    'n_estimators',	# 需要进行测试的超参数名称 
    np.arange(50, 550, 50), #超参数选值
    cv=5   # 折叠数
)
```

train_scores的结构:

| 超参数取值 | cv_1  | cv_2  | cv_3  | cv_4  | cv_5  |
| ---------- | ----- | ----- | ----- | ----- | ----- |
| 50         | 0.912 | 0.912 | 0.912 | 0.912 | 0.912 |
| 100        | 0.912 | 0.912 | 0.912 | 0.912 | 0.912 |
| ...        | ...   | ...   | ...   | ...   | ...   |

通过验证曲线, 可以选择模型的较优超参数.

```python
"""
demo03_vc.py  验证曲线
"""
import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms
import matplotlib.pyplot as mp

data = np.loadtxt('../ml_data/car.txt', 
	dtype='U20', delimiter=',')
data = data.T
encoders = []
train_x, train_y = [], []
for row in range(len(data)):
	# 创建适用于当前特征的标签编码器
	encoder = sp.LabelEncoder()
	if row < len(data)-1:
		train_x.append(
			encoder.fit_transform(data[row]))
	else:
		train_y = \
			encoder.fit_transform(data[row])
	encoders.append(encoder)
train_x = np.array(train_x).T

# 模型训练
'''
model = se.RandomForestClassifier(max_depth=6, 
	random_state=7)
# 输出验证曲线 选取最优:n_estimators
train_scores,test_scores=ms.validation_curve(
	model, train_x, train_y, 
	'n_estimators', np.arange(50,550,50),
	cv=5)

ne_scores = test_scores.mean(axis=1)
print(ne_scores)

mp.figure('VC')
mp.title('n_estimators Curve', fontsize=16)
mp.xlabel('n_estimators', fontsize=14)
mp.ylabel('score', fontsize=14)
mp.tick_params(labelsize=12)
mp.grid(linestyle=':')
mp.plot(np.arange(50,550,50), ne_scores,
	linewidth=2, c='dodgerblue', 
	label='n_estimators Curve')
mp.legend()
mp.show()


model = se.RandomForestClassifier(
	n_estimators=150, random_state=7)
# 输出验证曲线 选取最优:max_depth
train_scores,test_scores=ms.validation_curve(
	model, train_x, train_y, 
	'max_depth', np.arange(1, 11),
	cv=5)

md_scores = test_scores.mean(axis=1)
print(md_scores)

mp.figure('VC')
mp.title('max_depth Curve', fontsize=16)
mp.xlabel('max_depth', fontsize=14)
mp.ylabel('score', fontsize=14)
mp.tick_params(labelsize=12)
mp.grid(linestyle=':')
mp.plot(np.arange(1, 11), md_scores,
	linewidth=2, c='orangered', 
	label='max_depth Curve')
mp.legend()
mp.show()
'''

model = se.RandomForestClassifier(
	max_depth=9, n_estimators=150, 
	random_state=7)
model.fit(train_x, train_y)

# 自定义测试集  进行预测
data = [
['high','med','5more','4','big','low','unacc'],
['high','high','4','4','med','med','acc'],
['low','low','2','4','small','high','good'],
['low','med','3','4','med','high','vgood']]
# 训练时如何做的标签编码, 测试时需要使用相同的
# 标签编码器进行编码
data = np.array(data).T
test_x, test_y = [], []
for row in range(len(data)):
	encoder = encoders[row] # 得到标签编码器
	if row < len(data)-1:
		test_x.append(
			encoder.transform(data[row]))
	else:
		test_y = encoder.transform(data[row])
test_x = np.array(test_x).T
pred_test_y = model.predict(test_x)
enc = encoders[-1]
print(enc.inverse_transform(test_y))
print(enc.inverse_transform(pred_test_y))
```

#### 学习曲线

学习曲线: 模型性能 = f(训练集大小)

```python
_,train_score,test_score=ms.learning_curve(
	model, 输入集, 输出集, 
    [0.9, 0.8, 0.7], # 训练集大小序列
    cv=5	# 交叉验证折叠数
)
```

案例: 在小汽车评级案例中使用学习曲线选择训练集大小.

```python

# 验证学习曲线 获取最优训练集大小
train_sizes = np.linspace(0.1, 1, 10)
_, train_scores, test_scores=ms.learning_curve(
	model, train_x, train_y, 
	train_sizes=train_sizes, cv=5)
print(test_scores.mean(axis=1))

mp.figure('Learn Curve')
mp.title('Learn Curve', fontsize=16)
mp.xlabel('train size', fontsize=14)
mp.ylabel('score', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(train_sizes, test_scores.mean(axis=1),
	linewidth=2, c='dodgerblue')
mp.show()
```

### 支持向量机(SVM)

#### 支持向量机原理

1. **寻求最优分类边界** 

   正确:  对大部分样本可以正确的划分类别.

   泛化:  最大化支持向量间距.

   公平:  各类别与分类边界等距.

   简单:  基于线性模型, 直线/平面.

2. **基于核函数的升维变换**

   通过名为核函数的特征变换, 增加新的特征, 使得低维度空间中的线性不可分问题在高维度空间变得线性可分.

**支持向量机的使用**

**线性核函数: linear**  不通过核函数进行维度提升, 仅在原始维度空间中寻求线性分类边界.

```python
import sklearn.svm as svm
model = svm.SVC(kernel='linear')
model.fit(x, y)
pred_test_y = model.predict(test_x)
```

案例: multiple2.txt 使用svm实现分类.

```python

x, y = [],[]
data=np.loadtxt('../ml_data/multiple2.txt', 
	 delimiter=',')
x = data[:, :-1]
y = data[:, -1]
# 拆分训练集与测试集
train_x, test_x, train_y, test_y = \
	ms.train_test_split(x, y, test_size=0.25,
	random_state=5)
# 基于线性核函数的svm绘制分类边界
model=svm.SVC(kernel='linear')
model.fit(train_x, train_y)

# 绘制分类边界线
l, r = x[:, 0].min()-1, x[:, 0].max()+1
b, t = x[:, 1].min()-1, x[:, 1].max()+1
n = 500
grid_x, grid_y = np.meshgrid(
	np.linspace(l, r, n),
	np.linspace(b, t, n))
# 把grid_x与grid_y抻平了组成模型的输入,预测输出
mesh_x = np.column_stack(
	(grid_x.ravel(), grid_y.ravel()))
pred_mesh_y = model.predict(mesh_x)
grid_z = pred_mesh_y.reshape(grid_x.shape)

# 看一看测试集的分类报告
pred_test_y = model.predict(test_x)
cr = sm.classification_report(
	  	test_y, pred_test_y)
print(cr)
```

**多项式核函数: poly** 通过多项式函数增加原始样本特征的高次方幂.

案例: 基于多项式核函数, 训练multiple2.txt

```python
# 基于多项式核函数的svm绘制分类边界
model=svm.SVC(kernel='poly', degree=3)
model.fit(train_x, train_y)
```

**径向基核函数: rbf** , 通过高斯分布函数增加原始样本特征的分布概率作为新的特征.

```python
# C: 正则项
# gamma: 正态分布曲线的标准差
model= svm.SVC(
    kernel='rbf', C=600, gamma=0.01)
```

案例:

```python
# 基于多项式核函数的svm绘制分类边界
model=svm.SVC(kernel='rbf', C=600, gamma=0.01)
model.fit(train_x, train_y)
```

#### 样本类别均衡化

通过样本类别权重的均衡化, 使所占比例较小的样本权重较高,而所占比例较大的样本权重较低, 以此平均化不同类别样本对分类模型的贡献, 提高模型预测性能.

什么情况下会用到样本类别均衡化? 当每个类别的样本容量相差较大时, 有可能会用到样本类别均衡化.

```python
model = svm.SVC(kernel='linear', 
                class_weight='balanced')
```

案例: imbalance.txt

```python
# 基于线性核函数的svm绘制分类边界
model=svm.SVC(kernel='linear', 
			  class_weight='balanced')
model.fit(train_x, train_y)
```

#### 置信概率

根据样本与分类边界距离的远近, 对其预测类别的可信程度进行量化, 离边界越近的样本, 置信概率越低, 反之则越高.

获取样本的置信概率:

```python
model = svm.SVC(....., probability=True)
pred_test_y = model.predict(test_x)
# 获取每个样本的置信概率
置信概率矩阵 = model.predict_proba(样本矩阵)
```

置信概率矩阵的结构:

|       | 类别1 | 类别2 |
| ----- | ----- | ----- |
| 样本1 | 0.8   | 0.2   |
| 样本2 | 0.3   | 0.7   |
| 样本3 | 0.4   | 0.6   |

案例: 

```python
# 整理测试样本 , 绘制每个样本的置信概率
prob_x = np.array([
	[2, 1.5], 
	[8, 9], 
	[4.8, 5.2], 
	[4, 4], 
	[2.5, 7], 
	[7.6, 2], 
	[5.4, 5.9]])
pred_prob_y = model.predict(prob_x)
probs = model.predict_proba(prob_x)
print(probs)
mp.scatter(prob_x[:,0], prob_x[:,1], s=60,
		marker='D', 
		c=pred_prob_y, label='prob points', 
		cmap='rainbow')
```

#### 网格搜索

网格搜索是一种选取最优超参数的解决方案.

获取一个最优超参数的方式可以绘制验证曲线, 但是验证曲线只能每次获取一个最优超参数. 如果多个超参数有很多排列组合情况的话, 可以选择使用网格搜索寻求最优超参数的组合.

网格搜索相关API:

```python
import sklearn.model_selection as ms
model = 决策树模型
# 返回分值最高的模型对象 
model = ms.GridSearchCV(
    	model, 超参数列表, cv=折叠数)
# 直接训练模型
model.fit(输入集, 输出集)
# 获取最好的超参数
model.best_params_
model.best_score_
model.best_estimator_
```

案例: 修改置信概率的案例.

```python
# 基于svm绘制分类边界
model=svm.SVC()
# 使用网格搜索,获取最优模型超参数
params = [
  {'kernel':['linear'],'C':[1,10,100,1000]},
  {'kernel':['poly'],'C':[1],'degree':[2,3]},
  {'kernel':['rbf'],'C':[1,10,100,1000], 
    'gamma':[1, 0.1, 0.01, 0.001]}]
model = ms.GridSearchCV(model, params, cv=5)
model.fit(train_x, train_y)

print(model.best_params_)
print(model.best_score_)
print(model.best_estimator_)
```

#### 案例: 事件预测

案例: event.txt  预测某个时间段是否会出现特殊事件.

```python

```





















