import pymssql 

server = "localhost"    # 连接服务器地址
user = "SA"# 连接帐号
password = "Liyuan3970"# 连接密码

conn = pymssql.connect(server, user, password, "TestDB")  #获取连接

cursor = conn.cursor() # 获取光标
cursor.execute('USE TestDB' )