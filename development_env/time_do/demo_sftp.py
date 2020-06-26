# coding:utf8
import paramiko
 
transport = paramiko.Transport(("192.168.8.135", 22))    # 获取Transport实例
transport.connect(username="liyuan3970", password="051219")    # 建立连接
 
# 创建sftp对象，SFTPClient是定义怎么传输文件、怎么交互文件
sftp = paramiko.SFTPClient.from_transport(transport)
 
# 将本地 api.py 上传至服务器 /www/test.py。文件上传并重命名为test.py
sftp.put("/home/liyuan3970/test_demo/time/a.txt", "/home/liyuan3970/demo/b.txt")
 
# 将服务器 /www/test.py 下载到本地 aaa.py。文件下载并重命名为aaa.py
#sftp.get("/www/test.py", "E:/test/aaa.py")
 
# 关闭连接
transport.close()