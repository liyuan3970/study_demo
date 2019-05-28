# 机器学习DAY06

**回归算法**

线性回归

岭回归

多项式回归

决策树回归

集合算法-正向激励

集合算法-自助聚合

集合算法-随机森林

支持向量机 svm.SVR()

**分类算法**

简单分类

逻辑分类

朴素贝叶斯分类

决策树分类

支持向量机分类

**聚类算法**

K均值聚类

均值漂移聚类

凝聚层次聚类

DBSCAN聚类



#### 推荐引擎

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

代码实现:   ratings.json

```python
"""
demo01_recom.py  推荐引擎
"""
import json
import numpy as np
'''
1. 读取json文件, 遍历每一个用户, 计算当前
   用户与其他用户的相似度(欧式距离得分)
2. 把每个相似度得分,存入scmat矩阵.供以后使用
'''
with open('../ml_data/ratings.json', 'r')as f:
	ratings = json.loads(f.read())

users, scmat = list(ratings.keys()), []
for user1 in users:
	scrow = [] # 存储user1与其他人的相似度得分
	for user2 in users:
		movies = set()
		# user1看过的user2也看过
		for movie in ratings[user1]:
			if movie in ratings[user2]:
				movies.add(movie)
		# 两人没有共同语言
		if len(movies) == 0:
			score = 0
		else:  # 两人有都看过的电影
			x, y = [], []
			for movie in movies:
				x.append(ratings[user1][movie])
				y.append(ratings[user2][movie])
			x = np.array(x)
			y = np.array(y)
			score = 1/(1+np.sqrt(((x-y)**2).sum()))
		scrow.append(score)
	scmat.append(scrow)

users = np.array(users)
scmat = np.array(scmat)
# 输出每个用户的相关系数得分矩阵
for scrow in scmat:
	print('  '.join(
	'{:.2f}'.format(score) for score in scrow))
```

**皮尔逊相关系数**

```
x: [5, 3, 3]
y: [3, 1, 1]
m = np.corrcoef(x, y)
m[0, 1]
```

皮尔逊相关系数 = 协方差 / 标准差之积

相关系数处于[-1, 1]之间.  越靠近1越正相关, 越靠近-1越负相关.

**按照相关系数从高到低排列每个用户的相似度**

```python
# 按照相关系数从高到低排列每个用户的相似度
for i, user in enumerate(users):
	sorted_indices = scmat[i].argsort()[::-1]
	# 忽视当前user
	sorted_indices = \
		sorted_indices[sorted_indices!=i]
	# 获取相似用户数组
	similar_users = users[sorted_indices]
	# 获取每个相似用户的相似度得分
	similar_scores = scmat[i, sorted_indices]
	print(user, similar_users, similar_scores,
		sep='\n')

```

**生成推荐清单**

1. 找到所有皮尔逊相关系数正相关的用户.
2. 遍历当前用户的每个相似用户, 拿到相似用户看过,且当前用户没有看过的电影. 
3. 计算每个电影的推荐度.  获取所有用户对当前推荐电影的打分情况, 求均值, 以此来作为该电影的推荐度.
4. 排序, 输出.

```python
	# 生成推荐清单
	# 找到所有正相关用户即相关性分数
	positive_mask=similar_scores > 0
	similar_users=similar_users[positive_mask]
	similar_scores=similar_scores[positive_mask]
	# 存储对当前用户的推荐的电影
	# recomm_movies = {'电影名':[0.5, 0.4, 0.3]}
	recomm_movies = {}
	for i, similar_user in \
				enumerate(similar_users):
		# 拿到相似用户看过, 但user没看过的电影
		for movie, score in \
				ratings[similar_user].items():
			if movie not in ratings[user].keys():
				if movie not in recomm_movies:
					recomm_movies[movie]=[score]
				else:
					recomm_movies[movie].append(score)

	print(user)
	#print(recomm_movies)
	movie_list = sorted(recomm_movies.items(), 
		key=lambda x:np.average(x[1]), 
		reverse=True)
	print(movie_list)
```

### 自然语言处理(NLP)

Siri工作流程: 1. 听  2. 懂  3.思考  4. 组织语言  5.回答

1. 语音识别
2. 自然语言处理 - 语义分析
3. 业务逻辑分析 - 结合场景 上下文
4. 自然语言处理 - 分析结果生成自然语言文本
5. 语音合成

#### 自然语言处理

自然语言处理的常用处理过程:

先针对训练文本进行分词处理(词干提取, 原型提取), 统计词频, 通过词频-逆文档频率算法获得该词对整个样本语义的贡献, 根据每个词对语义的贡献力度, 构建有监督分类学习模型. 把测试样本交给模型处理, 得到测试样本的语义类别.

自然语言处理工具包 - nltk

#### 文本分词

```python
import nltk.tokenize as tk
# 把一段文本拆分句子
sent_list = tk.sent_tokenize(text)
# 把一句话拆分单词
word_list = tk.word_tokenize(sent)
# 通过文字标点分词器 拆分单词
punctTokenizer = tk.WordPunctTokenizer()
word_list = punctTokenizer.tokenize(text)
```

案例:

```python
"""
demo02_tokenize.py  分词器
"""
import nltk.tokenize as tk
doc = "Are you curious about tokenization? \
	Let's see how it works! \
	We neek to analyze a couple of sentences \
	with punctuations to see it in action."
# print(doc)

sent_list = tk.sent_tokenize(doc)
for i, sent in enumerate(sent_list):
	print('%2d' % (i+1), sent) 

word_list = tk.word_tokenize(doc)
for i, word in enumerate(word_list):
	print('%2d' % (i+1), word) 

tokenizer = tk.WordPunctTokenizer()
word_list = tokenizer.tokenize(doc)
for i, word in enumerate(word_list):
	print('%2d' % (i+1), word) 
```

#### 词干提取

```python
import nltk.stem.porter as pt
import nltk.stem.lancaster as lc
import nltk.stem.snowball as sb

# 波特词干提取器  (偏宽松)
stemmer = pt.PorterStemmer()
# 朗卡斯特词干提取器   (偏严格)
stemmer = lc.LancasterStemmer()
# 思诺博词干提取器   (偏中庸)
stemmer = sb.SnowballStemmer('english')
r = stemmer.stem('playing') # 词干提取
```

#### 词性还原

与词干提取作用类似, 次干提取出的词干信息不利于人工二次处理(人读不懂), 词性还原可以把名词复数等形式恢复为单数形式. 更有利于人工二次处理.

```python
import nltk.stem as ns
# 词性还原器
lemmatizer = ns.WordNetLemmatizer()
n_lemm=lemmatizer.lemmatize(word, pos='n')
v_lemm=lemmatizer.lemmatize(word, pos='v')
```

案例:

```python
"""
demo04_lemmetize.py  词性还原
"""
import nltk.stem as ns

words = ['table', 'probably', 'wolves', 
	'playing', 'is', 'the', 'beaches', 
	'grouded', 'dreamt', 'envision']

lemmatizer = ns.WordNetLemmatizer()
for word in words:
	n_lemm = lemmatizer.lemmatize(word,pos='n')
	v_lemm = lemmatizer.lemmatize(word,pos='v')
	print('%8s %8s %8s' % \
		  (word, n_lemm, v_lemm))
```

#### 词袋模型

文本分词处理后, 若需要分析文本语义, 需要把分词得到的结果构建样本模型, 词袋模型就是由每一个句子为一个样本, 单词在句子中出现的次数为特征值构建的数学模型. 

The brown dog is running. The black dog is in the black room. Running in the room is forbidden.

1. The brown dog is running. 
2. The black dog is in the black room.
3. Running in the room is forbidden.

| the  | brown | dog  | is   | running | black | in   | room | forbidden |
| ---- | ----- | ---- | ---- | ------- | ----- | ---- | ---- | --------- |
| 1    | 1     | 1    | 1    | 1       | 0     | 0    | 0    | 0         |
| 2    | 0     | 1    | 1    | 0       | 2     | 1    | 1    | 0         |
| 1    | 0     | 0    | 1    | 1       | 0     | 1    | 1    | 1         |

获取一篇文档的词袋模型:

```python
import sklearn.feature_extraction.text as ft
# 构建词袋模型对象
model = ft.CountVectorizer()
bow = model.fit_transform(sentences)
print(bow)
# 获取词袋模型的特征名
words = model.get_feature_names()
```



#### 词频(TF)

单词在句子中出现的次数 除以 句子的总词数 称为词频. 即一个单词在句子中出现的频率.  词频相对于单词出现的次数可以更加客观的评估单词对一句话的语义的贡献度. **词频越高,代表当前单词对语义贡献度越大.** 

#### 文档频率(DF)

含有某个单词的文档样本数 / 总文档样本数.

#### 逆文档频率(IDF)

总文档样本数 / 含有某个单词的文档样本数

**单词的逆文档频率越高, 代表当前单词对语义的贡献度越大.**

#### 词频-逆文档频率(TF-IDF)

词频矩阵中的每一个元素乘以相应单词的逆文档频率, 其值越大, 说明该词对样本语义的贡献度越大. 可以根据每个单词的贡献力度, 构建学习模型.

获取TFIDF矩阵相关API:

```python
model = ft.CountVectorizer()
bow = model.fit_transform(sentences)
# 获取IFIDF矩阵
tf = ft.TfidfTransformer()
tfidf = tf.fit_transform(bow)
# 基于tfidf 做模型训练
....
```

案例:

```python
"""
demo06_tfidf.py  tfidf转换
"""
import sklearn.feature_extraction.text as ft
import nltk.tokenize as tk
import numpy as np
doc = 'The brown dog is running. \
	The black dog is in the black room. \
	Running in the room is forbidden.'
# 拆分句子
sents = tk.sent_tokenize(doc)
print(sents)
# 构建词袋模型
model = ft.CountVectorizer()
bow = model.fit_transform(sents)
print(model.get_feature_names())

# 通过词袋矩阵  得到tfidf矩阵
tf = ft.TfidfTransformer()
tfidf = tf.fit_transform(bow)
print(np.round(tfidf.toarray(), 2))
```

#### 文本分类(主题识别)

读取20news文件夹, 每个文件夹的文件夹名作为类别标签, 文件夹中的没有文件作为样本, 构建tfidf矩阵, 交给朴素贝叶斯模型训练.   

自定义测试样本, 测试每句话的主题属于哪一类别.

```python
"""
demo07_news.py  主题识别
读取20news文件夹, 每个文件夹的文件夹名
作为类别标签, 文件夹中的没有文件作为样本, 
构建tfidf矩阵, 交给朴素贝叶斯模型训练.   

自定义测试样本, 测试每句话的主题属于哪一类别.
"""
import sklearn.datasets as sd
import sklearn.feature_extraction.text as ft
import sklearn.naive_bayes as nb
import numpy as np

train = sd.load_files('../ml_data/20news', 
	encoding='latin1', shuffle=True, 
	random_state=7)

# train.data: 返回每个文件的字符串内容
# train.target: 返回每个文件的父目录名(类别名)
print(np.array(train.data).shape)
print(np.array(train.target).shape)

# 整理输入集 输出集
train_data = train.data
train_y = train.target
categories = train.target_names # 类别名
cv = ft.CountVectorizer()
bow = cv.fit_transform(train_data)
tf = ft.TfidfTransformer()
train_x = tf.fit_transform(bow)
# 选择使用朴素贝叶斯 进行模型训练
model = nb.MultinomialNB()
model.fit(train_x, train_y)

# 测试集  测试模型是否可用
test_data = [
	'The curveballs of right handed pitchers \
	tend to curve to the left.', 
	'Caesar cipher is an ancient form of \
	encryption.',
	'This two-wheeler is really good on slippery \
	roads.']

bow = cv.transform(test_data)
tfidf = tf.transform(bow)
pred_y = model.predict(tfidf)

for sent, index in zip(test_data, pred_y):
	print(sent, '->', categories[index])
```

#### nltk内置分类器

nltk提供了朴素贝叶斯分类器方便的处理NLP相关的分类问题. 并且可以自动处理词袋, 完成TFIDF矩阵的整理, 完成模型训练, 最终实现类别预测.  使用方法:

```python
import nltk.classify as cf
import nltk.classify.util as su
'''
train_data与test_data的格式
不再是一行一样本, 一列一特征   格式如下:
[
({'age':10, 'score1':95, 'score2':80},'g'),
({'age':10, 'score1':35, 'score2':40},'b'),
({'age':10, 'score1':95, 'score2':80},'g')
]
'''
model =
  cf.NaiveBayesClassifier.train(train_data)
ac = cu.accuracy(model, test_data)
```

#### 情感分析

分析语料库中movie_reviews文档, 通过正面及负面评价进行自然语言训练, 实现情感分析.

```python
"""
demo08_movie_reviews.py 电影推荐
"""
import nltk.corpus as nc
import nltk.classify as cf
import nltk.classify.util as cu
import numpy as np

# 存储正面数据
pdata = []
# 读取语料库中movie_reviews文件夹中的pos文件夹
# 把每个文件的文件名返回
fileids = nc.movie_reviews.fileids('pos')
# 遍历每个文件, 把文件信息存入pdata
for fileid in fileids:
	sample = {}
	# 对全文进行分词  得到words列表
	words = nc.movie_reviews.words(fileid)
	for word in words:
		sample[word] = True
	pdata.append((sample, 'POSITIVE'))

# 存储负面数据
ndata = []
# 读取语料库中movie_reviews文件夹中的neg文件夹
# 把每个文件的文件名返回
fileids = nc.movie_reviews.fileids('neg')
# 遍历每个文件, 把文件信息存入pdata
for fileid in fileids:
	sample = {}
	# 对全文进行分词  得到words列表
	words = nc.movie_reviews.words(fileid)
	for word in words:
		sample[word] = True
	ndata.append((sample, 'NEGATIVE'))

# 拆分测试集与训练集 (80% 训练集)
pnumb, nnumb = \
	int(len(pdata)*0.8), int(len(ndata)*0.8)
train_data = pdata[:pnumb] + ndata[:nnumb]
test_data = pdata[pnumb:] + ndata[nnumb:]
print(np.array(train_data).shape)
print(np.array(test_data).shape)

# 基于朴素贝叶斯模型, 训练测试数据
model=cf.NaiveBayesClassifier.train(train_data)
ac = cu.accuracy(model, test_data)
print(ac)

# 模拟业务场景
reviews = [
 'It is an amazing movie. ',
 'This is a dull movie, I would never \
  recommend it to anyone. ', 
 'The cinematography is pretty great \
  in this movie. ', 
 'The direction was terrible and the story \
  was all over the place. ']

for review in reviews: 
	sample = {}
	words = review.split() # 野蛮分词
	for word in words:
		sample[word] = True
	# classify类似predict方法, 通过样本预测类别
	pred_y = model.classify(sample)
	print(review, '->', pred_y)
```

### 语音识别

语音识别可以实现通过一段音频信息(wav波) 识别出音频的内容. 

通过傅里叶变换, 可以将时间域的声音分解为一系列不同频率的正弦函数的叠加. 通过频率谱线的特殊分布, 建立音频内容与文本之间的对应关系, 以此作为模型训练的基础.

1. 准备多个声音样本作为训练数据. 并且为每个音频都标明其类别.
2. 读取每一个音频文件, 获取音频文件的mfcc矩阵.
3. 以mfcc作为训练样本, 进行训练.
4. 对测试样本进行测试.













