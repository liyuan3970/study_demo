import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data",one_hot=True)
batch_size = 100
learning_rate = 0.8
learning_rate_decay = 0.999
max_steps = 30000

#更改前向传播算法的定义,将得到权重参数和偏执参数的过程封装到了一个函数中
def hidden_layer(input_tensor,regularizer,name):
#要多多体会使用变量空间来管理变量的方便性。使用get_variable()函数会在训练神经
#网络时创建这些变量而在测试过程中通过保存的模型加载这些变量的取值，在测试过程中
#可以在加载变量时将滑动平均变量重命名，这样就会在测试过程中使用变量的滑动平均值
    with tf.variable_scope("hidden_layer"):
        weights = tf.get_variable("weights", [784, 500],
                         initializer=tf.truncated_normal_initializer(stddev=0.1))

        #如果调用该函数时传入了正则化的方法 ，那么在这里将参数求
        if regularizer!=None:
            tf.add_to_collection("losses",regularizer(weights))
        biases = tf.get_variable("biases", [500], initializer=tf.constant_initializer(0.0))
        hidden_layer = tf.nn.relu(tf.matmul(input_tensor, weights) + biases)

    with tf.variable_scope("hidden_layer_output"):
        weights = tf.get_variable("weights", [500, 10],
                                  initializer=tf.truncated_normal_initializer(stddev=0.1))
        if regularizer!=None:
            tf.add_to_collection("losses",regularizer(weights))
        biases = tf.get_variable("biases", [10], initializer=tf.constant_initializer(0.0))
        hidden_layer_output = tf.matmul(hidden_layer, weights) + biases
    return hidden_layer_output

#定义输出输出的部分没变
x = tf.placeholder(tf.float32, [None,784],name="x-input")
y_ = tf.placeholder(tf.float32, [None,10],name="y-output")

#定义L2正则化的办法被提前
regularizer = tf.contrib.layers.l2_regularizer(0.0001)

#将L2正则化的办法传入到hidden_layer()函数中
y = hidden_layer(x,regularizer,name="y")

training_step = tf.Variable(0,trainable=False)
averages_class = tf.train.ExponentialMovingAverage(0.99,training_step)
averages_op = averages_class.apply(tf.trainable_variables())

#不再定义average_y，因为average_y只在比较正确率时有用，
#在模型保存的程序中我们只输出损失
#average_y = hidden_layer(x,averages_class,name="average_y",reuse=True)

cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y,
                                                 labels=tf.argmax(y_, 1)) #tf.argmax()
#计算总损失
loss = tf.reduce_mean(cross_entropy)+tf.add_n(tf.get_collection("losses"))

laerning_rate = tf.train.exponential_decay(learning_rate,training_step,
                mnist.train.num_examples/batch_size,learning_rate_decay)
train_step= tf.train.GradientDescentOptimizer(learning_rate).\
                                minimize(loss,global_step=training_step)

#也可以采用train_op = tf.group(train_step,averages_op)的形式
with tf.control_dependencies([train_step, averages_op]):
    train_op = tf.no_op(name="train")

#初始化Saver持久化类
saver=tf.train.Saver()
with tf.Session() as sess:
    tf.global_variables_initializer().run()

    #进行30000轮到训练
    for i in range(max_steps):
        x_train, y_train = mnist.train.next_batch(batch_size)
        _, loss_value, step = sess.run([train_op, loss, training_step],
                                          feed_dict={x: x_train, y_: y_train})

        #每隔1000轮训练就输出当前训练batch上的损失函数大小，并保存一次模型
        if i % 1000 == 0:
            print("After %d training step(s), loss on training batch is "
                                                    "%g." % (step, loss_value))
            #保存模型的时候给出了global_step参数，这样可以让每个模型文件都添加
            #代表了训练轮数的后缀，这样做的原因是方便检索
            saver.save(sess, "mnist_model/mnist_model.ckpt",global_step=training_step)