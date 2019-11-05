import numpy as np
import random
 
# 初始化矩阵
Q = np.zeros((6, 6))
Q = np.matrix(Q)
 
# 回报矩阵R
R = np.matrix([[-1,-1,-1,-1,0,-1],[-1,-1,-1,0,-1,100],[-1,-1,-1,0,-1,-1],[-1,0,0,-1,0,-1],[0,-1,-1,0,-1,100],[-1,0,-1,-1,0,100]])
 
# 设立学习参数
γ = 0.8
 
# 训练
for i in range(2000):
    # 对每一个训练,随机选择一种状态
    state = random.randint(0, 5)
    while True:
        # 选择当前状态下的所有可能动作
        r_pos_action = []
        for action in range(6):
            if R[state, action] >= 0:
                r_pos_action.append(action)
        next_state = r_pos_action[random.randint(0, len(r_pos_action) - 1)]
        Q[state, next_state] = R[state, next_state] + γ *(Q[next_state]).max()  #更新
        state = next_state
        # 状态4位最优库存状态
        if state==5:
            break
print(Q)
