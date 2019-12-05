import numpy as np
import matplotlib.pyplot as plt
# 数据预处理
# 加载数据
# 特征 5,2
x=np.array([[1,0],[0,0],[0,1],[1,1],[1,1]])
# 标签 5,2
y=np.array([[0],[0],[0],[1],[1]])

# 数据可视化
for _x,_y in zip(x,y):
    plt.plot(_x[0],_x[1],'o' if _y[0] else '^',
                         mec='r' if _y[0] else 'b' )
#plt.show()

# 权重参数
# x [5,2]:5-样本数量,2-特征向量的数量
print(x)
# w:维度1-样本的特征向量的数量,维度2-输出结果的数量
w=np.random.normal(0,0.01,size=[2,1])
print(w)

b=np.random.normal(0,0.01,size=[1])

# 预测输出
output=np.dot(x,w)+b

print(output)