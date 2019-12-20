import collections
import tensorflow as tf
from tensorflow.contrib import slim


class Block(collections.namedtuple("block", ["name", "residual_unit", "args"])):
    "A named tuple describing a ResNet Block"
    # namedtuple()函数原型为：
    # collections.namedtuple(typename,field_names,verbose,rename)


def conv2d_same(inputs, num_outputs, kernel_size, stride, scope=None):
    # 如果步长为1，则直接使用padding="SAME"的方式进行卷积操作
    # 一般步长不为1的情况出现在残差学习块的最后一个卷积操作中
    if stride == 1:
        return slim.conv2d(inputs, num_outputs, kernel_size, stride=1,
                           padding="SAME", scope=scope)
    else:
        pad_begin = (kernel_size - 1) // 2
        pad_end = kernel_size - 1 - pad_begin

        # pad()函数用于对矩阵进行定制填充
        # 在这里用于对inputs进行向上填充pad_begin行0，向下填充pad_end行0，
        # 向左填充pad_begin行0，向右填充pad_end行0
        inputs = tf.pad(inputs,
                        [[0, 0], [pad_begin, pad_end], [pad_begin, pad_end], [0, 0]])
        return slim.conv2d(inputs, num_outputs, kernel_size, stride=stride,
                           padding="VALID", scope=scope)


@slim.add_arg_scope
def residual_unit(inputs, depth, depth_residual, stride, outputs_collections=None,
                  scope=None):
    with tf.variable_scope(scope, "residual_v2", [inputs]) as sc:

        # 输入的通道数，取inputs的形状的最后一个元素
        depth_input = slim.utils.last_dimension(inputs.get_shape(), min_rank=4)

        # 使用slim.batch_norm()函数进行BatchNormalization操作
        preact = slim.batch_norm(inputs, activation_fn=tf.nn.relu, scope="preac")

        # 如果本块的depth值(depth参数)等于上一个块的depth(depth_input)，则考虑进行降采样操作，
        # 如果depth值不等于depth_input，则使用conv2d()函数使输入通道数和输出通道数一致
        if depth == depth_input:
            # 如果stride等于1，则不进行降采样操作，如果stride不等于1，则使用max_pool2d
            # 进行步长为stride且池化核为1x1的降采样操作
            if stride == 1:
                identity = inputs
            else:
                identity = slim.max_pool2d(inputs, [1, 1], stride=stride, scope="shortcut")
        else:
            identity = slim.conv2d(preact, depth, [1, 1], stride=stride, normalizer_fn=None,
                                   activation_fn=None, scope="shortcut")

        # 在一个残差学习块中的3个卷积层
        residual = slim.conv2d(preact, depth_residual, [1, 1], stride=1, scope="conv1")
        residual = conv2d_same(residual, depth_residual, 3, stride, scope="conv2")
        residual = slim.conv2d(residual, depth, [1, 1], stride=1, normalizer_fn=None,
                               activation_fn=None, scope="conv3")

        # 将identity的结果和residual的结果相加
        output = identity + residual

        result = slim.utils.collect_named_outputs(outputs_collections, sc.name, output)

        return result


def resnet_v2_152(inputs, num_classes, reuse=None, scope="resnet_v2_152"):
    blocks = [
        Block("block1", residual_unit, [(256, 64, 1), (256, 64, 1), (256, 64, 2)]),
        Block("block2", residual_unit, [(512, 128, 1)] * 7 + [(512, 128, 2)]),
        Block("block3", residual_unit, [(1024, 256, 1)] * 35 + [(1024, 256, 2)]),
        Block("block4", residual_unit, [(2048, 512, 1)] * 3)]
    return resnet_v2(inputs, blocks, num_classes, reuse=reuse, scope=scope)


def resnet_v2(inputs, blocks, num_classes, reuse=None, scope=None):
    with tf.variable_scope(scope, "resnet_v2", [inputs], reuse=reuse) as sc:
        end_points_collection = sc.original_name_scope + "_end_points"

        # 对函数residual_unit()的outputs_collections参数使用参数空间
        with slim.arg_scope([residual_unit], outputs_collections=end_points_collection):

            # 创建ResNet的第一个卷积层和池化层，卷积核大小7x7，深度64，池化核大侠3x3
            with slim.arg_scope([slim.conv2d], activation_fn=None, normalizer_fn=None):
                net = conv2d_same(inputs, 64, 7, stride=2, scope="conv1")
            net = slim.max_pool2d(net, [3, 3], stride=2, scope="pool1")

            # 在两个嵌套的for循环内调用residual_unit()函数堆砌ResNet的结构
            for block in blocks:
                # block.name分别为block1、block2、block3和block4
                with tf.variable_scope(block.name, "block", [net]) as sc:

                    # tuple_value为Block类的args参数中的每一个元组值，
                    # i是这些元组在每一个Block的args参数中的序号
                    for i, tuple_value in enumerate(block.args):
                        # i的值从0开始，对于第一个unit，i需要加1
                        with tf.variable_scope("unit_%d" % (i + 1), values=[net]):
                            # 每一个元组都有3个数组成，将这三个数作为参数传递到Block类的
                            # residual_unit参数中，在定义blockss时，这个参数就是函数residual_unit()
                            depth, depth_bottleneck, stride = tuple_value
                            net = block.residual_unit(net, depth=depth, depth_residual=depth_bottleneck,
                                                      stride=stride)
                    # net就是每一个块的结构
                    net = slim.utils.collect_named_outputs(end_points_collection, sc.name, net)

            # 对net使用slim.batch_norm()函数进行BatchNormalization操作
            net = slim.batch_norm(net, activation_fn=tf.nn.relu, scope="postnorm")

            # 创建全局平均池化层
            net = tf.reduce_mean(net, [1, 2], name="pool5", keep_dims=True)

            # 如果定义了num_classes，则通过1x1池化的方式获得数目为num_classes的输出
            if num_classes is not None:
                net = slim.conv2d(net, num_classes, [1, 1], activation_fn=None,
                                  normalizer_fn=None, scope="logits")

            return net
