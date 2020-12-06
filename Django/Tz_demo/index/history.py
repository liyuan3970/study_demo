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
    # 计算历史降水排位
    sql = "SELECT Year(tTime) as ye, Sum(R20_20) as Rsum  FROM Tab_HistoryData Where R20_20>-1 And IIiii In ('58665') " \
          "And ((Month(tTime)*100+Day(tTime)) Between 1101 And 1130)  GROUP BY YEAR(tTime) ORDER BY  Rsum desc"
    cursor.execute(sql)
    row = cursor.fetchall()
    data = pd.DataFrame(list(row))
    # 计算历史最低气温
    sql2 = "SELECT Year(tTime) as ye, min(Tn) as Rsum  FROM Tab_HistoryData Where R20_20>-1 And IIiii In ('58665') " \
          "And ((Month(tTime)*100+Day(tTime)) Between 1101 And 1130)  GROUP BY YEAR(tTime) ORDER BY  Rsum desc"
    cursor.execute(sql2)
    row2 = cursor.fetchall()
    data2 = pd.DataFrame(list(row2))
    # 计算历史最高气温
    sql3 = "SELECT Year(tTime) as ye, max(Tx) as Rsum  FROM Tab_HistoryData Where R20_20>-1 And IIiii In ('58665') " \
          "And ((Month(tTime)*100+Day(tTime)) Between 1101 And 1130)  GROUP BY YEAR(tTime) ORDER BY  Rsum desc"
    cursor.execute(sql3)
    row3 = cursor.fetchall()
    data3 = pd.DataFrame(list(row3))
    tem_min = data3.iloc[0:6,:]
    print(tem_min)

return_sql_bar()