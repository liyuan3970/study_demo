import tensorflow as tf
import numpy as np

def fun01():
    m1=np.array([[1,2],[3,4]])
    m2=tf.constant([[1,2],[3,4]],dtype=tf.float32)
    m3=tf.convert_to_tensor(m1,dtype=tf.float32)
    m4=m2+m3
    with tf.Session() as sess:
        res=sess.run(m4)
        print(res)

#占位符函数
fun01()
#m=tf.Variable([[1,2],[3,4]],dtype=tf.float32)
t1=tf.placeholder(dtype=tf.float32)
t2=tf.placeholder(dtype=tf.float32)
t3=t1+t2
with tf.Session() as session:
    res=session.run(t3,feed_dict={t1:2,t2:3})
    print(res)





