# **深度学习**<br/>
## 神经网络的基本步骤
1. 构造方法
2. 打印权重参数和偏置项
3. 预测输出
4. 更新权重参数和偏置项
5. 迭代一次
6. 训练
## 单层神经网络
用单层神经网络实现and运算（等于是一个简单的二分类）

x1|x2|y
-----|-----|-----
0|0|0
0|1|0
1|0|0
1|1|1

## 源码
```python
#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
class Perceptron(object):

    '''
    单层神经网络 demo1   

    '''
    #1.构造方法
    def __init__(self,activator,input_vec):
        '''
        activator:激活函数
        input_vec:
        thetas:权重参数
        '''
        self.activator = activator
        self.input_vec = input_vec
        self.thetas = np.random.normal(0,0.01,size = (input_vec.shape[1],1))
        self.bias = 1

    #2.打印权重参数和偏置项
    def __str__(self):
        print("权重参数")
        print(self.thetas)
        print("偏置项")
        print(self.bias)
    #3.预测输出
    def predict(self,vec):
        '''
        计算一次迭代的预测值
        '''
        return(self.activator(np.sum(np.dot(vec,self.thetas)+self.bias)))
    #4.更新权重参数和偏置项
    def update_thetas(self,vec,output,lbl,rate):
        '''
        loss误差：预测值减去期望值
        lbl：期望值
        rate：学习速度，每一次迭代的步数，每次迭代的步长
        注意：这一步的作用时将正向传播的误差，反向传递给thetas（权重）和bias（偏置项） 
        '''
        loss = lbl-output
        self.thetas = list(map(lambda x:x[0]+x[1]*loss*rate,
            list(zip(self.thetas,vec))))
        self.bias+=loss*rate
    #5.迭代一次
    def one_iterator(self,lbls,rate):
        '''
        这一步的作用是：通过不断的迭代，反向传播，修正权重值和偏置项，以达到一个最好的模型参数
        '''
        samples = zip(self.input_vec,lbls)
        for vec,lbl in samples:
            output = self.predict(vec)
            self.update_thetas(vec,output,lbl,rate)	
    #6.训练
    def train(self,lbls,iteration,rate):
        '''
        lbls 预测期望值(正确的预测值) 
        iteration 迭代次数
        rate 学习速率
        '''
        for i in range(iteration):
            self.one_iterator(lbls,rate)

#1训练样本
'''
datas 是特征样本，这里有4个样本，2个特征，其中0表示预测假，1表示预测真
lbls  是给定的预测结果，与datas对应，比如当datas=[0.0]时，两个假==假事件，那么对应y的预测期望值也是0，同理[1,0]==真假 ，逻辑and运算为假
即y的预测期望为0，[1,1]==真真，y=1
'''
def createData():
    datas=[[0,0],[1,0],[0,1],[1,1]]
    lbls = [0,0,0,1]
    return datas,lbls
#2数据可视化
def viewData(datas,lbls):
    for lbl,dt in zip(lbls,datas):
        plt.plot(dt[0],dt[1],'o' if lbl else '^',mec = 'r' if lbl else 'b')
    plt.show()
#3激活函数
'''
神经元通过一次计算后的值并不是1或者0，我们需要一个函数（激活函数）对所计算的实际y值进行加工，使其变成1或0
'''
def f(x):
    return 1 if x>0 else 0



#运算过程如下：懒得打字了，自己看吧！哈哈哈相信你们看懂！！
ds,ls = createData()
x = np.array(ds)
p=Perceptron(f,x)
#这里的1000的意思时迭代了1000次！！还是打个字吧
p.train(ls,1000,0.1)
p.__str__()
x1=[1,1]
y1=p.predict(x1)
print(y1)
    
```
以上使用底层numpy实现的一个单层神经网络的二分类

# 用双层网络实现xor的逻辑
## BP算法
+ BP神经网络是1986年由Rumelhart和McClelland为首的科学家提出的概念
+ BP——back propagation，也就是逆向传播的意思，通俗的说就是：用模型得到的预测值与真实值之间的误差，来影响改变之前各层间的权重
  
![BP算法](https://img-blog.csdn.net/20180126173405671?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvenpaX0NNaW5n/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

## 先介绍几个符号代表的意思：（都是向量式）
+ X——输入值（数据项）；Y——真实值（标签项）
+ V——输入层连接隐藏层的权重；W——隐藏层连接输出层的权重
+ L1——隐藏层的值（输入层的值X经过权重V作用后的输出值）
+ L2——预测值（隐藏层的值L1经过权重W作用后的输出值，也就是模型预测值）

## **BP算法的工作流程：**
1. 输入值X经过权重V的作用，再通过激活函数处理，得到隐藏层的输入值L1
2. 同时L1也是隐藏层的输出值，L1经过权重W的作用，再经过激活函数处理，得到预测值L2
3. 用梯度下降法计算输出层的误差改变量：真实值Y与预测值L2之间的误差与L2的负梯度相乘，得到输出层的误差改变量L2_delta
4. 用梯度下降法计算隐藏层的误差改变量：用输出层的误差改变量L2_delta乘权重W再与L1的负梯度相乘，得到隐藏层的误差改变量L1_delta
5. 各层误差改变量与学习率相乘，再与各层原有权重相加，得到更新后权重V_、W_
6. 用更新后的权重V_、W_迭代计算，重复以上步骤，直到满足一定条件时，输出最后预测值
   
## **BP神经网络解决异或**
```python
#-*- coding: utf-8 -*-


import numpy as np

lr = 0.11        #学习速率

#输入数据分别:偏置值,x1,x2
X = np.array([[1,0,0],
              [1,0,1],
              [1,1,0],
              [1,1,1]])

#标签
Y = np.array([[0,1,1,0]])

# 权重初始化，取值范围-1到1
V = np.random.random((3,4))*2-1
W = np.random.random((4,1))*2-1
#print('输入层连接隐藏层的权值V：',V)
#print('隐藏层连接输出层的权值W：',W)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def dsigmoid(x):
    return x*(1-x)

#更新权重函数
def get_update():
    global X,Y,W,V,lr
    # L1：输入层传递给隐藏层的值；输入层3个节点，隐藏层4个节点
    # L2：隐藏层传递到输出层的值；输出层1个节点
    L1 = sigmoid(np.dot(X,V))
    L2 = sigmoid(np.dot(L1,W))

    # L2_delta：输出层的误差改变量
    # L1_delta：隐藏层的误差改变量
    L2_delta = (Y.T - L2)*dsigmoid(L2)
    L1_delta = L2_delta.dot(W.T)*dsigmoid(L1)

    # W_C：输出层对隐藏层的权重改变量
    # V_C：隐藏层对输入层的权重改变量
    W_C = lr * L1.T.dot(L2_delta)
    V_C = lr * X.T.dot(L1_delta)

    # 更新后的权重
    W = W + W_C
    V = V + V_C

def main():
    for i in range(100000):
        get_update()
        if i%500 == 0:
            L1 = sigmoid(np.dot(X, V))
            L2 = sigmoid(np.dot(L1, W))
            print('当前误差',np.mean(np.abs(Y.T - L2)))
    L1 = sigmoid(np.dot(X, V))
    L2 = sigmoid(np.dot(L1, W))
    print('最后逼近值：',L2)

if __name__ == "__main__":
    main()

```




