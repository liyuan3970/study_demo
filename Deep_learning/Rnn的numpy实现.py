import numpy as np

# 定义相关参数，init_state是输入到t1的t0时刻输出的状态
x = [0.8,0.1]
init_state = [0.3, 0.6]
W = np.asarray([[0.2, 0.4], [0.7, 0.3]])
U = np.asarray([0.8, 0.1])
b_h = np.asarray([0.2, 0.1])
V = np.asarray([[0.5], [0.5]])
b_o = 0.1

#执行两轮循环，模拟前向传播过程
for i in range(len(x)):

    #numpy的dot()函数用于矩阵相乘，函数原型为dot(a, b, out)
    before_activation = np.dot(init_state, W) + x[i] * U + b_h

    #numpy也提供了tanh()函数实现双曲正切函数的计算
    state = np.tanh(before_activation)

    #本时刻的状态作为下一时刻的初始状态
    init_state=state

    #计算本时刻的输出
    final_output = np.dot(state, V) + b_o

    # 打印t1和t2时刻的状态和输出信息
    print("t%s state: %s" %(i+1,state))
    print("t%s output: %s\n" %(i+1,final_output))

'''打印的信息如下；
t1 state: [0.86678393 0.44624361]
t1 output: [0.75651377]

t2 state: [0.64443809 0.5303174 ]
t2 output: [0.68737775]
'''