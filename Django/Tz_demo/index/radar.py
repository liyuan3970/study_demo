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
print(last_day_of_last_month)
end_day_in_mouth = today.replace(day=1)

#stations =['58559','58652','58568','58660','K8201','K8301','58665','58664','58665']
def return_sql_radar():
    print("this is a read station file")
    server = "172.21.158.201"    # 连接服务器地址
    user = "down"# 连接帐号
    password = "downx"# 连接密码
    conn = pymssql.connect(server, user, password, "ZJSZDZDB")  #获取连接
    cursor = conn.cursor() # 获取光标
    cursor.execute('USE ZJSZDZDB' )
    sql = "select tTime ,Ta/10.0,Tn/10.0,Tx/10.0,R20_20/10.0,S,fFy/10.0 FROM Tab_HistoryData WHERE \
          (IIiii ='58660')  \
          AND (tTime BETWEEN " + "'" + \
          str(first_day_of_last_month) + "'" + "AND" + "'" + str(last_day_of_last_month) +" "+"23:00:00"+ "'" + ")order BY tTime"
    cursor.execute(sql)
    row = cursor.fetchall()
    clomns = ['time', 'Ta', 'Tn', 'Tx','R20_20','S','Fy']
    data = pd.DataFrame(list(row),columns=clomns)
    sql2 = "SELECT IIiii, avg(Ta),avg(Tn),avg(Tx),avg(S),max(fFy)  FROM Tab_HistoryData Where IIiii In ('58665') " \
           "And (Year(tTime) Between '1981' And '2010') And ((Month(tTime)*100+Day(tTime)) Between 1101 And 1130) Group By IIiii"
    cursor.execute(sql2)
    row2 = cursor.fetchall()
    clomns2 = ['IIiii','Ta','Tn','Tx','S','Fy']
    data2 = pd.DataFrame(list(row2),columns=clomns2)
    sql3 = "SELECT IIiii, count(R20_20)/30.0 as Rn ,sum(R20_20)/30  FROM Tab_HistoryData Where R20_20>0  And IIiii In ('58665') " \
           "And (Year(tTime) Between '1981' And '2010') And ((Month(tTime)*100+Day(tTime)) Between 1101 And 1130) Group By IIiii"
    cursor.execute(sql3)
    row3 = cursor.fetchall()
    data3 = pd.DataFrame(list(row3))
    print("666")
    month = [data['Ta'].mean(),data['Tn'].mean(),data['Tx'].mean(),
             float(data[data["R20_20"]>0.0].sum()['R20_20']),float(data[data["R20_20"]>=0.1].count()['R20_20']),
             data['S'].mean(),float(data['Fy'].max())]
    history = [data2['Ta'].values[0]/10.0,data2['Tn'].values[0]/10.0,data2['Tx'].values[0]/10.0,
               float(data3.iloc[0,1]),data3.iloc[0,2]/10.0,
               data2['S'].values[0]/1.0,data2['Fy'].values[0]/10.0]
    result_radar = {
        'month':month,
        'history':history,
    }
    print(result_radar)
    return result_radar
return_sql_radar()