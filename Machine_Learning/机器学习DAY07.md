# 机器学习DAY07

### 语音识别

语音识别可以实现通过一段音频信息(wav波) 识别出音频的内容. 

通过傅里叶变换, 可以将时间域的声音分解为一系列不同频率的正弦函数的叠加. 通过频率谱线的特殊分布, 建立音频内容与文本之间的对应关系, 以此作为模型训练的基础.

#### 语音识别

梅尔频率倒谱系数(MFCC) 描述了与声音内容密切相关的13个特殊频率所对应的能量分布. 那么我们就可以使用梅尔频率倒谱系数(MFCC)矩阵作为语音识别的特征.  基于隐马尔科夫模型进行模式识别, 找到测试样本最匹配的声音模型, 从而识别语音内容.

1. 准备多个声音样本作为训练数据. 并且为每个音频都标明其类别.
2. 读取每一个音频文件, 获取音频文件的mfcc矩阵.
3. 以mfcc作为训练样本, 进行训练.
4. 对测试样本进行测试.  (基于隐马模型)

MFCC相关API:

```python
import scipy.io.wavfile as wf
import python_speech_features as sf

sample_rate, sigs = wf.read('../xx.wav')
mfcc = sf.mfcc(sigs, sample_rate)
```

案例:

```python
"""
demo01_mfcc.py  MFCC提取
"""
import scipy.io.wavfile as wf
import python_speech_features as sf
import matplotlib.pyplot as mp

sample_rate, sigs=wf.read(
	'../ml_data/speeches/training/banana/banana01.wav')
mfcc = sf.mfcc(sigs, sample_rate)
print(mfcc.shape)

mp.matshow(mfcc.T, cmap='gist_rainbow')
mp.title('MFCC')
mp.ylabel('Features', fontsize=14)
mp.xlabel('Samples', fontsize=14)
mp.tick_params(labelsize=10)
mp.show()
```

隐马尔科夫模型相关API:

```python
import hmmlearn.hmm as hl
# 构建隐马模型 
# n_components: 用几个高斯函数拟合样本数据
# covariance_type:使用相关矩阵辅对角线进行相关性比较
# n_iter: 最大迭代上限
model = hl.GaussianHMM(
    n_components=4, 
    covariance_type='diag', 
	n_iter=1000)
model.fit(mfccs)
# 通过训练好的隐马模型  验证音频mfcc的得分 
# 匹配度越好, 得分越高
score = model.score(test_mfcc)
```

案例:

```python
"""
demo02_speech.py   语音识别
"""
import os 
import numpy as np
import scipy.io.wavfile as wf
import python_speech_features as sf
import hmmlearn.hmm as hl

def search_files(directory):
	directory = os.path.normpath(directory)

	# {'apple':[dir,dir,dir], 'banana':[dir..]}
	objects = {}
	#当前目录, 当前目录子目录, 文件列表
	for curdir,subdirs,files in \
					os.walk(directory):
		for file in files:
			if file.endswith('.wav'):
				label = curdir.split(os.path.sep)[-1]
				if label not in objects:
					objects[label] = []
				path = os.path.join(curdir, file)
				objects[label].append(path)
	return objects


train_samples = \
	search_files('../ml_data/speeches/training')

# 整理训练集, 把每一个类别中的音频的mfcc
# 摞在一起, 基于隐马模型开始训练.
train_x, train_y = [], []
for label, filenames in train_samples.items():
	mfccs = np.array([])
	for filename in filenames:
		sample_rate, sigs = wf.read(filename)
		mfcc = sf.mfcc(sigs, sample_rate)
		if len(mfccs) == 0:
			mfccs = mfcc
		else:
			mfccs = np.append(mfccs, mfcc, axis=0)
	train_x.append(mfccs)
	train_y.append(label)

# 基于隐马模型进行训练, 把所有类别的模型都存起来
# 一共7个类别循环7次
models = {}
for mfccs, label in zip(train_x, train_y):
	model = hl.GaussianHMM(n_components=4, 
		covariance_type='diag', n_iter=1000)
	models[label] = model.fit(mfccs)

# 读取测试集中的文件, 使用每个模型对文件进行
# 评分, 取分值大的模型对应的label作为预测类别
test_samples = \
	search_files('../ml_data/speeches/testing')

# 整理测试集, 提取每一个文件的mfcc
test_x, test_y = [], []
for label, filenames in test_samples.items():
	mfccs = np.array([])
	for filename in filenames:
		sample_rate, sigs = wf.read(filename)
		mfcc = sf.mfcc(sigs, sample_rate)
		if len(mfccs) == 0:
			mfccs = mfcc
		else:
			mfccs = np.append(mfccs, mfcc, axis=0)
	test_x.append(mfccs)
	test_y.append(label)

# 使用7个模型, 对每一个文件进行预测得分.
pred_test_y = []
# test_x一共7个样本, 遍历7次, 每次验证1个文件
for mfccs in test_x:
	best_score, best_label = None, None
	for label, model in models.items():
		score = model.score(mfccs)
		if (best_score is None) or \
					(best_score < score):
			best_score, best_label=score,label
	pred_test_y.append(best_label)

print(test_y)
print(pred_test_y)
```

### 图像识别

#### OpenCV基础

opencv是一个开源的计算机视觉库. 提供了很多图像处理的常用工具.

案例: 

```python
"""
demo03_cv.py  opencv基础
"""
import numpy as np
import cv2 as cv

# 读取图片并显示
img = cv.imread('../ml_data/forest.jpg')
cv.imshow('Image', img)
# 显示图像中每个颜色通道的图像
print(img.shape)
# 0 保留蓝色通道 其他颜色值为0
blue = np.zeros_like(img)
blue[:,:,0] = img[:,:,0]
cv.imshow('blue', blue)

# 1 保留绿色通道 其他颜色值为0
green = np.zeros_like(img)
green[:,:,1] = img[:,:,1]
cv.imshow('green', green)

# 2 保留红色通道 其他颜色值为0
red = np.zeros_like(img)
red[:,:,2] = img[:,:,2]
cv.imshow('red', red)

# 图像裁剪
h, w = img.shape[:2]
l, t = int(w/4), int(h/4)
r, b = int(w*3/4), int(h*3/4)
cropped = img[t:b, l:r]
cv.imshow('cropped', cropped)

# 图像缩放  
scaled = cv.resize(img, (int(w/4), int(h/4)), 
	interpolation=cv.INTER_LINEAR)
cv.imshow('scaled', scaled)

scaled2 = cv.resize(scaled, (w, h),
	interpolation=cv.INTER_LINEAR)
cv.imshow('scaled2', scaled2)

# 图像文件的保存
cv.imwrite('../ml_data/blue.jpg', blue)


cv.waitKey()  # 阻塞方法, 按下键盘继续执行
```

#### 边缘检测

物体的边缘检测是物体识别的常用手段. 边缘检测常用亮度梯度方法, 通过识别亮度梯度变化最大的像素点从而检测出物体的边缘.

```python
# Canny边缘检测
# 50: 水平方向上的阈值   240: 垂直方向上的阈值
cv.Canny(img, 50, 240)
```

案例:

```python
"""
demo04_canny.py  边缘检测
"""
import cv2 as cv
img = cv.imread('../ml_data/chair.jpg', 
				cv.IMREAD_GRAYSCALE)
cv.imshow('img', img)
# canny边缘检测
canny = cv.Canny(img, 50, 240)
cv.imshow('canny', canny)

# cv.Sobel() 索贝尔边缘检测
# cv.CV_64F: 做索贝尔偏微分时使用的数据精度
# 1: 水平方向做偏微分   0: 垂直方向不做偏微分
# ksize: 索贝尔卷积过程中使用卷积核的大小 5*5
hsobel=cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
cv.imshow('hsobel', hsobel)

cv.waitKey()
```

#### 亮度提升

opencv提供了直方图均衡化的方式实现亮度提升, 更有利于边缘识别与物体识别模型的训练.

```python
# 彩色图转灰度图
gray = cv.cvtcolor(img, cv.COLOR_BGR2GRAY)
# 直方图均衡化
equalized_gray = cv.equalizeHist(gray)
```

案例:

```python
"""
demo05_eqhist.py  直方图均衡化 
"""
import cv2 as cv

img = cv.imread('../ml_data/sunrise.jpg')
cv.imshow('img', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
equalized_gray = cv.equalizeHist(gray)
cv.imshow('equalized_gray', equalized_gray)
# 对彩色图像提亮
# YUV: 亮度, 色度, 饱和度
yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
yuv[:,:,0] = cv.equalizeHist(yuv[:,:,0])
equalized_color = cv.cvtColor(yuv, cv.COLOR_YUV2BGR)
cv.imshow('equalized_color', equalized_color)

cv.waitKey()
```

#### 角点检测

对一个图像执行角点检测, 可以检测出平直楞线的交汇点. (求亮度梯度方向改变的像素点的位置)

```python
# Harris角点检测器
# gray: 灰度图像
# 边缘水平方向,垂直方向亮度梯度值改变超过阈值7/5时即为边缘.
# 边缘线方向改变超过阈值0.04弧度值即为一个角点.
corners = cv.cornerHarris(gray, 7, 5, 0.04)
```

案例:

```python
"""
demo06_corners.py  角点检测
"""
import cv2 as cv

img = cv.imread('../ml_data/box.png')
cv.imshow('img', img)
# 角点监测
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
corners = cv.cornerHarris(gray, 7, 5, 0.04)
print(img.shape, corners.shape)
# 在图像中绘制角点
mixture = img.copy()
mixture[corners>corners.max()*0.01] = [0,0,255]
cv.imshow('mixture', mixture)

cv.waitKey()
```

#### 特征点检测

STAR特征点检测 / SIFT特征点检测

特征点检测结合了边缘检测与角点检测从而识别出物体的特征点.

STAR特征点检测

```python
import cv2 as cv
# 创建star特征点检测器
star = cv.xfeatures2d.StarDetector_create()
keypoints = star.detect(gray)
# cv提供了方法吧keypoint绘制在图像中
cv.drawKeypoints(img, keypoints, 
                 mixture, flags=
cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
```

SIFT特征点检测

```python
sift = cv.xfeatures2d.SIFT_create()
keypoints = sift.detect(gray)
```

案例:

```python
"""
demo08_sift.py sift特征点检测
"""
import cv2 as cv
img = cv.imread('../ml_data/table.jpg')
cv.imshow('img', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
# 提取特征点
sift = cv.xfeatures2d.SIFT_create()
keypoints = sift.detect(gray)
mixture = img.copy()
cv.drawKeypoints(img, keypoints, 
                 mixture, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('mixture', mixture)
cv.waitKey()
```

#### 特征值矩阵

图像的特征值描述矩阵记录了图像的特征点以及每个特征点的梯度信息. 相似图像的特征值矩阵也相似. 如果有足够多的样本就可以基于隐马模型进行图像内容的识别.

```python
keypoints = sift.detect(gray)
# desc即为图像的特征值矩阵
_, desc = sift.compute(gray, keypoints)
```

#### 物体识别

1. 读取每个图片文件, 加载每个文件的特征值描述矩阵, 整理训练集, 与某个类别名绑定在一起.
2. 基于隐马模型, 对三个类别的特征值描述矩阵训练集进行训练, 得到3个隐马模型, 分别用于识别三个类别.
3. 对测试集分别进行测试, 取得分高的为最终预测类别.

```python
"""
demo09_wtsb.py   物体识别
"""
import os 
import numpy as np
import hmmlearn.hmm as hl
import cv2 as cv

def search_files(directory):
	directory = os.path.normpath(directory)

	# {'apple':[dir,dir,dir], 'banana':[dir..]}
	objects = {}
	#当前目录, 当前目录子目录, 文件列表
	for curdir,subdirs,files in \
					os.walk(directory):
		for file in files:
			if file.endswith('.jpg'):
				label = curdir.split(os.path.sep)[-1]
				if label not in objects:
					objects[label] = []
				path = os.path.join(curdir, file)
				objects[label].append(path)
	return objects


train_samples = \
	search_files('../ml_data/objects/training')

# 整理训练集, 把每一个类别中的图片的desc
# 摞在一起, 基于隐马模型开始训练.

train_x, train_y = [], []
for label, filenames in train_samples.items():
	descs = np.array([])
	for filename in filenames:
		# 获取当前图片的desc描述矩阵加入descs
		img = cv.imread(filename)
		gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
		# 对图片进行范围缩放
		h, w = gray.shape[:2]
		f = 200 / min(h, w)
		# fx: x轴伸缩比例  fy: y轴伸缩比例
		gray = cv.resize(gray, None, fx=f, fy=f)
		sift = cv.xfeatures2d.SIFT_create()
		keypoints = sift.detect(gray)
		_,desc = sift.compute(gray, keypoints)
		print(label, desc.shape)
		if len(descs) == 0:
			descs = desc
		else:
			descs = np.append(descs, desc, axis=0)
	train_x.append(descs)
	train_y.append(label)

# 基于隐马模型进行训练, 把所有类别的模型都存起来
# 一共3个类别循环3次
models = {}
for descs, label in zip(train_x, train_y):
	model = hl.GaussianHMM(n_components=4, 
		covariance_type='diag', n_iter=200)
	models[label] = model.fit(descs)

# 读取测试集中的文件, 使用每个模型对文件进行
# 评分, 取分值大的模型对应的label作为预测类别
test_samples = \
	search_files('../ml_data/objects/testing')

# 整理测试集, 提取每一个文件的mfcc
test_x, test_y = [], []
for label, filenames in test_samples.items():
	descs = np.array([])
	for filename in filenames:
		# 获取当前图片的desc描述矩阵加入descs
		img = cv.imread(filename)
		gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
		# 对图片进行范围缩放
		h, w = gray.shape[:2]
		f = 200 / min(h, w)
		# fx: x轴伸缩比例  fy: y轴伸缩比例
		gray = cv.resize(gray, None, fx=f, fy=f)
		sift = cv.xfeatures2d.SIFT_create()
		keypoints = sift.detect(gray)
		_,desc = sift.compute(gray, keypoints)
		print(label, desc.shape)
		if len(descs) == 0:
			descs = desc
		else:
			descs = np.append(descs, desc, axis=0)
	test_x.append(descs)
	test_y.append(label)

# 使用3个模型, 对每一个文件进行预测得分.
pred_test_y = []
# test_x一共3个样本, 遍历3次, 每次验证1个文件
for descs in test_x:
	best_score, best_label = None, None
	for label, model in models.items():
		score = model.score(descs)
		if (best_score is None) or \
					(best_score < score):
			best_score, best_label=score,label
	pred_test_y.append(best_label)

print(test_y)
print(pred_test_y)
```

### 人脸识别

人脸识别与图像识别的区别在于人脸识别需要识别出两个人的不同点. 眉间距离, 鼻子位置.眼睛位置等等..

#### opencv的视频捕捉

opencv提供了访问视频捕捉设备的API(摄像头), 从而获取图像帧.

```python
"""
demo10_vc.py  捕获视频
"""
import cv2 as cv
# 获取视频采集设备   下标为0的摄像头
videoCapture = cv.VideoCapture(0)
# 获取采集到的第一张图片(第一帧)

while True:
	frame = videoCapture.read()[1]
	cv.imshow('frame', frame)
	# 每33毫秒自动解除阻塞
	if cv.waitKey(33) == 27:
		break

# 释放视频设备
videoCapture.release()
cv.destroyAllWindows()  # 销毁所有窗口
```

#### 人脸定位

哈尔级联人脸定位

```python
fd = cv.CascadeClassifier('../xxx/face.xml')
# frame, 图像
# 1.3: 最小的人脸尺寸
# 5: 最多找5张脸
faces = fd.detectMultiScale(frame, 1.3, 5)
```

案例:

```python
"""
demo11_fd.py  人脸定位器
"""
import cv2 as cv

fd = cv.CascadeClassifier('../ml_data/haar/face.xml')
ed = cv.CascadeClassifier('../ml_data/haar/eye.xml')
nd = cv.CascadeClassifier('../ml_data/haar/nose.xml')

# 获取视频采集设备   下标为0的摄像头
videoCapture = cv.VideoCapture(0)
# 获取采集到的第一张图片(第一帧)
while True:
	frame = videoCapture.read()[1]
	# 通过哈尔定位器 进行局部定位 并在图像中标注
	faces = fd.detectMultiScale(frame, 1.3, 2)
	for l, t, w, h in faces:
		# 绘制椭圆
		a, b = int(w/2), int(h/2)
		cv.ellipse(frame, 
			(l+a, t+b), # 椭圆心坐标
			(a, b), # 椭圆半径
			0, 0, 360, (255,0,255), 
			2 # 椭圆的线宽
		)
		# 绘制鼻子和眼睛
		face = frame[t:t+h, l:l+w]
		eyes = ed.detectMultiScale(face, 1.3, 5)
		for l, t, w, h in eyes:	
			a, b = int(w/2), int(h/2)
			cv.ellipse(face, 
				(l+a, t+b), # 椭圆心坐标
				(a, b), # 椭圆半径
				0, 0, 360, (0,255,255), 
				2 # 椭圆的线宽
			)
		
		nodes = nd.detectMultiScale(face, 1.3, 5)
		for l, t, w, h in nodes:	
			a, b = int(w/2), int(h/2)
			cv.ellipse(face, 
				(l+a, t+b), # 椭圆心坐标
				(a, b), # 椭圆半径
				0, 0, 360, (255,255,0), 
				2 # 椭圆的线宽
			)
	cv.imshow('frame', frame)
	# 每33毫秒自动解除阻塞
	if cv.waitKey(33) == 27:
		break

# 释放视频设备
videoCapture.release()
cv.destroyAllWindows()  # 销毁所有窗口
```



####  人脸识别

简单人脸识别:  opencv的LBPH(局部二值模式直方图)

```python

```























