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
def return_sql_bar():
    print("this is a read station file")
    server = "172.21.158.201"    # 连接服务器地址
    user = "down"# 连接帐号
    password = "downx"# 连接密码
    conn = pymssql.connect(server, user, password, "ZJSZDZDB")  #获取连接
    cursor = conn.cursor() # 获取光标
    cursor.execute('USE ZJSZDZDB' )
    sql = "select tTime ,fFy/10.0,T/10.0,RR/10.0 FROM TAB_Aws WHERE \
          (IIiii ='58660')  \
          AND (tTime BETWEEN " + "'" + \
          str(first_day_of_last_month) + "'" + "AND" + "'" + str(last_day_of_last_month) +" "+"23:00:00"+ "'" + ") order BY tTime"
    cursor.execute(sql)
    row = cursor.fetchall()
    clomns = ['time', 'wind', 'tem', 'RR']
    data = pd.DataFrame(list(row),columns=clomns)
    print(data)
    #print(data['time'].dt.date)
    data['time'] = data['time'].dt.date

    data = data.set_index('time')

    #print("gp:",data['2020-10-01'].mean())
    #print(data)
    day = data.groupby('time')['wind'].max().index.values
    wind = (data.groupby('time')['wind'].max()).tolist()
    tem = (data.groupby('time')['tem'].sum()/24).tolist()
    RR = (data.groupby('time')['RR'].sum()).tolist()
    result = [day,wind,tem,RR]
    return result
#return_sql_bar()



