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
    # 统计大风站
    sql = "select tTime ,max(fFy)/10.0 FROM Tab_HistoryData WHERE \
          (IIiii in (select IIiii from TAB_StationInfo where (City = '台州')))  \
          AND (tTime BETWEEN " + "'" + \
          str(first_day_of_last_month) + "'" + "AND" + "'" + str(last_day_of_last_month) +" "+"23:00:00"+ "'" + ") and (fFy>=172) group by tTime"
    cursor.execute(sql)
    row = cursor.fetchall()
    # clomns = ['time', 'wind', 'tem', 'RR']
    data = pd.DataFrame(list(row))
    sql2 ="select tTime,max(R20_20) FROM Tab_HistoryData WHERE \
          (IIiii in (select IIiii from TAB_StationInfo where (City = '台州')))  \
          AND (tTime BETWEEN " + "'" + \
          str(first_day_of_last_month) + "'" + "AND" + "'" + str(last_day_of_last_month) +" "+"23:00:00"+ "'" + ")  and (R20_20>=10) group by tTime order by tTime"
    cursor.execute(sql2)
    row2 = cursor.fetchall()
    # clomns = ['time', 'wind', 'tem', 'RR']
    data2 = pd.DataFrame(list(row2))
    print(data2)

return_sql_bar()





