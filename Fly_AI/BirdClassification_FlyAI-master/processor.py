# -*- coding: utf-8 -*
import cv2
import numpy as np
from flyai.processor.base import Base
from flyai.processor.download import check_download
from skimage import transform

from path import DATA_PATH


class Processor(Base):

    def input_x(self, image_path):
        '''
        参数为csv中作为输入x的一条数据，该方法会被Dataset多次调用
        '''
        # path 为图片的真实路径
        path = check_download(image_path, DATA_PATH)
        image = cv2.imread(path)
        image = np.array(image)  # 图片转化为矩阵向量
        image = transform.resize(image, output_shape=(80, 80))
        print(image.shape)#(80,80,3)
        return image

    def input_y(self, label):
        '''
        参数为csv中作为输入y的一条数据，该方法会被Dataset多次调用
        '''
        temp = np.zeros(200)
        temp[label] = 1
        return temp

    def output_y(self, data):
        '''
        验证时使用，把模型输出的y转为对应的结果
        '''

        return data.argmax()
