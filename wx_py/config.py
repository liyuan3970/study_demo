# 发送文本
#my_friend.send('Hello, WeChat!')
# 发送图片
#my_friend.send_image('my_picture.png')
# 发送视频
#my_friend.send_video('my_video.mov')
# 发送文件
#my_friend.send_file('my_file.zip')
# 以动态的方式发送图片
import datetime
import time
from multiprocessing import Process

def dosometing():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print('我在干活')

def main(h,m):
    while True:
        now  = datetime.datetime.now()
        print(now.hour,now.minute)
        if now.hour == h and now.minute in m:
            dosometing()
        time.sleep(60)


#main(23,m=[24])

friend = 5
message = '6'
# 功能二 ：定时的自动向目标群(好友)推送消息
def putmsg(friend,message):
    print('friend.send(message)')

def run(h,m):
    while True:
        now  = datetime.datetime.now()
        print(now.hour,now.minute)
        if now.hour == h and now.minute in m:
            putmsg(friend,message)
        time.sleep(60)

# run函数为定时启动的函数
# run(23,m=[24])
# 开辟一个新的进程对新的
p = Process(target = run,kwargs = {'h':23,'m':[38]})
p.start()
p.join()