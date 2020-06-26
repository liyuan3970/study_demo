import os
from ftplib import FTP

def ftp_connect(host, username, password):
    ftp = FTP()
    # ftp.set_debuglevel(2)
    ftp.connect(host, 21)
    ftp.login(username, password)
    return ftp

"""
从ftp服务器下载文件
"""
def download_file(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

"""
从本地上传文件到ftp
"""
def upload_file(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')

    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()


if __name__ == "__main__":
    ftp = ftp_connect("192.168.8.200", "XXXX", "123456")
    download_file(ftp, r"IMG_0682.jpg", r"C:\Users\lenovo\Desktop\最新接口\img.jpg")
    #调用本地播放器播放下载的视频
    os.system('start "C:\Program Files\Windows Media Player\wmplayer.exe" "C:/Users/Administrator/Desktop/test.mp4"')
    upload_file(ftp, r"IMG_0682.jpg", "E:\我们的照片\新建文件夹\IMG_0682.jpg")

    ftp.quit()