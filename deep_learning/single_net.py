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