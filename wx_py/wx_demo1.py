from wxpy import *

import time,datetime

from threading import Thread 
bot=Bot(cache_path=True)


friend = bot.friends().search('liyuan')[0]
print(friend)

message = '这是message消息'
# 功能一 ：自动回复微信消息
@bot.register() # 接收从指定好友发来的消息，发送者即recv_msg.sender为指定好友girl_friend
def recv_send_msg(recv_msg):
    #业务逻辑代码
    # 附加功能：增加消息记录的功能
    print('收到的消息：',recv_msg.text) # recv_msg.text取得文本
    if recv_msg.text == '1':
        return '今夜玉环气温15度'
    elif recv_msg.text == '2':
        return '今夜玉环风速'
    #return '您好，这里是玉环气象局，现在微信播报天气服务信息...,查询气温请按1,播报天气请按2'


# 功能二 ：主动推送消息给一些人
def putmsg(friend,message):
    friend.send(message)

# 功能三 ：定时的自动向目标群(好友)推送消息
def run(h,m):
    while True:
        now  = datetime.datetime.now()
        print(now.hour,now.minute)
        if now.hour in h and now.minute in m:
            putmsg(friend,message)
        time.sleep(60)

# run函数为定时启动的函数
# run(23,m=[24])
# 开辟一个新的进程对新的
#p = Process(target = run,kwargs = {'h':22,'m':[50,51,52]})
p = Thread(target = run,kwargs = {'h':[23],'m':[8,9,10,11,12]})
p.start()
#p.join()
# 功能三：主动推送消息给一些人


# 阻塞等待微信机器人的消息

bot.join()