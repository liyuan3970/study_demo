# -*- coding: utf-8 -*
import numpy
import os
import tensorflow as tf
from flyai.model.base import Base
from tensorflow.python.saved_model import tag_constants

from path import MODEL_PATH

TENSORFLOW_MODEL_DIR = "best"


class Model(Base):
    def __init__(self, data):
        self.data = data

    def predict(self, **data):

        with tf.Session() as session:
            tf.saved_model.loader.load(session, [tag_constants.SERVING], os.path.join(MODEL_PATH, TENSORFLOW_MODEL_DIR))
            input_x = session.graph.get_tensor_by_name(self.get_tensor_name('input_x'))
            y_conv = session.graph.get_tensor_by_name(self.get_tensor_name('y_conv'))
            keep_prob = session.graph.get_tensor_by_name(self.get_tensor_name('keep_prob'))
            x_data = self.data.predict_data(**data)
            predict = session.run(y_conv, feed_dict={input_x: x_data, keep_prob: 1.0})
            return self.data.to_categorys(predict)

    def predict_all(self, datas):

        with tf.Session() as session:
            tf.saved_model.loader.load(session, [tag_constants.SERVING], os.path.join(MODEL_PATH, TENSORFLOW_MODEL_DIR))
            input_x = session.graph.get_tensor_by_name(self.get_tensor_name('input_x'))
            y_conv = session.graph.get_tensor_by_name(self.get_tensor_name('y_conv'))
            keep_prob = session.graph.get_tensor_by_name(self.get_tensor_name('keep_prob'))
            outputs = []
            for data in datas:
                x_data = self.data.predict_data(**data)
                predict = session.run(y_conv, feed_dict={input_x: x_data, keep_prob: 1.0})
                outputs.append(self.data.to_categorys(predict))
            return outputs

    def save_model(self, session, path, name=TENSORFLOW_MODEL_DIR, overwrite=False):

        if overwrite:
            self.delete_file(path)

        builder = tf.saved_model.builder.SavedModelBuilder(os.path.join(path, name))
        builder.add_meta_graph_and_variables(session, [tf.saved_model.tag_constants.SERVING])
        builder.save()

    def batch_iter(self, x, y, batch_size=128):

        data_len = len(x)
        num_batch = int((data_len - 1) / batch_size) + 1

        indices = numpy.random.permutation(numpy.arange(data_len))
        x_shuffle = x[indices]
        y_shuffle = y[indices]

        for i in range(num_batch):
            start_id = i * batch_size
            end_id = min((i + 1) * batch_size, data_len)
            yield x_shuffle[start_id:end_id], y_shuffle[start_id:end_id]

    def get_tensor_name(self, name):
        return name + ":0"

    def delete_file(self, path):
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
