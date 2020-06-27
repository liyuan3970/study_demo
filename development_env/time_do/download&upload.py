# 李渊 2020 06 26 21：57
'''自动下载M4数据到samba文件中,需要pip install schedule 并在GDSJavaClient客户端jar文件所在目录下运行'''
import schedule
import time
import datetime
import os
from datetime import datetime, date, timedelta

'''可以调节的参数'''
runtime ='06:00'
yesterday = (date.today() + timedelta(days = -1)).strftime("%Y-%m-%d")    # 昨天日期
year = yesterday[2:4]
month =yesterday[5:7]
day = yesterday[8:10]



ip = "192.168.8.135"
port = 22
name ="liyuan3970"
password = "123456"
local_path = '/home/liyuan3970/test_demo/time/'
remote_path = '/home/liyuan3970/demo/'
filename ='a.txt'
remote_file_name='b.txt'

runtime2 ='16:10'



def job_upload():
    transport = paramiko.Transport((ip, port))    # 获取Transport实例
    transport.connect(username=name, password=password)    # 建立连接
    # 创建sftp对象，SFTPClient是定义怎么传输文件、怎么交互文件
    sftp = paramiko.SFTPClient.from_transport(transport)
    # 将本地 a.txt 上传至服务器 /www/test.py。文件上传并重命名为b.txt
    sftp.put(local_path+filename, remote_path+remote_file_name)
    # 关闭连接
    transport.close()

def job_download():
    '''处理时间函数'''
    print("Job4:每天06:00自动下载前一天20时向后预报一天的M4 10米风数据")
    os.system('java -jar GDSJavaClient.jar 10.135.29.64 8080 samba ECMWF_HR/10_METRE_WIND_GUST_IN_THE_LAST_3_HOURS'+' '+year+month+day+'20.000'+' '+year+month+day+'20.024'+' '+'diamond')
    time.sleep(20)
    print('job finshed------------------------------------------------------------------------')



if __name__ == '__main__':
    print("主程序")
    schedule.every().day.at(runtime).do(job_download)
    schedule.every().day.at(runtime2).do(job_upload)
    while True:
        schedule.run_pending()