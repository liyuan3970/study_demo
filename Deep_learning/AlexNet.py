import tensorflow as tf
import math
import time
from datetime import datetime

batch_size = 32
num_batches = 100


# 在函数inference_op()内定义前向传播的过程
def inference_op(images):
    parameters = []

    # 在命名空间conv1下实现第一个卷积层
    with tf.name_scope("conv1"):
        kernel = tf.Variable(tf.truncated_normal([11, 11, 3, 96], dtype=tf.float32,
                                                 stddev=1e-1), name="weights")
        conv = tf.nn.conv2d(images, kernel, [1, 4, 4, 1], padding="SAME")
        biases = tf.Variable(tf.constant(0.0, shape=[96], dtype=tf.float32),
                             trainable=True, name="biases")
        conv1 = tf.nn.relu(tf.nn.bias_add(conv, biases))

        # 打印第一个卷积层的网络结构
        print(conv1.op.name, ' ', conv1.get_shape().as_list())

        parameters += [kernel, biases]

    # 添加一个LRN层和最大池化层
    lrn1 = tf.nn.lrn(conv1, 4, bias=1.0, alpha=0.001 / 9.0, beta=0.75, name="lrn1")
    pool1 = tf.nn.max_pool(lrn1, ksize=[1, 3, 3, 1], strides=[1, 2, 2, 1],
                           padding="VALID", name="pool1")

    # 打印池化层网络结构
    print(pool1.op.name, ' ', pool1.get_shape().as_list())

    # 在命名空间conv2下实现第二个卷积层
    with tf.name_scope("conv2"):
        kernel = tf.Variable(tf.truncated_normal([5, 5, 96, 256], dtype=tf.float32,
                                                 stddev=1e-1), name="weights")
        conv = tf.nn.conv2d(pool1, kernel, [1, 1, 1, 1], padding="SAME")
        biases = tf.Variable(tf.constant(0.0, shape=[256], dtype=tf.float32),
                             trainable=True, name="biases")
        conv2 = tf.nn.relu(tf.nn.bias_add(conv, biases))
        parameters += [kernel, biases]

        # 打印第二个卷积层的网络结构
        print(conv2.op.name, ' ', conv2.get_shape().as_list())

    # 添加一个LRN层和最大池化层
    lrn2 = tf.nn.lrn(conv2, 4, bias=1.0, alpha=0.001 / 9.0, beta=0.75, name="lrn2")
    pool2 = tf.nn.max_pool(lrn2, ksize=[1, 3, 3, 1], strides=[1, 2, 2, 1],
                           padding="VALID", name="pool2")
    # 打印池化层的网络结构
    print(pool2.op.name, ' ', pool2.get_shape().as_list())

    # 在命名空间conv3下实现第三个卷积层
    with tf.name_scope("conv3"):
        kernel = tf.Variable(tf.truncated_normal([3, 3, 256, 384],
                                                 dtype=tf.float32, stddev=1e-1),
                             name="weights")
        conv = tf.nn.conv2d(pool2, kernel, [1, 1, 1, 1], padding="SAME")
        biases = tf.Variable(tf.constant(0.0, shape=[384], dtype=tf.float32),
                             trainable=True, name="biases")
        conv3 = tf.nn.relu(tf.nn.bias_add(conv, biases))
        parameters += [kernel, biases]

        # 打印第三个卷积层的网络结构
        print(conv3.op.name, ' ', conv3.get_shape().as_list())

    # 在命名空间conv4下实现第四个卷积层
    with tf.name_scope("conv4"):
        kernel = tf.Variable(tf.truncated_normal([3, 3, 384, 384],
                                                 dtype=tf.float32, stddev=1e-1),
                             name="weights")
        conv = tf.nn.conv2d(conv3, kernel, [1, 1, 1, 1], padding="SAME")
        biases = tf.Variable(tf.constant(0.0, shape=[384], dtype=tf.float32),
                             trainable=True, name="biases")
        conv4 = tf.nn.relu(tf.nn.bias_add(conv, biases))
        parameters += [kernel, biases]

        # 打印第四个卷积层的网络结构
        print(conv4.op.name, ' ', conv4.get_shape().as_list())

    # 在命名空间conv5下实现第五个卷积层
    with tf.name_scope("conv5"):
        kernel = tf.Variable(tf.truncated_normal([3, 3, 384, 256],
                                                 dtype=tf.float32, stddev=1e-1),
                             name="weights")
        conv = tf.nn.conv2d(conv4, kernel, [1, 1, 1, 1], padding="SAME")
        biases = tf.Variable(tf.constant(0.0, shape=[256], dtype=tf.float32),
                             trainable=True, name="biases")

        conv5 = tf.nn.relu(tf.nn.bias_add(conv, biases))
        parameters += [kernel, biases]

        # 打印第五个卷积层的网络结构
        print(conv5.op.name, ' ', conv5.get_shape().as_list())

    # 添加一个最大池化层
    pool5 = tf.nn.max_pool(conv5, ksize=[1, 3, 3, 1], strides=[1, 2, 2, 1],
                           padding="VALID", name="pool5")
    # 打印最大池化层的网络结构
    print(pool5.op.name, ' ', pool5.get_shape().as_list())

    # 将pool5输出的矩阵汇总为向量的形式，为的是方便作为全连层的输入
    pool_shape = pool5.get_shape().as_list()
    nodes = pool_shape[1] * pool_shape[2] * pool_shape[3]
    reshaped = tf.reshape(pool5, [pool_shape[0], nodes])

    # 创建第一个全连接层
    with tf.name_scope("fc_1"):
        fc1_weights = tf.Variable(tf.truncated_normal([nodes, 4096], dtype=tf.float32,
                                                      stddev=1e-1), name="weights")
        fc1_bias = tf.Variable(tf.constant(0.0, shape=[4096],
                                           dtype=tf.float32), trainable=True, name="biases")
        fc_1 = tf.nn.relu(tf.matmul(reshaped, fc1_weights) + fc1_bias)
        parameters += [fc1_weights, fc1_bias]

        # 打印第一个全连接层的网络结构信息
        print(fc_1.op.name, ' ', fc_1.get_shape().as_list())

    # 创建第二个全连接层
    with tf.name_scope("fc_2"):
        fc2_weights = tf.Variable(tf.truncated_normal([4096, 4096], dtype=tf.float32,
                                                      stddev=1e-1), name="weights")
        fc2_bias = tf.Variable(tf.constant(0.0, shape=[4096],
                                           dtype=tf.float32), trainable=True, name="biases")
        fc_2 = tf.nn.relu(tf.matmul(fc_1, fc2_weights) + fc2_bias)
        parameters += [fc2_weights, fc2_bias]

        # 打印第二个全连接层的网络结构信息
        print(fc_2.op.name, ' ', fc_2.get_shape().as_list())

    # 返回全连接层处理的结果
    return fc_2, parameters


with tf.Graph().as_default():
    # 创建模拟的图片数据.
    image_size = 224
    images = tf.Variable(tf.random_normal([batch_size, image_size, image_size, 3],
                                          dtype=tf.float32, stddev=1e-1))

    # 在计算图中定义前向传播模型的运行，并得到不包括全连部分的参数
    # 这些参数用于之后的梯度计算
    fc_2, parameters = inference_op(images)

    init_op = tf.global_variables_initializer()

    # 配置会话，gpu_options.allocator_type 用于设置GPU的分配策略，值为"BFC"表示
    # 采用最佳适配合并算法
    config = tf.ConfigProto()
    config.gpu_options.allocator_type = "BFC"
    with tf.Session(config=config) as sess:
        sess.run(init_op)

        num_steps_burn_in = 10
        total_dura = 0.0
        total_dura_squared = 0.0

        back_total_dura = 0.0
        back_total_dura_squared = 0.0

        for i in range(num_batches + num_steps_burn_in):

            start_time = time.time()
            _ = sess.run(fc_2)
            duration = time.time() - start_time
            if i >= num_steps_burn_in:
                if i % 10 == 0:
                    print('%s: step %d, duration = %.3f' %
                          (datetime.now(), i - num_steps_burn_in, duration))
                total_dura += duration
                total_dura_squared += duration * duration
        average_time = total_dura / num_batches

        # 打印前向传播的运算时间信息
        print('%s: Forward across %d steps, %.3f +/- %.3f sec / batch' %
              (datetime.now(), num_batches, average_time,
               math.sqrt(total_dura_squared / num_batches - average_time * average_time)))

        # 使用gradients()求相对于pool5的L2 loss的所有模型参数的梯度
        # 函数原型gradients(ys,xs,grad_ys,name,colocate_gradients_with_ops,gate_gradients,
        # aggregation_method=None)
        # 一般情况下我们只需对参数ys、xs传递参数，他会计算ys相对于xs的偏导数，并将
        # 结果作为一个长度为len(xs)的列表返回，其他参数在函数定义时都带有默认值，
        # 比如grad_ys默认为None，name默认为gradients，colocate_gradients_with_ops默认
        # 为False，gate_gradients默认为False
        grad = tf.gradients(tf.nn.l2_loss(fc_2), parameters)

        # 运行反向传播测试过程
        for i in range(num_batches + num_steps_burn_in):
            start_time = time.time()
            _ = sess.run(grad)
            duration = time.time() - start_time
            if i >= num_steps_burn_in:
                if i % 10 == 0:
                    print('%s: step %d, duration = %.3f' %
                          (datetime.now(), i - num_steps_burn_in, duration))
                back_total_dura += duration
                back_total_dura_squared += duration * duration
        back_avg_t = back_total_dura / num_batches

        # 打印反向传播的运算时间信息
        print('%s: Forward-backward across %d steps, %.3f +/- %.3f sec / batch' %
              (datetime.now(), num_batches, back_avg_t,
               math.sqrt(back_total_dura_squared / num_batches - back_avg_t * back_avg_t)))

'''打印打内容
conv1/Relu   [32, 56, 56, 96]
pool1   [32, 27, 27, 96]
conv2/Relu   [32, 27, 27, 256]
pool2   [32, 13, 13, 256]
conv3/Relu   [32, 13, 13, 384]
conv4/Relu   [32, 13, 13, 384]
conv5/Relu   [32, 13, 13, 256]
pool5   [32, 6, 6, 256]
fc_1/Relu   [32, 4096]
fc_2/Relu   [32, 4096]
2018-04-27 22:36:29.513579: step 0, duration = 0.069
2018-04-27 22:36:30.244733: step 10, duration = 0.070
2018-04-27 22:36:30.946855: step 20, duration = 0.069
2018-04-27 22:36:31.640846: step 30, duration = 0.069
2018-04-27 22:36:32.338336: step 40, duration = 0.070
2018-04-27 22:36:33.034304: step 50, duration = 0.069
2018-04-27 22:36:33.727489: step 60, duration = 0.069
2018-04-27 22:36:34.563139: step 70, duration = 0.080
2018-04-27 22:36:35.262315: step 80, duration = 0.073
2018-04-27 22:36:35.992172: step 90, duration = 0.075
2018-04-27 22:36:36.636055: Forward across 100 steps, 0.072 +/- 0.006 sec / batch
2018-04-27 22:39:24.976134: step 0, duration = 0.227
2018-04-27 22:39:27.256709: step 10, duration = 0.228
2018-04-27 22:39:29.541159: step 20, duration = 0.228
2018-04-27 22:39:31.820606: step 30, duration = 0.227
2018-04-27 22:39:34.101613: step 40, duration = 0.227
2018-04-27 22:39:36.382223: step 50, duration = 0.228
2018-04-27 22:39:38.662726: step 60, duration = 0.227
2018-04-27 22:39:40.943501: step 70, duration = 0.227
2018-04-27 22:39:43.225993: step 80, duration = 0.228
2018-04-27 22:39:45.511031: step 90, duration = 0.230
2018-04-27 22:39:47.659823: Forward-backward across 100 steps, 0.229 +/- 0.008 sec / batch
'''



