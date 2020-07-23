import pymssql 
import pandas as pd
server = "172.21.158.201"    # 连接服务器地址
user = "down"# 连接帐号
password = "downx"# 连接密码

conn = pymssql.connect(server, user, password, "ZJSZDZDB")  #获取连接

cursor = conn.cursor() # 获取光标
cursor.execute('USE ZJSZDZDB' )
sql  = "select IIiii ,MAX(fFy*1000+dFy) AS Expr1 FROM Tab_Aws WHERE (IIiii IN('58665','58559','58568')) AND ((tTime BETWEEN '2020-7-14 2:00:01' AND '2020-7-14 05:00:00')OR(tTime BETWEEN '2020-7-13 2:00:01' AND '2020-7-13 05:00:00')) GROUP BY IIiii"




cursor.execute(sql) 
# select IIiii ,MAX(fFy*1000+dFy) AS Expr1 FROM Tab_Aws WHERE (IIiii IN('58665','58559','58568','58652')) AND (tTime BETWEEN '2020-7-14 2:00:01' AND '2020-7-14 05:00:00') GROUP BY IIiii
#sql2 = "GO"
#cursor.execute(sql2)
row = cursor.fetchall()
print(row)
print(pd.DataFrame(list(row)).shape)
#connect.commit()  # 提交
cursor.close()  # 关闭游标
conn.close()  # 关闭连接