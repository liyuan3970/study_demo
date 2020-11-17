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
def return_sql_map():
    print("this is a read station file")
    server = "172.21.158.201"    # 连接服务器地址
    user = "down"# 连接帐号
    password = "downx"# 连接密码
    conn = pymssql.connect(server, user, password, "ZJSZDZDB")  #获取连接
    cursor = conn.cursor() # 获取光标
    cursor.execute('USE ZJSZDZDB' )
    sql1 = "select IIiii,lat,lon from TAB_StationInfo where( \
          IIiii ='58559' or IIiii ='58568' or IIiii ='58652' \
          or IIiii ='58660' or IIiii ='58664' or IIiii ='58665' \
          or IIiii ='K8201' or IIiii ='K8301' or IIiii ='K8101' or IIiii='K8505'\
          )"
    cursor.execute(sql1)
    row1 = cursor.fetchall()
    data1 = pd.DataFrame(list(row1))

    sql2 = "select IIiii ,max(Tx)/10.0 FROM TAB_Aws WHERE \
          (IIiii ='58559' or IIiii ='58652' or IIiii ='58568' or IIiii = '58660'  \
          or IIiii ='58665' or IIiii = '58664' or IIiii ='58665')  \
          AND (tTime BETWEEN " + "'" + \
          str(first_day_of_last_month) + "'" + "AND" + "'" + str(last_day_of_last_month) + "'" + ") group BY IIiii"
    cursor.execute(sql2)
    row2 = cursor.fetchall()
    data2 = pd.DataFrame(list(row2))
    sql3 = "select IIiii ,max(Tx)/10.0 FROM Tab_MWS WHERE \
          (IIiii ='K8201' or IIiii ='K8302' or IIiii ='K8101' or IIiii ='K8505')  \
          AND (tTime BETWEEN " + "'" + \
          str(first_day_of_last_month) + "'" + "AND" + "'" + str(last_day_of_last_month) + "'" + ") group BY IIiii"
    cursor.execute(sql3)
    row3 = cursor.fetchall()
    data3 = pd.DataFrame(list(row3))


    clomns = ['IIiii', 'lat', 'lon','Tx']
    data = pd.DataFrame(np.random.randn(10,4),columns=clomns)
    data['IIiii'][0:6] = data2.iloc[0:6,0]
    data['IIiii'][6:] = data3.iloc[0:6, 0]
    data['Tx'][0:6] = data2.iloc[0:6,1]
    data['Tx'][6:] = data3.iloc[0:6, 1]
    data['lat'][:] = data1.iloc[:,1]
    data['lon'][:] = data1.iloc[:,2]

    result = []
    #print("0行",data.iloc[0,:].values)
    for i in range(10):
        #print("数据",i)
        clomns_data = data.iloc[i, :].values
        data_values = {'name':clomns_data[0],
                       'value':[clomns_data[2],clomns_data[1],clomns_data[3]]}
        result.append(data_values)
    #print(data1)
    #print(data)
    #print(result)
    return result

#return_sql_map()



