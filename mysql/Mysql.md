# Mysql

## 创建acct(账户)
```sql
create database bank default charset=utf8;
use bank;
create table acct(acct_no varchar(32),acct_name varchar(128))default charset=utf8;
show tables;-- 看表
desc acct; -- 查看表的结构
show create table acct;-- 查看创建表的语句
drop table acct;-- 删除表
create table acct(acct_no varchar(32),acct_name varchar(128),cusr_no varchar(32),-- 用户编号
acct_tpye int,-- 账户类型
reg_date date,-- 开户日期
status int,-- 账户状态
balance decimal(16,2)-- 浮点数最长16位，2位小数
)default charset=utf8; 
insert into acct values('622345000001','Jerry','C0001',1,now(),2,1000.00); -- 插入数据 
select * from acct;-- 查看数据
-- 方法二（插入多个数据）
insert into acct values('622345000001','Jerry','C0001',1,now(),2,1000.00),
('622345000002','Jerry','C0001',1,now(),2,1000.00),
('622345000003','Jerry','C0001',1,now(),2,1000.00),
('622345000004','Jerry','C0001',1,now(),2,1000.00);

-- 方法三指定字段插入
insert into acct(acct_no,acct_name)
values('622345000005','Jerry');
```
## 查询数据
```sql
-- 查询所有数据
select * from acct;

-- 查询制定部分字段
select acct_no, acct_name,balance from acct;

-- 查询指定的字段，为字段制定别名
-- 1
select acct_no "账号",
       acct_name "姓名",
       balance "余额"
from acct;
-- 2
select acct_no as "账号" from acct;

-- 查询时使用字段的值进行计算查询账号余额，一万元为单位显示
select acct_no "账号",
       acct_name "姓名",
       balance/10000 "余额(万元)"
from acct;
```
## 待条件的查询
```sql
-- 带条件的查询 寻找账号为623333。。。02的账户（1个条件）
select * from acct
where acct_no = '622345000002';


-- 带多个条件的查询
select * from acct
where acct_no = '622345000002' and acct_name = ''; -- 且

select * from acct
where acct_no = '622345000002' or acct_name = ''; -- 或
```

## 数据类型
1. 数值类型：整数，浮点型，字符类型，日期时间（now()）,枚举类型（至相对较少，限定范围，性别，账户状态）
2. tinyint(1) smallint(2) int(4) bigint(8)    数值类型
3. decimal(可变，精确数字可指定小数的位数) decimal(16,2)  浮点类型
4. char(定长字符串255个字符，如果长度不足，用空格填充，超过规定长度，则无法存入)性能好于varchar
5. varchar(可变长字符串，65535个字符，按照实际大小分配存储空间，字符串超过最大长度，则无法写入)
6. text 大文本字符类型 数据大于65535时使用
7. char和varchar对比
   ```sql
        create table tmp(acct_no char(10),acct_name varchar(32));
        insert into tmp values('01111','liyuan')
    ```
8. 枚举类型 enum(多个值选一个) set(给定范围选一个或者多个)
   ```sql
   create table enum_test(name varchar(32),sex enum('boy','girl'),course set('music','dance','paint'));
    insert into enum_test
   values('Jerry','girl','music,dance');--
   ```
