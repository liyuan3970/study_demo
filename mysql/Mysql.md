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
## 改数据
update 表名称 set 字段1=值1，字段2=值2 where 条件语句
```sql
update acct set status =2 where acct_no ='622345000001';
update acct set balance =2 where acct_no ='622345000003';
update acct set balance =2 where acct_no ='622345000003';
```
## 删除
delete from 表名称 where 条件表达式；
```sql
delete from acct where acct_no ='622345000002';
```
## 运算符操作
1. 比较操作符<,>,>=,<=,<>或!=
   ```sql
   select * from acct where balance <5000;
   select * from acct where status <10 and status>1;
   select * from acct where acct_no in('622345000002','622345000003');
   select * from acct where status between 2 and 100;
   ```
2. 范围查询
   ```sql
   select * from acct where status between 2 and 100;
   select * from acct where acct_no in('622345000002','622345000003');
   ```
## 模糊查询
```sql
select * from acct where acct_no like '6%'; -- 6%以6开头任意长度的字符串
select * from acct where acct_no like '6_'; -- 6_表示6后面跟一个任意字符
select * from acct where acct_no like '%6%'; -- 表示字符串里面有6的任意字符
select * from acct where acct_no like '%0005';-- 表示查询已0005结尾的任意字符
```
## 空和非空查询
空和非空的判断(NULL是一个特殊的值)
判断的时候用is null  或者 is not null
```sql
select * from acct where acct_no is null ;
select * from acct where acct_no ='';
```
## 排序
查询子句 排序 分组<br/> 
oeder by 字句<br/>
按照查询结果按照某个字段的值进行排序<br/>
order by 排序字段 [ASC/DESC]升降 默认是升序<br/>
按照账户余额进行升序排序<br/>
```sql
select * from acct  order by balance ASC;
select * from acct  order by balance DESC;
select * from acct  order by acct_tpye asc,balance desc;
```
## limit子句 是从0开始的
```sql
-- 限制显示查询结果的笔数
-- 格式limit n显示前面的n行
-- limit m,n 从m笔开始一直显示n笔，通常用于分页查询  m=(页数-1)*每页几笔  注：经常利用此句来分页  但是容易漏点数据？？？？
select * from acct  order by balance DESC limit 2;
select * from acct  limit 1;
select * from acct  limit 2,3;
```
## 聚合函数
```sql
select max(balance) from acct; -- 返回的是最大的值
select avg(balance) from acct; 
select sum(balance) from acct; 
select count(*) from acct;-- 避免字段名称，因为空值他不统计
-- group by 子句：对查询结果进行分组，通常和聚合函数连用，
-- 格式 group by 分组字段名称
select count(*), acct_tpye from acct  group by acct_tpye; -- 根据字段依据来分组
-- 统计每一类账户下面的余额平均值????

select count(*),acct_tpye "账户类型",max(balance) "最大余额" from acct group by acct_tpye;

-- 过滤子句having对分组聚合的结果进行筛选和group子句进行筛选
-- 格式 group by 分组字段 having 过滤条件
select count(*),acct_tpye "账户类型" ,sum(balance) from acct group by acct_tpye having acct_tpye is not null;
-- 
select count(*),acct_tpye "账户类型" ,sum(balance) from acct group by acct_tpye having acct_tpye is not null order by acct_tpye desc;

select count(*),acct_tpye "账户类型" ,sum(balance) from acct group by acct_tpye having acct_tpye is not null order by acct_tpye desc limit 2;

```
## 去重
```sql
-- distinct子句:select distinct (字段名称) from 表名称  对某个字段进行去重
-- 看账户表中有多少个账户类型
select distinct(acct_tpye) from acct; 
```
## 改表操作
```sql
-- 表结构调整--- 慎用

-- 添加字段 修改字段 删除字段

-- 添加字段，添加到最后一个字段
-- alter table 表名称 add 字段名称 类型（长度）
-- 添加到第一个字段
-- alter table 表名 add 字段名 类型(长度) first
-- 添加到特定字段后面
-- alter table 表名 add 字段名 类型(长度) after 字段

create table student(name varchar(32) , num varchar(32) )default charset =utf8;
alter table student add age int;
alter table student add id int first;
alter table student add tel_no varchar(32) after name;

-- 修改字段的类型
-- alter table 表名 modify 字段名 类型（长度）
-- 修改字段的名称
-- alter table 表名 change 旧字段名 新字段名 类型（宽度）


alter table student modify name varchar(128);
alter table student change name name_stu varchar(32);

```
## 删除字段
```sql
-- 删除表字段
alter table student drop id;
```
## SQL难点
**SQL语句执行的顺序的执行过程（难点）**
1. 执行from acct                      找打原数据
2. 执行where过滤                       过滤条件
3. 执行group by                       进行分组
4. sum(balance) acct_tpye             统计计算
5. havingacct_tpye is not null        把聚合后的数据进行过滤
6. order by acct_tpye desc            排序是为了limit
7. limit 1                            终于弄完啦



## 数据的约束条件
约束类型：<br>
1. 非空约束：字段值不能为空（账户金额）
2. 唯一约束：字段的值不能重复
3. 主键约束；制定字段作为主键，非空、唯一
4. 默认值：未填写值的情况下，自动填默认值
5. 自动增加：字段的值自动增加
6. 外键约束：在当前表，某个属性不是主键，在另一个表里是主键，参照外键时，外键对应的实体必须存在
```sql
-- 非空约束：制定字段的值不能为空，如果插入时没有设置值，并且没有默认值，插入时就会报错，
-- 语法：字段名称 字段类型 not null （创建的时候）
create table customer (cust_no varchar(32) not null ,cust_name varchar(32) not null , tel_no varchar(32) not null)
insert into customer(cust_no,cust_name) values('C0001','Jerry') -- 报错因为tel_no空值
 


-- 唯一约束
-- 字段不能重复，语法 字段名称 类型 unique
create table customer (cust_no varchar(32) unique ,cust_name varchar(32) unique , tel_no varchar(32) unique)
insert into customer(cust_no,cust_name) values
('C0001','Jerry','13512345678'),
('C0001','Jerry','13512345678') -- 报错因为违反了唯一性约束



-- 主键约束（重点primary key）
-- 唯一表示一笔记录，要求唯一、非空，PK和一笔记录有唯一对应关系
-- PK可以是一个属性构成，也可是好几个属性共同构成（证件号码和证件类型；客户编号，微信手机号和邮箱）
-- 语法 字段名称 字段类型 Primary Key
-- 主键约束 
create table customer(cust_no varchar(32) Primary key ,cust_name varchar(32) not null , tel_no varchar(32) not null)；
insert into customer(cust_no,cust_name) values
('','Jerry','13512345678')；-- 报错 因为主键不能为空，且唯一


-- 默认值
-- 当插入数据时，该字段如果没有添值，系统会字段添值
-- 语法 字段名称 类型 default 默认值
alter table customer add status int default 0 ;-- status 的默认值为0 


-- 自动增长
-- 当字段设置为自动增长时，插入数据不需要添值，数据库系统会自动在上一个值加1
-- 进场和PK配合使用
-- 语法 字段名 字段类型 auto_increment
create table ai_test(id int primary key auto_increment, name varchar(32) );
insert into ai_test values
(null,'aaa'), -- id=1
(null,'bbb'), -- id=2
(null,'ccc'); -- id=3


-- 外键约束(难点)
-- 外键；在当前表示不是主键，但是在另一个表时主键
-- 作用：保证参照的完整心、一致性
-- 使用外键的条件：
-- 表的存储引擎必须为InnoDB
-- 被参照字段在另外的表里面必须是主键
-- 当前表中的字段类型和被参照表中的类型要一致
-- 语法
constraint foreign key (当前表字段)
references 参照表名（参照字段名称）

create table account(acc_no varchar(32) primary key,cust_no varchar(32) not null constraint foreign key(cust_no) references customer(cust_no));

insert into account values
('0001','C0001'),-- 参照完整性正确可以插入
('0001','C0004');-- 外键的表里面没有，所以插不进去(参照表里面没有，参照不存在)

delete from customer where cust_no='C0001' ;-- 删不掉（想删除的话，先删除主账号，在删除主表）
-- 删除外键
alter table account drop foreign key 外键名
```

## **数据导入**
### 导出
**格式**<br>
select 查询语句  into outfile '文件路径'<br>
fields terminated by '字段分隔符'<br>
lines terminated by '行分割符'<br>
```sql
-- 实例
-- 第一步通过查看数据库允许导出的目录路径
show variables like 'secure_file%'
-- 第二部执行导出，文件必须导出到第一步的目录下
select * from source 
into outfile 'C:\ProgramData\MySQL\MySQL Server 5.7\Uploads\test.txt' 
fields terminated by ','
lines terminated by '\n';

-- test succeed
select * from orders 
into outfile 'D:test.txt' 
fields terminated by ','
lines terminated by '\n';

-- test 2 succeed
select * from orders 
into outfile 'E:python/MySQL/data/test.txt' 
fields terminated by ','
lines terminated by '\n';






select * from acct
into outfile '\var\lib\mysql-files\acct.bak'
fields terminated by ','
lines terminated by '\n';

-- 第三部 查看导出文件
sudo cat /var/lib/mysql-files/acct.bak



```
### 导入
**格式**<br>

load data infile '备份文件路经'<br>
into table 表名称<br>
fields terminated by ','  -- 字段分割符<br>
lines terminated by '\n'; -- 行分割符<br>

```sql
load data infile '\var\lib\mysql-files\acct.bak'
into table acct
fields terminated by ',' 
lines terminated by '\n';

```
**方法二**<br>
**进入到mysql，source xxx.sql**


## 子查询
```sql
select * from acct where acct_no in(select distinct acct_no from acct_trans_detail)
```
说明：先执行子查询在执行外层查询，条件要相互匹配，子查询结果先放到临时表里面的。
## 连接查询

### 内连接－注意笛卡尔积
```sql
select * from acct.acct_no acct.acct_name 
customer.cust_tel customer.cust_name  
from acct,customer
where acct.cust_no = customer.cust_no --关联条件 不会产生笛卡尔积  默认内连接
```
### 外链接
```sql
select 字段列表 from  表A inner join 表B on 关联条件


select a.acct_no ,a.acct_name c.cust_tel from acct a inner join customer c on a.acct_no=c.cust_no

外链接的方式：左连接右连接匹配到就匹配，匹配不到就显示空
```



