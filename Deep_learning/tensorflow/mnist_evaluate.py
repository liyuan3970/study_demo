import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data", one_hot=True)


# 定义相同的前向传播过程，要保持命名空间和变量名的一致
def hidden_layer(input_tensor, regularizer, name):
    with tf.variable_scope("hidden_layer"):
        weights = tf.get_variable("weights", [784, 500],
                                  initializer=tf.truncated_normal_initializer(stddev=0.1))
        if regularizer != None:
            tf.add_to_collection("losses", regularizer(weights))
        biases = tf.get_variable("biases", [500], initializer=tf.constant_initializer(0.0))
        hidden_layer = tf.nn.relu(tf.matmul(input_tensor, weights) + biases)

    with tf.variable_scope("hidden_layer_output"):
        weights = tf.get_variable("weights", [500, 10],
                                  initializer=tf.truncated_normal_initializer(stddev=0.1))
        if regularizer != None:
            tf.add_to_collection("losses", regularizer(weights))
        biases = tf.get_variable("biases", [10], initializer=tf.constant_initializer(0.0))
        hidden_layer_output = tf.matmul(hidden_layer, weights) + biases
    return hidden_layer_output


x = tf.placeholder(tf.float32, [None, 784], name="x-input")
y_ = tf.placeholder(tf.float32, [None, 10], name="y-input")

# 因为测试时不必关注正则化损失的值，所以不会传入正则化的办法
y = hidden_layer(x, None, name="y")

# 计算正确率的过程也基本和第六章的样例一致
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
variable_averages = tf.train.ExponentialMovingAverage(0.99)

# 通过变量重命名的方式加载模型，这里使用了滑动平均类提供的variables_to_restore()
# 于是就免去了在前向传播过程中调用求解滑动平均的函数来获取滑动平均值的过程
saver = tf.train.Saver(variable_averages.variables_to_restore())

with tf.Session() as sess:
    validate_feed = {x: mnist.validation.images, y_: mnist.validation.labels}
    test_feed = {x: mnist.test.images, y_: mnist.test.labels}

    # get_checkpoint_state()函数会通过checkpoint文件自动找到目录中最新模型的文件名
    # 函数原型get_checkpoint_state(checkpoint_dir,latest_filename)
    ckpt = tf.train.get_checkpoint_state("mnist_model/")

    # 加载模型
    saver.restore(sess, ckpt.model_checkpoint_path)

    # 通过文件名得到模型保存时迭代的轮数
    global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
    print("The latest ckpt is mnist_model.ckpt-%s" % (global_step))
    # 输出The latest ckpt is mnist_model.ckpt-29001

    # 计算在验证数据集上的准确率并打印出来
    accuracy_score = sess.run(accuracy, feed_dict=validate_feed)
    print("After %s training step(s), validation accuracy = %g%%"
          % (global_step, accuracy_score * 100))
    # 输出After 29001 training step(s), validation accuracy = 98.62%

    # 计算在测试数据集上的准确率并打印出来
    test_accuracy = sess.run(accuracy, feed_dict=test_feed)
    print("After %s trainging step(s) ,test accuracy = %g%%"
          % (global_step, test_accuracy * 100))
    # 输出After 29001 trainging step(s) ,test accuracy = 98.51%

