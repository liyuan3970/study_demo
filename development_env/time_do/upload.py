# coding:utf8
import paramiko
import schedule
import time
import datetime
import os
from datetime import datetime, date, timedelta

'''可以调节的参数'''

ip = "192.168.8.135"
port = 22
name ="liyuan3970"
password = "123456"
local_path = '/home/liyuan3970/test_demo/time/'
remote_path = '/home/liyuan3970/demo/'
filename ='a.txt'
remote_file_name='b.txt'

runtime ='16:10'
date = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
year = date[2:4]
month =date[5:7]
day = date[8:10]


def job_upload():
    transport = paramiko.Transport((ip, port))    # 获取Transport实例
    transport.connect(username=name, password=password)    # 建立连接
    # 创建sftp对象，SFTPClient是定义怎么传输文件、怎么交互文件
    sftp = paramiko.SFTPClient.from_transport(transport)
    # 将本地 a.txt 上传至服务器 /www/test.py。文件上传并重命名为b.txt
    sftp.put(local_path+filename, remote_path+remote_file_name)
    # 关闭连接
    transport.close()



if __name__ == '__main__':
    print("主程序")
    schedule.every().day.at(runtime).do(job_upload)
    while True:
        schedule.run_pending()