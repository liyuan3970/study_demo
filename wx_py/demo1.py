

import tkinter as tk

from tkinter import ttk


'''

这是一个微信的客户段

满足微信客户端的基本功能


'''





##########################　　　　　　　　用户数据　　　　　　###########################

###################################################################################
#global friends,groups,friend_list

groups = ['name1','name1','name1','name1','name1','name1','name1','name1','name1','name1']

friends = ['friend1','friend1','friend1','friend1',
'friend1','friend1','friend1','friend1','friend1',
'friend1','friend1','friend1','friend1','friend1',
'friend1','friend1','friend1','friend1','friend1',
'friend1','friend1','friend1','friend1','friend1',
'friend1','friend1','friend1','friend1','friend1',
'friend1','friend1','friend1','friend1','friend1',
'friend1']
##################################################################################

'''定义按键函数'''
# def fun_name_list(friends,friend_list):
#     friends = friends
#     print("111111111111")
#     friend_list = friend_list
#     for item in friends:
#         friend_list.insert("end", item)
#     friend_list.place(x=10,y=140,width=255,height =450 )
#
# def fun_name_group(groups,friend_list):
#     groups = groups
#     print("222222222222")
#     friend_list = friend_list
#     for item in groups:
#         friend_list.insert("end", item)
#     friend_list.place(x=10,y=140,width=255,height =450 )



###################################################################################

chat = tk.Tk()             #初始化Tk()
chat.title("Electronic WeChat")#
chat.geometry('800x600')                 #窗口大小*



chat.resizable(width=False, height=False) #宽不可变, 高可变,默认为True
chat['bg'] = 'black'


#########################################################################################
# 好友列
frame1 = tk.Frame(chat).place(x=0,y=0,width=279,height =600 )

v = tk.StringVar(frame1)
v.set('Python')
name_menu = ttk.OptionMenu(frame1,v,'Python','Php','C','Java','Cart').place(x=230,y=15,width=30,height =30)

name_pic = tk.Button(frame1,text = 'name',bg='white').place(x=10,y=10,width=40,height =40 )

name_label = tk.Label(frame1,text='liyuan').place(x=50,y=20)

search = tk.Entry(frame1).place(x=10,y=52,width=255,height =30)

name_pic = tk.Button(frame1,text = 'name',bg='white').place(x=10,y=10,width=40,height =40 )



name_artical = tk.Button(frame1,text = 'artical',bg='white').place(x=120,y=90,width=40,height =40 )



friend_list = tk.Listbox(frame1)#.place(x=10,y=140,width=255,height =450 )


def fun_name_list():
    #friends = friends
    print("111111111111")
    friend_list.delete(0,'end')
    l=[]
    l=friends
    #friend_list = friend_list
    for item in l:
        friend_list.insert("end", item)
    friend_list.place(x=10,y=140,width=255,height =450 )

def fun_name_group():
    #groups = groups
    friend_list.delete(0,'end')
    print("222222222222")
    l=[]
    l=groups
    #friend_list = friend_list
    for item in l:
        friend_list.insert("end", item)
    friend_list.place(x=10,y=140,width=255,height =450 )




name_list = tk.Button(frame1,text = 'list',bg='white',command = fun_name_group).place(x=30,y=90,width=40,height =40 )

name_all = tk.Button(frame1,text = 'all',bg='white',command = fun_name_list)

name_all.place(x=210,y=90,width=40,height =40 )
#for item in friends:
#    friend_list.insert("end", item)
#friend_list.place(x=10,y=140,width=255,height =450 )
#########################################################################################


#########################################################################################
# 消息列
frame2 = tk.Frame(chat).place(x=280,y=0,width=520,height =419 )

## 显示名称
name = tk.Label(frame2,text='name').place(x=510,y=12)

text_recv = tk.Text(frame2).place(x=285,y=40,width=500,height =370 )
#########################################################################################


#########################################################################################
# 消息列
frame3 = tk.Frame(chat).place(x=280,y=420,width=520,height =180 )

emoji = tk.Button(frame3).place(x=285,y=425,width=30,height =30 )
file = tk.Button(frame3).place(x=320,y=425,width=30,height =30 )

text_send = tk.Text(frame3).place(x=285,y=465,width=500,height =100 )
send = tk.Button(frame3,text = 'send',bg='white').place(x=685,y=565,width=100,height =30 )

##########################################################################################

chat.mainloop() 