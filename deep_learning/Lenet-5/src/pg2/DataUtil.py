"""
    导入库
"""
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
import numpy as np


"""
    数据加载
    one-hot:热编码,
"""
def loadData(filename):
    mnist=input_data.read_data_sets(filename,one_hot=True)
    mnist.train.cls=np.argmax(mnist.train.labels,axis=1)
    mnist.validation.cls = np.argmax(mnist.validation.labels, axis=1)
    mnist.test.cls = np.argmax(mnist.test.labels, axis=1)
    return mnist

# 代码测试
mnist=loadData('../../dataset/mnist')
print(mnist.train.images[0])

"""
    数据可视化
"""
def plotData(imgs,cls,pred=None):
    '''
    :param imgs: 图片
    :param cls: 图片的真实标签
    :param pred: 图片的预测类别
    :return: 无
    '''
    # 断言
    assert  len(imgs)==len(cls)==9
    # 将绘图窗口拆分为3*3的窗口
    f,subs=plt.subplots(3,3)
    lbl='' #x轴标题
    for i,sub in enumerate(subs.flat):
        sub.imshow(imgs[i].reshape(28,28),cmap='binary')
        if pred is None:
            lbl='true:{0}'.format(cls[i])
        else:
            lbl='true:{0};pred:{1}'.format(cls[i],pred[i])
        sub.set_xlabel(lbl)#标题
        sub.set_xticks([]) #清除刻度
        sub.set_yticks([])
    plt.show()

#plotData(mnist.train.images[:9],mnist.train.cls[:9])
