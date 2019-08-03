'''导入相关库'''
import tkinter  #界面库
from wxpy import *  #微信库
 
def loginWeChat():
    '''Function:登录微信'''
    global bot
    bot = Bot() #初始化微信,会显示登录二维码界面
 
def logoutWeChat():
    '''Function:登出微信'''
    bot.logout()
    chatform.destroy()#关闭窗口
 
def addFriendListToTable():
    '''Function:添加好友到好友列表框当中'''
    bot.friends(update=False) #更新好友列表
    friend_list = bot.friends(False).search() #得到好友列表 type:<class 'wxpy.api.chats.chats.Chats'>
    for i in range(2): #显示前10位经常联系的好友
        user_detail_info = bot.user_details(friend_list[i], 50) #获得好友信息
        friend_info = str(user_detail_info)
        listbox_friends.insert(i,friend_info)
    @bot.register(Friend, TEXT)
    def showMessageInfo(msg):
        listbox_ReceiveMsg.insert(tkinter.END, str(msg))
        if listbox_ReceiveMsg.size() >= 10:
            listbox_ReceiveMsg.delete(0,tkinter.END)
 
def sendMessageToFriend():
    '''Function:发送消息给好友'''
    select_friendname = txt_Sender.get(0.0,tkinter.END)
    check_friend = bot.friends().search(select_friendname)[0]
    send_msg = txt_SendMsg.get(0.0,tkinter.END)
    check_friend.send(send_msg)
    sent_msgs = bot.messages.search(sender=bot.self) #获得自己发送的消息
    current_sent_msgs = str(sent_msgs[len(sent_msgs)-1])
    listbox_ReceiveMsg.insert(tkinter.END,current_sent_msgs)
    txt_SendMsg.delete(0.0,tkinter.END) #发送完信息后清空
    if listbox_ReceiveMsg.size() >= 10: #清空listBox
        listbox_ReceiveMsg.delete(0, tkinter.END)
 
def autoReplyInfo():
    '''Function:自动回复信息功能'''
    @bot.register(Friend,PICTURE)
    def replyInfoFormal(msg):
        return "I am busy!"
 
'''初始化界面及相关参数'''
chatform = tkinter.Tk()
chatform.geometry("500x700") #设置窗体大小 width x height
chatform.resizable(width=False,height=False) #设置大小不可变
chatform.title("YTouch微信聊天") #标题
 
'''添加相关控件'''
#登录微信按钮
btn_login = tkinter.Button(text='登录微信',command=loginWeChat)
btn_login['fg'] = 'red' #字体颜色
btn_login['bg'] = 'blue' #背景色
btn_login.place(x = 220,y = 600,width = 60,height = 30) #x:距离左半边的距离,y:距离上面的距离
 
#退出微信按钮
btn_logout = tkinter.Button(text='退出微信',command=logoutWeChat)
btn_logout['fg'] = 'red' #字体颜色
btn_logout['bg'] = 'blue' #背景色
btn_logout.place(x = 300,y = 600,width = 60,height = 30) #x:距离左半边的距离,y:距离上面的距离
 
#更新好友列表按钮
btn_FriendList = tkinter.Button(text='更新好友',command=addFriendListToTable)
btn_FriendList['fg'] = 'red' #字体颜色
btn_FriendList['bg'] = 'blue' #背景色
btn_FriendList.place(x =0 ,y = 0,width = 60,height = 30) #x:距离左半边的距离,y:距离上面的距离
 
#发送消息按钮
btn_SendMsg = tkinter.Button(text='发送消息',command=sendMessageToFriend)
btn_SendMsg['fg'] = 'red' #字体颜色
btn_SendMsg['bg'] = 'blue' #背景色
btn_SendMsg.place(x =400 ,y = 600,width = 60,height = 30) #x:距离左半边的距离,y:距离上面的距离
 
#自动回复按钮
btn_ReplyAuto = tkinter.Button(text='自动回复',command=autoReplyInfo)
btn_ReplyAuto['fg'] = 'red' #字体颜色
btn_ReplyAuto['bg'] = 'blue' #背景色
btn_ReplyAuto.place(x = 120,y = 600,width = 60,height = 30) #x:距离左半边的距离,
 
#输入消息文本框
txt_SendMsg = tkinter.Text(chatform,height = 1) #height表示几行
txt_SendMsg.place(x =200 ,y = 500,width = 260)
 
#选择指定好友文本框
txt_Sender = tkinter.Text(chatform,height = 1) #height表示几行
txt_Sender.place(x =0 ,y = 500,width = 150)
 
#消息对话框
listbox_ReceiveMsg = tkinter.Listbox(chatform) #height表示几行
listbox_ReceiveMsg.place(x =240,y = 50,width =200,height = 300)
 
#好友列表框
listbox_friends = tkinter.Listbox(chatform,height = 300)
listbox_friends.place(x = 20,y = 50,width = 200,height = 300)
 
chatform.mainloop() #保持登录状态
 