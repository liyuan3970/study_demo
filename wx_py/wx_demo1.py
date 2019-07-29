from wxpy import *
bot=Bot(cache_path=True)


@bot.register() # 接收从指定好友发来的消息，发送者即recv_msg.sender为指定好友girl_friend
def recv_send_msg(recv_msg):
    #业务逻辑代码
    print('收到的消息：',recv_msg.text) # recv_msg.text取得文本
    if recv_msg.text == '1':
        return '今夜玉环气温15度'
    elif recv_msg.text == '2':
        return '今夜玉环风速'
    return '您好，这里是玉环气象局，现在微信播报天气服务信息'

#embed()

bot.join()