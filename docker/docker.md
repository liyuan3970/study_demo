#docker
##常用基本指令
1. 下载镜像
   1. docker search ubuntu18.04 --> **查找ubuntu18.04的镜像**
   2. docker pull ubuntu18.04 --> **下载ubuntu18.04的镜像**
   3. deocker image ls --> **查看镜像名称**
2. 进入镜像
   1. 直接进入
      1. docker run -it 镜像名(ubuntu) 
      2. 一系列操作
      3. exit --> 退出**此时会返回一个镜像id**
   2. 保存上述操作 
      1. docker commit **镜像ID（sdwq3fsdff）**  镜像名称(ubuntu)
