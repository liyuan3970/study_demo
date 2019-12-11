import tensorflow as tf
from datetime import datetime
import math
import time

batch_size = 12
num_batches = 100


# 定义卷积操作
def conv_op(input, name, kernel_h, kernel_w, num_out, step_h, step_w, para):
    # num_in是输入的深度，这个参数被用来确定过滤器的输入通道数
    num_in = input.get_shape()[-1].value

    with tf.name_scope(name) as scope:
        kernel = tf.get_variable(scope + "w", shape=[kernel_h, kernel_w, num_in, num_out],
                                 dtype=tf.float32,
                                 initializer=tf.contrib.layers.xavier_initializer_conv2d())
        conv = tf.nn.conv2d(input, kernel, (1, step_h, step_w, 1), padding="SAME")
        biases = tf.Variable(tf.constant(0.0, shape=[num_out], dtype=tf.float32),
                             trainable=True, name="b")
        # 计算relu后的激活值
        activation = tf.nn.relu(tf.nn.bias_add(conv, biases), name=scope)

        para += [kernel, biases]
        return activation


# 定义全连操作
def fc_op(input, name, num_out, para):
    # num_in为输入单元的数量
    num_in = input.get_shape()[-1].value

    with tf.name_scope(name) as scope:
        weights = tf.get_variable(scope + "w", shape=[num_in, num_out], dtype=tf.float32,
                                  initializer=tf.contrib.layers.xavier_initializer())
        biases = tf.Variable(tf.constant(0.1, shape=[num_out], dtype=tf.float32), name="b")

        # tf.nn.relu_layer()函数会同时完成矩阵乘法以加和偏置项并计算relu激活值
        # 这是分步编程的良好替代
        activation = tf.nn.relu_layer(input, weights, biases)

        para += [weights, biases]
        return activation


# 定义前向传播的计算过程，input参数的大小为224x224x3，也就是输入的模拟图片数据
def inference_op(input, keep_prob):
    parameters = []

    # 第一段卷积，输出大小为112x112x64(省略了第一个batch_size参数)
    conv1_1 = conv_op(input, name="conv1_1", kernel_h=3, kernel_w=3, num_out=4,
                      step_h=1, step_w=1, para=parameters)
    conv1_2 = conv_op(conv1_1, name="conv1_2", kernel_h=3, kernel_w=3, num_out=64,
                      step_h=1, step_w=1, para=parameters)
    pool1 = tf.nn.max_pool(conv1_2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1],
                           padding="SAME", name="pool1")
    print(pool1.op.name, ' ', pool1.get_shape().as_list())

    # 第二段卷积，输出大小为56x56x128(省略了第一个batch_size参数)
    conv2_1 = conv_op(pool1, name="conv2_1", kernel_h=3, kernel_w=3, num_out=128,
                      step_h=1, step_w=1, para=parameters)
    conv2_2 = conv_op(conv2_1, name="conv2_2", kernel_h=3, kernel_w=3, num_out=128,
                      step_h=1, step_w=1, para=parameters)
    pool2 = tf.nn.max_pool(conv2_2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1],
                           padding="SAME", name="pool2")
    print(pool2.op.name, ' ', pool2.get_shape().as_list())

    # 第三段卷积，输出大小为28x28x256(省略了第一个batch_size参数)
    conv3_1 = conv_op(pool2, name="conv3_1", kernel_h=3, kernel_w=3, num_out=256,
                      step_h=1, step_w=1, para=parameters)
    conv3_2 = conv_op(conv3_1, name="conv3_2", kernel_h=3, kernel_w=3, num_out=256,
                      step_h=1, step_w=1, para=parameters)
    conv3_3 = conv_op(conv3_2, name="conv3_3", kernel_h=3, kernel_w=3, num_out=256,
                      step_h=1, step_w=1, para=parameters)
    pool3 = tf.nn.max_pool(conv3_3, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1],
                           padding="SAME", name="pool3")
    print(pool2.op.name, ' ', pool2.get_shape().as_list())

    # 第四段卷积，输出大小为14x14x512(省略了第一个batch_size参数)
    conv4_1 = conv_op(pool3, name="conv4_1", kernel_h=3, kernel_w=3, num_out=512,
                      step_h=1, step_w=1, para=parameters)
    conv4_2 = conv_op(conv4_1, name="conv4_2", kernel_h=3, kernel_w=3, num_out=512,
                      step_h=1, step_w=1, para=parameters)
    conv4_3 = conv_op(conv4_2, name="conv4_3", kernel_h=3, kernel_w=3, num_out=512,
                      step_h=1, step_w=1, para=parameters)
    pool4 = tf.nn.max_pool(conv4_3, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1],
                           padding="SAME", name="pool4")
    print(pool4.op.name, ' ', pool4.get_shape().as_list())

    # 第五段卷积，输出大小为7x7x512(省略了第一个batch_size参数)
    conv5_1 = conv_op(pool4, name="conv5_1", kernel_h=3, kernel_w=3, num_out=512,
                      step_h=1, step_w=1, para=parameters)
    conv5_2 = conv_op(conv5_1, name="conv5_2", kernel_h=3, kernel_w=3, num_out=512,
                      step_h=1, step_w=1, para=parameters)
    conv5_3 = conv_op(conv5_2, name="conv5_3", kernel_h=3, kernel_w=3, num_out=512,
                      step_h=1, step_w=1, para=parameters)
    pool5 = tf.nn.max_pool(conv5_3, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1],
                           padding="SAME", name="pool5")
    print(pool5.op.name, ' ', pool5.get_shape().as_list())

    # pool5的结果汇总为一个向量的形式
    pool_shape = pool5.get_shape().as_list()
    flattened_shape = pool_shape[1] * pool_shape[2] * pool_shape[3]
    reshped = tf.reshape(pool5, [-1, flattened_shape], name="reshped")

    # 第一个全连层
    fc_6 = fc_op(reshped, name="fc6", num_out=4096, para=parameters)
    fc_6_drop = tf.nn.dropout(fc_6, keep_prob, name="fc6_drop")

    # 第二个全连层
    fc_7 = fc_op(fc_6_drop, name="fc7", num_out=4096, para=parameters)
    fc_7_drop = tf.nn.dropout(fc_7, keep_prob, name="fc7_drop")

    # 第三个全连层及softmax层
    fc_8 = fc_op(fc_7_drop, name="fc8", num_out=1000, para=parameters)
    softmax = tf.nn.softmax(fc_8)

    # predictions模拟了通过argmax得到预测结果
    predictions = tf.argmax(softmax, 1)
    return predictions, softmax, fc_8, parameters


with tf.Graph().as_default():
    # 创建模拟的图片数据
    image_size = 224
    images = tf.Variable(tf.random_normal([batch_size, image_size, image_size, 3],
                                          dtype=tf.float32, stddev=1e-1))

    # Dropout的keep_prob会根据前向传播或者反向传播而有所不同，在前向传播时，
    # keep_prob=1.0，在反向传播时keep_prob=0.5
    keep_prob = tf.placeholder(tf.float32)

    # 为当前计算图添加前向传播过程
    predictions, softmax, fc_8, parameters = inference_op(images, keep_prob)

    init_op = tf.global_variables_initializer()

    # 使用BFC算法确定GPU内存最佳分配策略
    config = tf.ConfigProto()
    config.gpu_options.allocator_type = "BFC"
    with tf.Session(config=config) as sess:
        sess.run(init_op)
        num_steps_burn_in = 10

        total_dura = 0.0
        total_dura_squared = 0.0

        back_total_dura = 0.0
        back_total_dura_squared = 0.0

        # 运行前向传播的测试过程
        for i in range(num_batches + num_steps_burn_in):
            start_time = time.time()
            _ = sess.run(predictions, feed_dict={keep_prob: 1.0})
            duration = time.time() - start_time
            if i >= num_steps_burn_in:
                if i % 10 == 0:
                    print("%s: step %d, duration = %.3f" %
                          (datetime.now(), i - num_steps_burn_in, duration))
                total_dura += duration
                total_dura_squared += duration * duration
        average_time = total_dura / num_batches

        # 打印前向传播的运算时间信息
        print("%s: Forward across %d steps, %.3f +/- %.3f sec / batch" %
              (datetime.now(), num_batches, average_time,
               math.sqrt(total_dura_squared / num_batches - average_time * average_time)))

        # 定义求解梯度的操作
        grad = tf.gradients(tf.nn.l2_loss(fc_8), parameters)

        # 运行反向传播测试过程
        for i in range(num_batches + num_steps_burn_in):
            start_time = time.time()
            _ = sess.run(grad, feed_dict={keep_prob: 0.5})
            duration = time.time() - start_time
            if i >= num_steps_burn_in:
                if i % 10 == 0:
                    print("%s: step %d, duration = %.3f" %
                          (datetime.now(), i - num_steps_burn_in, duration))
                back_total_dura += duration
                back_total_dura_squared += duration * duration
        back_avg_t = back_total_dura / num_batches

        # 打印反向传播的运算时间信息
        print("%s: Forward-backward across %d steps, %.3f +/- %.3f sec / batch" %
              (datetime.now(), num_batches, back_avg_t,
               math.sqrt(back_total_dura_squared / num_batches - back_avg_t * back_avg_t)))

'''打印的内容
pool1   [12, 112, 112, 64]
pool2   [12, 56, 56, 128]
pool2   [12, 56, 56, 128]
pool4   [12, 14, 14, 512]
pool5   [12, 7, 7, 512]
2018-04-28 09:35:34.973581: step 0, duration = 0.353
2018-04-28 09:35:38.553523: step 10, duration = 0.366
2018-04-28 09:35:42.124513: step 20, duration = 0.351
2018-04-28 09:35:45.691710: step 30, duration = 0.351
2018-04-28 09:35:49.274942: step 40, duration = 0.366
2018-04-28 09:35:52.828938: step 50, duration = 0.351
2018-04-28 09:35:56.380751: step 60, duration = 0.351
2018-04-28 09:35:59.951856: step 70, duration = 0.364
2018-04-28 09:36:03.583875: step 80, duration = 0.360
2018-04-28 09:36:07.214103: step 90, duration = 0.357
2018-04-28 09:36:10.460588: Forward across 100 steps, 0.358 +/- 0.007 sec / batch
2018-04-28 09:36:27.955719: step 0, duration = 1.364
2018-04-28 09:36:41.584773: step 10, duration = 1.363
2018-04-28 09:36:55.197996: step 20, duration = 1.355
2018-04-28 09:37:08.822001: step 30, duration = 1.360
2018-04-28 09:37:22.442811: step 40, duration = 1.364
2018-04-28 09:37:36.091333: step 50, duration = 1.358
2018-04-28 09:37:49.744742: step 60, duration = 1.362
2018-04-28 09:38:03.358585: step 70, duration = 1.355
2018-04-28 09:38:16.874355: step 80, duration = 1.331
2018-04-28 09:38:30.432612: step 90, duration = 1.356
2018-04-28 09:38:42.658764: Forward-backward across 100 steps, 1.361 +/- 0.009 sec / batch
'''