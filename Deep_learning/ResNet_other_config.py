#50层深的ResNet使用到的Block
def resnet_v2_50(inputs,num_classes=None,global_pool=True,
                 reuse=None,scope="resnet_v2_50"):
    blocks = [
        Block("block1", residual_unit, [(256, 64, 1),(256, 64, 1),(256, 64, 2)]),
        Block("block2", residual_unit, [(512, 128, 1)] * 3 + [(512, 128, 2)]),
        Block("block3", residual_unit, [(1024, 256, 1)] * 5 + [(1024, 256, 2)]),
        Block("block4", residual_unit, [(2048, 512, 1)] * 3)]
    return resnet_v2(inputs, blocks, num_classes,reuse=reuse, scope=scope)

#101层深的ResNet使用到的Block
def resnet_v2_101(inputs,num_classes=None,global_pool=True,
                  reuse=None,scope="resnet_v2_101"):
    blocks = [
        Block("block1", residual_unit, [(256, 64, 1),(256, 64, 1),(256, 64, 2)]),
        Block("block2", residual_unit, [(512, 128, 1)] * 3 + [(512, 128, 2)]),
        Block("block3", residual_unit, [(1024, 256, 1)] * 22 + [(1024, 256, 2)]),
        Block("block4", residual_unit, [(2048, 512, 1),(2048, 512, 1),(2048, 512, 1)])]
    return resnet_v2(inputs, blocks, num_classes,reuse=reuse, scope=scope)

#200层深的ResNet使用到的Block
def resnet_v2_200(inputs,num_classes=None,global_pool=True,
                  reuse=None,scope='resnet_v2_200'):
    blocks = [
        Block("block1", bottleneck, [(256, 64, 1),(256, 64, 1),(256, 64, 2)]),
        Block("block2", bottleneck, [(512, 128, 1)] * 23 + [(512, 128, 2)]),
        Block("block3", bottleneck, [(1024, 256, 1)] * 35 + [(1024, 256, 2)]),
        Block("block4", bottleneck, [(2048, 512, 1)] * 3)]
    return resnet_v2(inputs, blocks, num_classes,reuse=reuse, scope=scope)