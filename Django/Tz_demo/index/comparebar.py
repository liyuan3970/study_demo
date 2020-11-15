import pymssql 
import pandas as pd
import time
import datetime
from datetime import  date, timedelta
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



today = datetime.date.today()
last_day_of_last_month = datetime.date(today.year, today.month, 1) - datetime.timedelta(1)
first_day_of_last_month = datetime.date(last_day_of_last_month.year, last_day_of_last_month.month, 1)
def read_sql_station(station):
    print("this is a read station file")
    server = "172.21.158.201"    # 连接服务器地址
    user = "down"# 连接帐号
    password = "downx"# 连接密码
    conn = pymssql.connect(server, user, password, "ZJSZDZDB")  #获取连接
    cursor = conn.cursor() # 获取光标
    cursor.execute('USE ZJSZDZDB' )
    if station.find('K')==0:
        #print("K_station")
        sql  = "select IIiii ,tTime,fFy,T,RR FROM Tab_MWS2020 WHERE (IIiii ='"+station+"') AND (tTime BETWEEN "+"'"+str(first_day_of_last_month)+"'"+ "AND"+"'"+str(last_day_of_last_month) +"'"+ ") order BY IIiii,tTime"
        #sql  = "select IIiii ,tTime,avg(fFy) FROM TAB_Aws2020 WHERE (IIiii ='"+station+"') AND (tTime BETWEEN "+"'"+str(first_day_of_last_month)+"'"+ "AND"+"'"+str(last_day_of_last_month) +"'"+ ") order BY IIiii,tTime"   
        cursor.execute(sql) 
        row = cursor.fetchall()
        data  = pd.DataFrame(list(row))    
        sql2 =  "select IIiii ,S FROM tab_historydata WHERE (IIiii ='"+station+"') AND (tTime BETWEEN "+"'"+str(first_day_of_last_month)+"'"+ "AND"+"'"+str(last_day_of_last_month) +"'"+ ") order BY IIiii,tTime"
        cursor.execute(sql2) 
        row2 = cursor.fetchall()
        data2  = pd.DataFrame(list(row2))
    else:
        #print("station")
        sql  = "select IIiii ,tTime,fFy,T,RR FROM TAB_Aws2020 WHERE (IIiii ='"+station+"') AND (tTime BETWEEN "+"'"+str(first_day_of_last_month)+"'"+ "AND"+"'"+str(last_day_of_last_month) +"'"+ ") order BY IIiii,tTime"
        #sql  = "select IIiii ,tTime,avg(fFy) FROM TAB_Aws2020 WHERE (IIiii ='"+station+"') AND (tTime BETWEEN "+"'"+str(first_day_of_last_month)+"'"+ "AND"+"'"+str(last_day_of_last_month) +"'"+ ") order BY IIiii,tTime"   
        cursor.execute(sql) 
        row = cursor.fetchall()
        data  = pd.DataFrame(list(row))    
        sql2 =  "select IIiii ,S FROM tab_historydata WHERE (IIiii ='"+station+"') AND (tTime BETWEEN "+"'"+str(first_day_of_last_month)+"'"+ "AND"+"'"+str(last_day_of_last_month) +"'"+ ") order BY IIiii,tTime"
        cursor.execute(sql2) 
        row2 = cursor.fetchall()
        data2  = pd.DataFrame(list(row2))
    #print(data.shape,data,data2)
    #返回计算结果
    averge = [data.iloc[:][2].mean(),data.iloc[:][3].mean(),data.iloc[:][4].mean(),data2.iloc[:][1].mean()]# 依次是风 温度 和降水1
    print(averge)    
    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接
    return averge

#stations =['58559','58652','58568','58660','K8201','K8301','58665','58664','58665']
def return_sql_station():
    print("this is a read station file")
    server = "172.21.158.201"    # 连接服务器地址
    user = "down"# 连接帐号
    password = "downx"# 连接密码
    conn = pymssql.connect(server, user, password, "ZJSZDZDB")  #获取连接
    cursor = conn.cursor() # 获取光标
    cursor.execute('USE ZJSZDZDB' )
    sql = "select IIiii ,max(fFy),avg(T),avg(RR) FROM TAB_Aws WHERE \
          (IIiii ='58559' or IIiii ='58652' or IIiii ='58568' or IIiii = '58660'  \
          or IIiii ='58665' or IIiii = '58664' or IIiii ='58665')  \
          AND (tTime BETWEEN " + "'" + \
          str(first_day_of_last_month) + "'" + "AND" + "'" + str(last_day_of_last_month) + "'" + ") group BY IIiii"
    cursor.execute(sql)
    row = cursor.fetchall()
    data = pd.DataFrame(list(row))
    sql2 = "select IIiii ,max(fFy),avg(T ),avg(RR) FROM Tab_MWS WHERE \
          (IIiii ='K8201' or IIiii ='K8302' or IIiii ='K8101' or IIiii ='K8505')  \
          AND (tTime BETWEEN " + "'" + \
          str(first_day_of_last_month) + "'" + "AND" + "'" + str(last_day_of_last_month) + "'" + ") group BY IIiii"
    cursor.execute(sql2)
    row2 = cursor.fetchall()
    data2 = pd.DataFrame(list(row2))

    sql3 = "select IIiii ,avg(S) FROM tab_historydata WHERE \
          (IIiii ='58559' or IIiii ='58652' or IIiii ='58568' or IIiii = '58660'  \
          or IIiii ='K8201' or IIiii = 'K8301' or IIiii = 'K8101' or IIiii ='58664' or\
           IIiii ='K8505'or IIiii = '58665')  \
          AND (tTime BETWEEN " + "'" + \
          str(first_day_of_last_month) + "'" + "AND" + "'" + str(last_day_of_last_month) + "'" + ") group BY IIiii"
    cursor.execute(sql3)
    row3 = cursor.fetchall()
    data3 = pd.DataFrame(list(row3))
    clomes = ['IIiii','wind','pre','tem','sun']
    print("data3",data3,
          "data2",data2,
          "data",data)

    wind =[
        data.iloc[0,1]/10,data.iloc[2,1]/10,data.iloc[1,1]/10,data2.iloc[0,1]/10,data2.iloc[1,1]/10,
        data2.iloc[2, 1]/10,data.iloc[5,1]/10,data.iloc[4,1]/10,data2.iloc[3,1]/10,data.iloc[3,1]/10
    ]

    pre =[
        data.iloc[0,3]/1.0,data.iloc[2,3]/1.0,data.iloc[1,3]/1.0,data2.iloc[0,3]/1.0,data2.iloc[1,3]/1.0,
        data2.iloc[2,3]/1.0,data.iloc[5,3]/1.0,data.iloc[4,3]/1.0,data2.iloc[3,3]/1.0,data.iloc[3,3]/1.0
    ]
    tem =[
        data.iloc[0,2]/10,data.iloc[2,2]/10,data.iloc[1,2]/10,data2.iloc[0,2]/10,data2.iloc[1,2]/10,
        data2.iloc[2,2]/10,data.iloc[5,2]/10,data.iloc[4,2]/10,data2.iloc[3,2]/10,data.iloc[3,2]/10
    ]

    sun =[
        data3.iloc[0,1]/1.0,data3.iloc[2,1]/1.0,data3.iloc[1,1]/1.0,data3.iloc[0,1]/1.0,data3.iloc[1,1]/1.0,
        data3.iloc[2,1]/1.0,data3.iloc[5,1]/1.0,data3.iloc[4,1]/1.0,data3.iloc[3,1]/1.0,data3.iloc[3,1]/1.0
    ]
    result = [wind,pre,tem,sun]
    print(result)
    return result
#return_sql_station()



