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
