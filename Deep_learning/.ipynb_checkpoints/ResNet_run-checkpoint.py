import tensorflow as tf
import math
import time
import ResNet_struct
from tensorflow.contrib import slim
from datetime import datetime

batch_size = 32
num_batches = 100
num_steps_burn_in = 10
total_duration = 0.0
total_duration_squared = 0.0
inputs = tf.random_uniform((batch_size, 224, 224, 3))

def arg_scope(is_training=True,weight_decay=0.0001,batch_norm_decay=0.997,
                           batch_norm_epsilon=1e-5,batch_norm_scale=True):

    batch_norm_params = {"is_training": is_training,
                         "decay": batch_norm_decay,
                         "epsilon": batch_norm_epsilon,
                         "scale": batch_norm_scale,
                         "updates_collections": tf.GraphKeys.UPDATE_OPS}

    with slim.arg_scope([slim.conv2d],
                        #weights_initializer用于指定权重的初始化程序
                        weights_initializer=slim.variance_scaling_initializer(),
                        #weights_regularizer为权重可选的正则化程序
                        weights_regularizer=slim.l2_regularizer(weight_decay),
                        #activation_fn用于激活函数的指定，默认的为ReLU函数
                        #normalizer_params用于指定正则化函数的参数
                        activation_fn=tf.nn.relu, normalizer_fn=slim.batch_norm,
                        normalizer_params=batch_norm_params):

        #定义slim.batch_norm()函数的参数空间
        with slim.arg_scope([slim.batch_norm], **batch_norm_params):
            # slim.max_pool2d()函数的参数空间
            with slim.arg_scope([slim.max_pool2d], padding="SAME") as arg_scope:
                return arg_scope

# 定义模型的前向传播过程，这被限制在一个参数空间中
with slim.arg_scope(arg_scope(is_training=False)):
    net = ResNet_struct.resnet_v2_152(inputs, 1000)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)

    #运行前向传播测试过程
    for i in range(num_batches + num_steps_burn_in):
        start_time = time.time()
        _ = sess.run(net)
        duration = time.time() - start_time
        if i >= num_steps_burn_in:
            if i % 10 == 0:
                print('%s: step %d, duration = %.3f' %
                      (datetime.now(), i - num_steps_burn_in, duration))
            total_duration += duration
            total_duration_squared += duration * duration
    average_time = total_duration / num_batches

    #打印前向传播的运算时间信息
    print('%s: Forward across %d steps, %.3f +/- %.3f sec / batch' %
          (datetime.now(), num_batches, average_time,
           math.sqrt(total_duration_squared / num_batches-average_time*average_time)))


'''打印的内容
2018-04-28 15:44:25.253434: step 0, duration = 1.039
2018-04-28 15:44:35.616892: step 10, duration = 1.037
2018-04-28 15:44:45.981536: step 20, duration = 1.035
2018-04-28 15:44:56.349566: step 30, duration = 1.036
2018-04-28 15:45:06.728368: step 40, duration = 1.035
2018-04-28 15:45:17.089299: step 50, duration = 1.035
2018-04-28 15:45:27.456285: step 60, duration = 1.037
2018-04-28 15:45:37.822637: step 70, duration = 1.035
2018-04-28 15:45:48.192688: step 80, duration = 1.035
2018-04-28 15:45:58.555936: step 90, duration = 1.035
2018-04-28 15:46:07.886232: Forward across 100 steps, 1.037 +/- 0.002 sec / batch
'''