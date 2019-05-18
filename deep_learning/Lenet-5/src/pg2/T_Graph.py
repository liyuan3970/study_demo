import tensorflow as tf
from DataUtil import *
import numpy as np

import os 
import time 
from datetime import timedelta
"""
 构建训练模型:LeNet5
 对数据进行训练
 并对训练的结果进行性能评估
"""
# 输入层,输出层
input_x=tf.placeholder(dtype=tf.float32,shape=[None,784])
input_img=tf.reshape(input_x,shape=[-1,28,28,1])
output_y=tf.placeholder(dtype=tf.float32,shape=[None,10])
output_cls=tf.argmax(output_y,dimension=1)

# 卷积层1
"""
 32个5*5大小的卷积核
 卷积运算:same
 激活函数:relu
 输出:32个28*28的矩阵
"""
conv1=tf.layers.conv2d(inputs=input_img,  # 输入数据
                       filters=32,        # 卷积核的数量
                       kernel_size=[5,5], # 卷积核的大小
                       padding='same',    # 卷积运算的方式
                       activation=tf.nn.relu) #激活函数
# 池化层1
"""
  池化核:2*2最大值池化
  输出:32个14*14
"""
pool1=tf.layers.max_pooling2d(inputs=conv1,
                              pool_size=[2,2],
                              strides=2)


# 卷积层2
"""
 64个5*5大小的卷积核
 卷积运算:same
 激活函数:relu
 输出:64个14*14的矩阵
"""
conv2=tf.layers.conv2d(inputs=pool1,  # 输入数据
                       filters=64,        # 卷积核的数量
                       kernel_size=[5,5], # 卷积核的大小
                       padding='same',    # 卷积运算的方式
                       activation=tf.nn.relu) #激活函数
# 池化层2
"""
  池化核:2*2最大值池化
  输出:64个7*7
"""
pool2=tf.layers.max_pooling2d(inputs=conv2,
                              pool_size=[2,2],
                              strides=2)

#扁平化pool2 7*7*64结果
flat=tf.reshape(pool2,shape=[-1,7*7*64])

#定义全连接的神经元
#全连接层1
full1=tf.layers.dense(inputs=flat,units=1024,
    activation=tf.nn.relu
    )
#防止过拟合，1.数据增强 2.正则化 3.降采样rate=0.4 40%的不用链接
dp=tf.layers.dropout(inputs=full1,rate=0.4)






#结果层全连接层2
'''
最后输出的0～9数字的概率，输出多分类的结果
多分类使用softmax激活函数
对于二分类来说，则使用sigmoid激活函数
'''
full2=tf.layers.dense(inputs=dp,units=10,)
#表示0到9的概率有多大
#归一化
logit=tf.nn.softmax(full2)
#预测类别
pred=tf.argmax(logit,dimension=1)

#利用交叉熵定义损失函数
cross=tf.nn.softmax_cross_entropy_with_logits(labels=output_y,logits=logit)
cost = tf.reduce_mean(cross)#损失均值



#优化 随机梯度下降 (反向传播优化)
train=tf.train.AdamOptimizer(learning_rate=1e-4).minimize(cost)

#性能评估：预测的准确率
#布尔类型
corr_pred=tf.equal(output_cls,pred)
#转换类型
acc = tf.reduce_mean(tf.cast(corr_pred,tf.float32))
  
# 测试
#with tf.Session() as ress:
#    ress.run(tf.global_variables_initializer())
#    c1,p1=ress.run([conv2,pool2],feed_dict={input_x:mnist.train.images[:2]})
#    print(c1)
#    print(c1.shape)
#    print(p1.shape)
#测试logit
#with tf.Session() as ress:
#    ress.run(tf.global_variables_initializer())
#    result=ress.run([logit],feed_dict={input_x:mnist.train.images[:2]})
#    print(result)
#测试logit
#with tf.Session() as ress:
#    ress.run(tf.global_variables_initializer())
#    result,pd=ress.run([logit,pred],feed_dict={input_x:mnist.train.images[:2]})
 #   print(result)
  #  print(pd)
#测试cost cross
##with tf.Session() as ress:
#    ress.run(tf.global_variables_initializer())
 #   result,pd,loss=ress.run([logit,pred,cost],feed_dict={input_x:mnist.train.images[:2],
#    	output_y:mnist.train.labels[:2]})
#    print(result)
#    print(pd)
#    print(loss)

#循环的开启会话()
#保存训练模型
save_dir='checkpoint/'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
save_path = os.path.join(save_dir,'besetmodel')
#模型保存对象
saver=tf.train.Saver()

#训练的批次大小--64--（每次训练要拿多少数据来训练）
batch_size = 64

def opt(num_iter):
    #定义训练方法
    '''
    训练过程
    num_iter : 更新迭代的次数
    return：无返回
    '''
    session=tf.Session()
    session.run(tf.global_variables_initializer())
	#定义最优准确率
    best_acc=0

    for i in range(num_iter):
        #产生参与训练的样本
        x_batch,y_batch=mnist.train.next_batch(batch_size)
        #执行优化与性能评估　ac 表示每次迭代更新的预测准确率，　_,表示不关心输出是啥
        _,ac=session.run([train,acc],feed_dict={input_x:x_batch,output_y:y_batch})
        #
        if i%100==0:
            print('迭代次数:{0},准确率：{1}'.format((i+1),ac))
        if ac>best_acc :
            best_acc=ac
            saver.save(sess=session,save_path=save_path)

    #用已经训练好的模型测试输出，测试集第一个样本的标签
    pred_test = session.run(pred,feed_dict={input_x:mnist.test.images[:1]})
    print(pred_test)
    print('正确标签:{0}'.format(mnist.test.cls[:1]))

opt(num_iter=1000)






"""
 构建训练模型:定义超参数
 神经网络的层数
 每一层神经元的数量
 神经元之间的连接方式
 每层使用的激活函数
 
 
 训练参数:
 权重参数和阈值
"""