# 机器学习DAY05

#### 案例:事件预测

```python
"""
demo11_event.py 事件预测
"""
import numpy as np
import sklearn.preprocessing as sp
import sklearn.model_selection as ms
import sklearn.svm as svm

# 模仿LabelEncoder的接口 设计数字编码器
class DigitEncoder():

    def fit_transform(self, y):
        return y.astype(int)

    def transform(self, y):
    	return y.astype(int)

    def inverse_transform(self, y):
    	return y.astype(str)

data = np.loadtxt('../ml_data/events.txt', 
       delimiter=',', dtype='U20')
# 转置后删掉1列
data = np.delete(data.T, 1, axis=0)
# 整理训练集
encoders, x = [], [] 
for row in range(len(data)):
	# 选择编码器, 如果是数字,则用自定义编码器
	if data[row][0].isdigit():
		encoder = DigitEncoder()
	else:
		encoder = sp.LabelEncoder()

	encoders.append(encoder)

	if row < len(data)-1: 
		x.append(
    		encoder.fit_transform(data[row]))
	else:
		y = encoder.fit_transform(data[row])

x = np.array(x).T
# 拆分训练集与测试集
train_x, test_x, train_y, test_y = \
    ms.train_test_split(x, y, test_size=0.25,
	random_state=7)
# 选择模型, 开始训练
model = svm.SVC(kernel='rbf', 
			    class_weight='balanced')
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
# 输出精确度
print((pred_test_y==test_y).sum()/test_y.size)


# 模拟接收参数: 预测输入  从而预测输出
data = [['Monday','13:30:00','22','31']]
data = np.array(data).T
x = []
for row in range(len(data)):
	encoder = encoders[row]
	x.append(encoder.transform(data[row]))
x = np.array(x).T
pred_y = model.predict(x)
print(encoders[-1].inverse_transform(pred_y))
```

**支持向量机也可以做多元分类.**

#### 案例: 交通流量预测(回归)

支持向量机也可以做回归业务.  traffic.txt

```python
"""
demo02_traffic.py 支持向量机
"""
import numpy as np
import sklearn.preprocessing as sp
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm

class DigitEncoder():

    def fit_transform(self, y):
        return y.astype(int)

    def transform(self, y):
    	return y.astype(int)

    def inverse_transform(self, y):
    	return y.astype(str)

data = np.loadtxt('../ml_data/traffic.txt', 
	delimiter=',', dtype='U20')
data = data.T
encoders, x = [], []
for row in range(len(data)):
	if data[row][0].isdigit():
		encoder = DigitEncoder()
	else:
		encoder = sp.LabelEncoder()
	encoders.append(encoder)
	# 整理输入集
	if row < len(data)-1:
		x.append(
			encoder.fit_transform(data[row]))
	else:
		y = encoder.fit_transform(data[row])
# 整理数据集
x = np.array(x).T
# 拆分测试集 训练集 
train_x, test_x, train_y, test_y = \
    ms.train_test_split(x, y, test_size=0.25, 
	random_state=7)
# 创建模型, 模型训练
model = svm.SVR(kernel='rbf', C=10)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))

# 结果预测
data=[['Tuesday','13:35','San Francisco','yes']]
data = np.array(data).T

x = []
for row in range(len(data)):
	encoder = encoders[row]
	x.append(encoder.transform(data[row]))
x = np.array(x).T
pred_y = model.predict(x)
print(int(pred_y))
```

### 聚类

分类(class) 与 聚类 (cluster) 不同, 分类属于有监督学习, 聚类属于无监督学习模型.  聚类讲究使用一些算法把样本划分为n个群落. 一般情况下,这种算法都需要计算欧氏距离. 

欧氏距离(欧几里得距离):
$$
P(x_1)-P(x_2): |x_1-x_2| = \sqrt{(x_1-x_2)^2}\\
p(x_1,y_1)-p(x_2,y_2):  \sqrt{(x_1-x_2)^2 + (y_1-y_2)^2} \\
p(x_1,y_1,z_1)-p(x_2,y_2,z_2):  \sqrt{(x_1-x_2)^2 + (y_1-y_2)^2 + (z_1-z_2)^2}
$$

#### K均值算法

第一步: 随机选择K个样本作为K个聚类中心, 计算每个样本到各个聚类中心的欧式距离, 将该样本分配到与之距离最近的聚类中心所在的类别中.

第二步: 根据第一步得到的聚类划分, 分别计算每个聚类所有样本的几何中心, 将几何中心作为新的聚类中心,重复第一步. 直到计算所得几何中心与聚类中心重合或接近重合为止.

**注意:**

1. 聚类数K必须事先已知. 可以借助某些指标,选择最好的K.
2. 聚类中心的初始选择会影响到最终的聚类划分的结果. 初始重新样本尽量选择距离较远的样本.

K均值算法相关API:

```python
import sklearn.cluster as sc
#n_clusters: 聚类数
model = sc.KMeans(n_clusters=3)
model.fit(x)
# 获取聚类中心
centers = model.cluster_centers_
```

案例: multiple3.txt

```python
"""
demo03_kmeans.py k均值算法
"""
import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp

x = np.loadtxt('../ml_data/multiple3.txt', 
	delimiter=',')
# KMeans聚类
model = sc.KMeans(n_clusters=4)
model.fit(x)
centers = model.cluster_centers_
print(centers)
pred_y = model.predict(x)
# 划分聚类边界
l, r = x[:, 0].min()-1, x[:, 0].max()+1
b, t = x[:, 1].min()-1, x[:, 1].max()+1
n = 500
grid_x, grid_y = np.meshgrid(
	np.linspace(l, r, n),
	np.linspace(b, t, n))
mesh_x = np.column_stack((grid_x.ravel(), 
	grid_y.ravel()))
pred_mesh_y = model.predict(mesh_x)
grid_z = pred_mesh_y.reshape(grid_x.shape)

mp.figure('Kmeans', facecolor='lightgray')
mp.title('Kmeans', fontsize=16)
mp.xlabel('X',fontsize=14)
mp.ylabel('Y',fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x,grid_y,grid_z,cmap='gray')
mp.scatter(x[:,0], x[:,1], c=pred_y, cmap='jet',
		label='points')
# 绘制聚类中心点
mp.scatter(centers[:,0], centers[:,1],
	marker='+', s=230, c='orangered')
mp.legend()
mp.show()
```

#### 图像量化

Kmeans聚类算法可以应用于图像量化领域. 通过KMeans算法可以把一张图像所包含的颜色值进行聚类划分. 得到划分后的聚类中心后, 把靠近某个聚类中的点的亮度值改为聚类中心值, 由此生成新的图片. 达到图像降维的目的. 这个过程称为图像量化.  

图像量化可以很好的保存图像的轮廓, 降低机器识别的难度.

案例:  lily.jpg

```python
"""
demo04_qu.py  图像量化  KMeans聚类
"""
import numpy as np
import scipy.misc as sm
import scipy.ndimage as sn
import sklearn.cluster as sc
import matplotlib.pyplot as mp

img = sm.imread('../ml_data/lily.jpg', True)
# 图像量化
x = img.reshape(-1, 1)
model = sc.KMeans(n_clusters=4)
model.fit(x)
y = model.labels_
print(y.shape)
# 把每个亮度值修改为相应的聚类中心值
centers = model.cluster_centers_.ravel()
print(centers.shape, centers)
# 使用numpy的掩码操作 修改y数组的每个值
result = centers[y].reshape(img.shape)
mp.figure('Image')
mp.subplot(121)
mp.xticks([])
mp.yticks([])
mp.imshow(img, cmap='gray')
mp.subplot(122)
mp.xticks([])
mp.yticks([])
mp.imshow(result, cmap='gray')
mp.tight_layout()
mp.show()
```

#### 均值漂移算法

首先嘉定样本空间中的每个聚类均服从某种已知的概率分布规则, 然后用不同的概率密度函数拟合样本中的统计直方图, 不断移动密度函数的中心位置, 直到获得最佳拟合效果为止.这些概率密度函数的峰值点就是聚类的中心, 再根据每个样本距离各个中心的距离, 选择最近的聚类中心所属的类别作为该样本的类别.

均值漂移算法的特点:

1. 聚类数不必事先已知, 算法会自动识别出统计直方图的中心数量.
2. 聚类中心不依据于最初假定, 聚类划分的结果相对稳定.
3. 样本空间应该服从某种概率分布规则, 某则算法的准确性将会大打折扣.

均值漂移相关的API:

```python
# x: 输入 n_samples: 样本数量
# quantile: 量化宽度 (直方图一条的宽度)
bw = sc.estimate_bandwidth(
    x, n_samples=len(x), quantile=0.1)
# 构建均值漂移模型
model = sc.MeanShift(bandwidth=bw)
```

案例: multiple3.txt  

```python
"""
demo05_meanshift.py 均值漂移
"""
import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp

x = np.loadtxt('../ml_data/multiple3.txt', 
	delimiter=',')

# 均值漂移实现聚类划分

bw = sc.estimate_bandwidth(
	x, n_samples=len(x), quantile=0.2)
model = sc.MeanShift(bandwidth=bw)

model.fit(x)
centers = model.cluster_centers_
print(centers)
pred_y = model.predict(x)
# 划分聚类边界
l, r = x[:, 0].min()-1, x[:, 0].max()+1
b, t = x[:, 1].min()-1, x[:, 1].max()+1
n = 500
grid_x, grid_y = np.meshgrid(
	np.linspace(l, r, n),
	np.linspace(b, t, n))
mesh_x = np.column_stack((grid_x.ravel(), 
	grid_y.ravel()))
pred_mesh_y = model.predict(mesh_x)
grid_z = pred_mesh_y.reshape(grid_x.shape)

mp.figure('MeanShift', facecolor='lightgray')
mp.title('MeanShift', fontsize=16)
mp.xlabel('X',fontsize=14)
mp.ylabel('Y',fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x,grid_y,grid_z,cmap='gray')
mp.scatter(x[:,0], x[:,1], c=pred_y, cmap='jet',
		label='points')
# 绘制聚类中心点
mp.scatter(centers[:,0], centers[:,1],
	marker='+', s=230, c='orangered')
mp.legend()
mp.show()
```

#### 凝聚层次算法

首先假定每个样本都是一个独立的聚类, 如果统计出来的聚类数大于期望的聚类数, 则从每个样本出发, 寻找离自己最近的另外一个样本, 与之聚集, 形成更大的聚类. 同时另总聚类数减少, 不断重复以上过程, 直到统计出来的聚类总数达到期望值为止.

凝聚层次算法的特点:

1. 凝聚数量必须事先已知. 可以借助于某些指标, 优选参数.
2. 没有聚类中心的概念, 因此只能在训练集中划分聚类, 但不能对训练集以外的未知样本确定其归属.
3. 在确定被凝聚样本时, 除了以距离作为条件以外, 还可以根据连续性来确定被聚集的样本.

凝聚层次相关API:

```python
# 构建凝聚层次聚类模型
model = sc.AgglomerativeClustering(
        n_clusters=4)
pred_y = model.fit_predict(x)
```

案例: multiple3.txt

```python
"""
demo06_agglomerative_clustering.py 
凝聚层次算法
"""
import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp

x = np.loadtxt('../ml_data/multiple3.txt', 
	delimiter=',')

# 凝聚层次实现聚类划分
model = sc.AgglomerativeClustering(
			n_clusters=4)
pred_y = model.fit_predict(x)

mp.figure('AgglomerativeClustering', facecolor='lightgray')
mp.title('AgglomerativeClustering', fontsize=16)
mp.xlabel('X',fontsize=14)
mp.ylabel('Y',fontsize=14)
mp.tick_params(labelsize=10)
mp.scatter(x[:,0], x[:,1], c=pred_y, cmap='jet',
		label='points')
mp.legend()
mp.show()
```

案例: 以连续性为条件进行聚类划分.

```python
"""
demo06_agglomerative_clustering.py 
凝聚层次算法
"""
import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp
import sklearn.neighbors as nb

x = np.loadtxt('../ml_data/multiple3.txt', 
	delimiter=',')

# 凝聚层次实现聚类划分 以连续性为条件
# 近邻筛选器
conn = nb.kneighbors_graph(
	   x, 10, include_self=False)
model = sc.AgglomerativeClustering(
			linkage='average',
			n_clusters=4, connectivity=conn)
pred_y = model.fit_predict(x)

mp.figure('AgglomerativeClustering2', facecolor='lightgray')
mp.title('AgglomerativeClustering2', fontsize=16)
mp.xlabel('X',fontsize=14)
mp.ylabel('Y',fontsize=14)
mp.tick_params(labelsize=10)
mp.scatter(x[:,0], x[:,1], c=pred_y, cmap='jet',
		label='points')
mp.legend()

mp.show()
```

#### 轮廓系数

轮廓系数用于评估一个聚类模型的性能. 一个好的聚类: 内密外疏. 同一个聚类内部的样本要足够密集, 不同聚类之间的样本要足够稀疏.

轮廓系数的计算规则: 针对样本空间中的一个特定样本, 计算它与所在聚类其它样本的平均距离a, 以及该样本与距离最近的另一个聚类中所有的样本的平均距离b. 那么该样本的轮廓系数为(b-a)/max(a,b).   若将整个样本空间中所有样本的轮廓系数取算数平均值, 就可以把该结果作为聚类划分的指标.

该公式结果处于:[-1, 1].  -1代表分类效果比较差, 1代表分类效果好. 0代表聚类重叠, 没有很好的划分聚类.

```python
import sklearn.metrics as sm
score = sm.silhouette_score(
    输入集, 输出集, 
    sample_size=样本数,
    # 距离算法: euclidean 欧几里得距离
	metric='euclidean' 
)
```

案例:

```python
# 输出轮廓系数
score = sm.silhouette_score(x, pred_y, 
	sample_size=len(x), metric='euclidean')
print(score)
```

#### DBSCAN算法

从样本空间中任意选择一个样本, 以事先给定的半径做圆. 凡是被该圆圈中的样本都视为与该样本处于同样的聚类. 以这些被圈中样本为圆心继续做圆.不断的扩大被圈中样本的规模, 直到没有新的样本加入为止, 由此得到一个聚类. 

在剩余样本中重复以上过程,直到耗尽样本空间中所有的样本为止.

DBSCAN算法的特点:

1. 实现给定的半径会影响最后的聚类效果, 可以根据轮廓系数选择较优的方案.

2. 根据聚类的形成过程, DBSCAN算法支持把样本分为3类:

   **外周样本:** 被其他样本聚集到某个聚类中, 但无法引入新样本的样本.

   **孤立样本:** 聚类中样本数低于所设置的下限, 则不称其为聚类, 反之称为孤立样本.

   **核心样本:** 除了外周样本和孤立样本外的其他样本.

```python
# 构建DBSCAN聚类模型
# eps: 半径
# min_samples: 最小样本数,若低于该值,则为孤立样本
model = sc.DBSCAN(eps=1, min_samples=5)
model.fit(x)
# 获取核心样本的索引
core_indices=best_model.core_sample_indices_
```

案例: perf.txt

```python
"""
demo08_dbscan.py dbscan算法
"""
import numpy as np
import sklearn.cluster as sc
import sklearn.metrics as sm
import matplotlib.pyplot as mp

x = np.loadtxt('../ml_data/perf.txt', 
		       delimiter=',')

# 准备训练模型相关数据
epsilons, scores, models = \
	np.linspace(0.3, 1.2, 10), [], []
# 遍历所有的半径, 训练模型, 查看得分
for epsilon in epsilons:
	model=sc.DBSCAN(eps=epsilon,min_samples=5)
	model.fit(x)
	score=sm.silhouette_score(x, model.labels_, 
		sample_size=len(x), metric='euclidean')
	scores.append(score)
	models.append(model)
# 转成ndarray数组
scores = np.array(scores)
best_i = scores.argmax() # 最优分数的索引
best_eps = epsilons[best_i]
best_sco = scores[best_i]
print(best_eps)
print(best_sco)
# 获取最优模型
best_model = models[best_i]

# 对输入x进行预测得到预测类别
pred_y = best_model.fit_predict(x)

# 获取孤立样本, 外周样本, 核心样本
core_mask = np.zeros(len(x), dtype=bool)
# 获取核心样本的索引, 把对应位置的元素改为True
core_mask[best_model.core_sample_indices_]=True
# 孤立样本的类别标签为-1
offset_mask = best_model.labels_ == -1
# 外周样本掩码 (不是核心也不是孤立样本)
p_mask = ~(core_mask | offset_mask)

# 绘制这些样本数据
mp.figure('DBSCAN cluster', facecolor='lightgray')
mp.title('DBSCAN cluster', fontsize=16)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
# 绘制核心样本
mp.scatter(x[core_mask][:,0], x[core_mask][:,1],
	s=60, cmap='brg', c=pred_y[core_mask])
# 绘制外周样本
mp.scatter(x[p_mask][:,0], x[p_mask][:,1],
	s=60, cmap='brg', c=pred_y[p_mask], 
	alpha=0.5)
# 绘制孤立样本
mp.scatter(x[offset_mask][:,0], 
	x[offset_mask][:,1], s=60, c='gray')

mp.show()
```

### 推荐引擎

目的: 把用户最需要的内容找到并推荐给用户.

针对不用的业务需求, 一般情况下推荐流程:

1. 根据当前用户信息, 寻找相似用户
2. 根据相似用户的行为, 选择推荐内容.
3. 对推荐内容进行重要性排序, 最终推荐给用户.



针对不同推荐业务场景都需要分析相似样本. 统计相似样本可以基于欧式距离分数.(也可以基于皮氏距离分数)
$$
欧式距离分数= \frac{1}{1+欧式距离}
$$
该欧式距离分数区间处于: (0,1], 越趋近于0, 样本间的欧式距离越远,样本越不相似; 越趋近于1, 则样本间的欧式距离越近, 越相似.

|      | a    | b    | c    | d    | ...  |
| ---- | ---- | ---- | ---- | ---- | ---- |
| a    | 1    | 0.4  | 0.8  | 0.1  | ...  |
| b    | 0.4  | 1    | 0.9  | 0.2  | ...  |
| c    | 0.8  | 0.9  | 1    | 0.6  | ...  |
| d    | 0.1  | 0.2  | 0.6  | 1    | ...  |
| ...  | ...  | ...  | ...  | ...  | ...  |

















