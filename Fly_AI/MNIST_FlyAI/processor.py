# -*- coding: utf-8 -*
import numpy as np
import cv2
from flyai.processor.base import Base
from path import DATA_PATH
import os

class Processor(Base):
    def input_x(self, image_path):
        # 获取图片路径
        path = os.path.join(DATA_PATH, image_path)
        # 读取图片
        img = cv2.imread(path)
        # 将图片BGR格式转换成RGB格式
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # 对图片进行归一化操作
        img = img / 255.0
        # 将图片转换成 [28, 28, 1]
        img = img[:, :, 0]
        img = img.reshape(28, 28, 1)
        #img = img.reshape(784, 1)
        #print(img.shape)
        return img

    def input_y(self, label):
        # 对标签进行onehot化
        one_hot_label = np.zeros([10])
        # 生成全0矩阵
        one_hot_label[label] = 1
        # 相应标签位置置
        return one_hot_label

    def output_y(self, data):
        return np.argmax(data)
