#docker
##常用基本指令
1. 下载镜像
   1. docker search ubuntu18.04 --> **查找ubuntu18.04的镜像**
   2. docker pull ubuntu18.04 --> **下载ubuntu18.04的镜像**

2. 进入镜像
   1. 直接进入
      1. docker run -it 镜像名(ubuntu) 
      2. 一系列操作
      3. exit --> 退出**此时会返回一个镜像id**
   2. 保存上述操作 
      1. docker commit **容器ID/容器名称（sdwq3fsdff）**  镜像名称(ubuntu)
   3. 自定义容器名字运行容器
      1. docker run --name =自定义名 -it IMAGE /bin/bash

3. 查看已知镜像
   1. docker image ls --> **查看镜像名称**
   2. docker ps -a --> **查看所有容器**
   3. docker ps -l -->**查看最近运行的容器** 
   4. docker inspect 容器ID -->**返回配置信息**

4. 后台运行docker容器
   1. docker run -d **容器名称(filetest)** 
   2. docker run -it **容器名称(filetest)**<br/>ctrl +p ctrl +q
   3. 查看此时运行的docke容器 --> docker ps
#知识点总结
![image](docker.png)
