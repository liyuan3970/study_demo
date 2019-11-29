# -*- coding: utf-8 -*
import argparse
import tensorflow as tf
from flyai.dataset import Dataset

from model import Model
from path import MODEL_PATH, LOG_PATH

# 数据获取辅助类
dataset = Dataset()

# 模型操作辅助类
model = Model(dataset)

'''
使用tensorflow实现自己的算法

'''
parser = argparse.ArgumentParser()
parser.add_argument("-e", "--EPOCHS", default=500, type=int, help="train epochs")
parser.add_argument("-b", "--BATCH", default=32, type=int, help="batch size")
args = parser.parse_args()
# 定义命名空间
x = tf.placeholder(tf.float32, shape=[None, 80, 80, 3], name='input_x')
y = tf.placeholder(tf.float32, shape=[None, 200], name='input_y')
keep_prob = tf.placeholder(tf.float32, name='keep_prob')


# 参数概要
def variable_summaries(var):
    with tf.name_scope('summaries'):
        mean = tf.reduce_mean(var)
        tf.summary.scalar('mean', mean)
        with tf.name_scope('stddev'):
            stddev = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
        tf.summary.scalar('stddev', stddev)
        tf.summary.scalar('max', tf.reduce_max(var))
        tf.summary.scalar('min', tf.reduce_min(var))
        tf.summary.histogram('histogram', var)


# 初始化权值
def weight_variable(shape, name):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial, name=name)


# 初始化偏置
def bias_variable(shape, name):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial, name=name)


#  定义卷积层网络的步长
def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


# 定义池化层网络的大小和步长
def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


x_image = tf.reshape(x, [-1, 80, 80, 3])

with tf.name_scope('Conv1'):
    # 初始化第一个卷积层的权值和偏置
    with tf.name_scope('W_conv1'):
        W_conv1 = weight_variable([5, 5, 3, 32], name='W_conv1')
    with tf.name_scope('b_conv1'):
        b_conv1 = bias_variable([32], name='b_conv1')
    with tf.name_scope('conv2d_1'):
        conv2d_1 = conv2d(x_image, W_conv1) + b_conv1
    with tf.name_scope('relu'):
        h_conv1 = tf.nn.relu(conv2d_1)
    with tf.name_scope('h_pool1'):
        h_pool1 = max_pool_2x2(h_conv1)

with tf.name_scope('Conv2'):
    # 初始化第二个卷积层的权值和偏置
    with tf.name_scope('W_conv2'):
        W_conv2 = weight_variable([5, 5, 32, 64], name='W_conv2')
    with tf.name_scope('b_conv2'):
        b_conv2 = bias_variable([64], name='b_conv2')
    with tf.name_scope('conv2d_2'):
        conv2d_2 = conv2d(h_pool1, W_conv2) + b_conv2
    with tf.name_scope('relu'):
        h_conv2 = tf.nn.relu(conv2d_2)
    with tf.name_scope('h_pool2'):
        h_pool2 = max_pool_2x2(h_conv2)

with tf.name_scope('fc1'):
    # 初始化第一个全连接层的权值
    with tf.name_scope('W_fc1'):
        W_fc1 = weight_variable([20 * 20 * 64, 256], name='W_fc1')
    with tf.name_scope('b_fc1'):
        b_fc1 = bias_variable([256], name='b_fc1')
    with tf.name_scope('h_pool2_flat'):
        h_pool2_flat = tf.reshape(h_pool2, [-1, 20 * 20 * 64], name='h_pool2_flat')  # 应该是这一句出现了问题
    with tf.name_scope('wx_plus_b1'):
        wx_plus_b1 = tf.matmul(h_pool2_flat, W_fc1) + b_fc1
    with tf.name_scope('relu'):
        h_fc1 = tf.nn.relu(wx_plus_b1)
    with tf.name_scope('h_fc1_drop'):
        h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob, name='h_fc1_drop')

with tf.name_scope('fc2'):
    with tf.name_scope('W_fc2'):
        W_fc2 = weight_variable([256, 200], name='W_fc2')
    with tf.name_scope('b_fc2'):
        b_fc2 = bias_variable([200], name='b_fc2')

prediction = tf.add(tf.matmul(h_fc1_drop, W_fc2), b_fc2, name='y_conv')  # 取出网络预测值

with tf.name_scope('loss_fucntion'):
    loss_function = tf.sqrt(tf.reduce_mean(tf.square(y - prediction)))
    tf.summary.scalar('loss_function', loss_function)

with tf.name_scope('train'):
    train_step = tf.train.AdamOptimizer(1e-4).minimize(loss_function)

merged = tf.summary.merge_all()

saver = tf.train.Saver()
best_accuracy = 0.0
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    train_writer = tf.summary.FileWriter(LOG_PATH, sess.graph)
    test_writer = tf.summary.FileWriter(LOG_PATH, sess.graph)

    for i in range(args.EPOCHS):
        x_train, y_train, x_test, y_test = dataset.next_batch(args.BATCH)
        _, loss = sess.run([train_step, loss_function], feed_dict={x: x_train, y: y_train, keep_prob: 0.5})
        summary = sess.run(merged, feed_dict={x: x_train, y: y_train, keep_prob: 1.0})
        train_writer.add_summary(summary, i)
        model.save_model(sess, MODEL_PATH, overwrite=True)
        print("step:", i, "loss:", loss)
        print(str(i + 1) + "/" + str(args.EPOCHS))
