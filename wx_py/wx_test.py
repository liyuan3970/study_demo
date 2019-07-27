'''
微信软件开发

需求分析：
1.能够自动回复天气预报信息
2.能够定时推送微信信息
3.待定

技术实现分析：
1.用正则表达式世识别用户的消息，判断是否符合发送短信的条件，若符合则推送今天的天气预报

2.用time模块定义发送天气预报的时间，并利用wxpy推送消息

'''

#msg = '您好我是李渊的微信机器人'


# 返回所有好友的列表
# a.bot.friends()

# 向所有好友发送消息
# a.send('str')

#自动响应各类请求
######################################################

# 打印来自其他好友、群聊和公众号的消息
#@bot.register()
#def print_others(msg):
#    print(msg)



# 自动接受新的好友请求
#@bot.register(msg_types=FRIENDS)
#def auto_accept_friends(msg):
#    # 接受好友请求
#    new_friend = msg.card.accept()
#    # 向新的好友发送消息
#    new_friend.send('哈哈，我自动接受了你的好友请求')


##############################################################
from wxpy import *
bot=Bot(cache_path=True)


@bot.register() # 接收从指定好友发来的消息，发送者即recv_msg.sender为指定好友girl_friend
def recv_send_msg(recv_msg):
    print('收到的消息：',recv_msg.text) # recv_msg.text取得文本
    return '今夜台州气温15度'

#embed()

bot.join()


