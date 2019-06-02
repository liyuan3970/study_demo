# Mongodb
## 关系型数据库
1. 关系数据库
  - 关系数据库：使用二维表表示数据，数据联系
  - 数据管理三个阶段：手工管理，文件管理，数据库管理
  - 数据库：存放数据，提供快速的增删改查操作
            备份、恢复功能
	    管理系统工具
	    编程语言接口 
  - 重要概念：
     数据：表达信息的载体
     数据结构：数据组织的方式，数据之间关系
     数据库：数据库科学、有效存放、管理的仓库
     DBMS：数据库管理系统，一套数据库管理的软件

     表：由行、列组成，用来表示一定意义的数据
     字段：表的一列，表示实体的一个属性
     键：可以区分实体的属性（属性组合）
     主键：从键中选一个作为主键
     索引：提高查询效率的技术
           通过避免全表扫描提高查询效率

  - 关系型数据库的缺点
     性能：高并发、大数据量情况下
           性能容易成为瓶颈
	   
	   为了维护数据一致性，需要在写数据时候
	   对数枷锁

	   联合查询容易导致性能下降
     扩展性：无法通过横向扩展来扩展性能、负载能力
     处理非结构化数据不方便
2. 非关系型数据库
   1. 优点：
	- 高并发、读写能力强
	- 易扩展
	- 弱化了数据结构，降低数据一致性要求
   2. 缺点：
	- 技术成熟度不如关系型数据库
	- 通用性比较差，不想SQL语言有统一标准
	- 操作冗长，容易混乱
	- 有些不支持jion/事务，一致性不如关系型

   3. 使用非关系型数据库的情况
       - 对数据一致性要求较低
       - 数据库需要处理海量并发
       - 需要快速处理数据
       - 方便构建非关系模型
   
   4. 分类
      - 键值对：key-value, 例如redis
      - 文档型：MongoDB
      - 列存储型：HBase
      - 图形数据库
3. MongoDB的特点
   - 开发语言：C++
   - 支持丰富增删改查，最像关系数据库的非关系数据库
   - 技术相对成熟，支持丰富的存储类型
   - 支持众多的编程语言接口
   - 使用方便，便于扩展、部署
4. 基本操作
   1. mongod --dbpath 目录<br>
     功能：设置Mongodb数据存储路径<br>
     e.g. mongod --dbpath /home/tarena/mongo/

   2. mongod --port 端口号<br>
     功能：修改服务监听的端口，默认27017

   3. 启动mongo操作界面(Mongo Shell)<br>
	mongo   (登录到本机)<br>
	mongo 127.0.0.1:27017
	      连接到127.0.0.1:27017服务器<br>
	mongo 192.168.1.10/test -u xxx -p xxxx<br>
	      使用指定的用户名密码登录远程数据库
	      test表示库名称
5. Mongo数据结构<br>
	键值对 --> 文档 --> 集合 --> 数据库

   关系数据库概念|MongoDB概念
   --|--
   数据库 | 数据库
   表|集合(collection)
   行|文档（document,一笔数据）
   列|域(field)
   索引|索引
   主键|主键
6. 库操作
   1. 创建库：use databaseName<br>
     说明：表示进入某个库，当库不存在时自动创建
           在实际写入数据时创，而不是马上创建<br>
     e.g. use test
       创建test库

   2. 查看库：show dbs<br>
     系统中会有几个自动创建的库<br>
     admin:该库中的成员拥有最高权限<br>
     local:存储跟本地服务器相关的数据
           这部分数据不会被复制到其它服务器

   3. 查看当前所在库：db

   4. 删除库：db.dropDatabase()
       * 删除之前首先进入要删除的库
   5. 库的命名规则
     - 使用utf-8字符
     - 不能有空格，点，/, \, '\0'(空字符)
     - 长度不能超过64字节
     - 不能和系统数据库重名

   6. 备份和恢复
     - 备份：mongodump -h 主机 -d 库名 -o 目录<br>
       e.g. mongodump -h localhost -d test -o /tmp/
     
     - 恢复:mongorestore -h 主机:端口 -d 库名 路径<br>
       e.g. mongorestore -h localhost:27017 -d test /tmp/test
  
   7. 数据库监控: 
     - mongostat<br>
     insert query update delete：每秒执行增删改查次数 <br>
     command ：每秒中运行的命令次数<br>
     flushes ：每秒中清理缓存次数<br>
     vsize  ：虚拟内存的使用量<br>
     res：物理内存使用量

     - mongotop: 监测每个数据库读写时长
       ns: 数据集合
       total:总时长
       read:读时长
       write：写时长
7. 集合操作
   1. 集合：相当于关系数据库中的表
           包含很多文档
	   集合没有特定的结构
	   当有数据插入时自动创建

   2. 集合的使用
     - 同一类数据放入一个集合
     - 尽量保持每条数据结构的一致性

   3. 集合操作命令
     - 创建：
         格式：db.createCollection(集合名称)<br>
	 e.g.  db.createCollection("acct")
	       创建acct集合

     - 插入文档，自动创建，执行下列语句，自动
       创建acct集合<br>
	db.acct.insert({
	    acct_no:"622345000001",
	    acct_name:"Jerry",
	    balance:5000.00
	})

	集合命名注意事项：
	 1. 集合名称不能为空字符串
	 2. 不能含有'\0'字符串
	 3. 不能以system.开头，这是系统保留前缀
	 4. 不能含有保留字，不能包含$符号

     - 删除集合：db.collectionName.drop()<br>
        e.g.  db.acct.drop()  
	      删除acct集合

     - 重命名集合：
       db.collectionName.renameCollection(新名字)<br>
       e.g. db.student.renameCollection("stu")
           将student重命名为stu
8. 文档操作
   1. 文档：文档是构成集合的基本单元
           相当于关系数据库的行（记录）
	   由一系列键值对组成

        例如：
	{
	    acct_no:"622345000001",
	    acct_name:"Jerry",
	    balance:5000.00
	}
	
       文档的特点
       - 文档中的键值对是有序的
       - 文档中的键不能重复
       - MongDB区分大小写
       - 键需要使用utf-8字符

      文档存储：存储为BSON(Binary JSON)

   2. 插入<br>
	 插入文档操作<br>
	db.acct.insert({
	    acct_no:"622345000002",
	    acct_name:"Tom",
	    acct_type:1,
	    balance:12345.67
	})

	    同时插入两笔<br>
	db.acct.insert([
	    {
		acct_no:"622345000003",
		acct_name:"Dekie",
		acct_type:1,
		balance:888.99
	    },
	    {
		acct_no:"622345000004",
		acct_name:"Daniel",
		acct_type:1,
		balance:5000.00
	    }
	])

	  save实现插入,如果_id域有匹配的文档
	  则修改，没有匹配到则插入<br>
	db.acct.save({
	    "_id" : ObjectId("5c10cf9a6586b97dd12e0d8f"),
	    acct_no:"62234500005",
	    acct_name:"Emma",
	    acct_type:2,
	    balance:7777.77
	})

	  ObjectId:系统为每一个文档生成主键
	         长度24字符
		 8位：文档创建时间
		 6位：机器id
		 4位：进程id
		 6位：流水号

     3. MongoDB数据类型<br>
   
        类型|序号|类型
        --|--|--
        Double|		1	|浮点型
        String|		2	|字符串(utf-8)
        Object|		3	|内嵌文档
        Array|		4	|数组
        Binary Data|	5	|二进制(图片，视频)
        ObjectId|	7	|系统生成的ObjectId
        Boolean|		8	|布尔(true,false)
        Date|		9	|日期时间
        NULL|		10	|空值
        Integer|		16/18	|整型(32b/64b整型)
        Timestamp|	17	|时间戳


# Day02
**db.collection.find(query,field)**<br>
query: 是一个键值对构成的文档，表达查找条件<br>
field：是一个键值对构成文档，通过描述某个域的值是1或者0表达是否查找。1表示查找该域0表示不查找。
findOne(query,field)<br>
功能： 查找第一条符合条件的文档<br>
参数： 同find<br>
## query 的使用
**比较操作符**

    $eq  等于 = 

    e.g.  年龄等于18
          db.class0.find({age:{$eq:18}},{_id:0})

    $lt  小于 < 

    e.g.  年龄小于Jack （字符串可以比较大小）
    db.class0.find({name:{$lt:'Jack'}},{_id:0})

    $gt  大于 >
	
    e.g.  大于16小于19的 （表达区间关系）
    db.class0.find({age:{$gt:16,$lt:19}},{_id:0})

    $lte  小于等于  <=
    $gte  大于等于  >=
    $ne   不等于    !=

    $in  包含

    e.g. 查找年龄在数组范围内的文档
    db.class0.find({age:{$in:[18,19,20]}},{_id:0})

    $nin  不包含

    e.g. 查找年龄不包含在数组中的
    db.class0.find({age:{$nin:[18,19,20]}},{_id:0})

**逻辑操作符**
    表示逻辑与
        1. 在query文档中逗号隔开的多个键值对即表示与关系

	e.g. 年龄18 并且 性别为女
	     db.class0.find({age:18,sex:'w'},{_id:0})

        2. $and 表示逻辑与

	e.g. 年龄大于17 并且性别为女
	     db.class0.find({$and:[{age:{$gt:17}},{sex:'w'}]},{_id:0})
    
    逻辑或  $or

        e.g. 年龄小于18或者性别为女
	db.class0.find({$or:[{age:{$lt:18}},{sex:'w'}]},{_id:0})
    
    逻辑非  $not
    
        e.g.  年龄不大于17
	db.class0.find({age:{$not:{$gt:17}}},{_id:0})

    逻辑既不也不  $nor	   --> not (A or B)

        e.g.  年龄既不小于17，性别也不为女
	db.class0.find({$nor:[{age:{$lt:17}},{sex:'w'}]},{_id:0})


    条件混合
        年龄（大于18 或者小于17）并且性别为男的
	
	db.class0.find({$or:[{age:{$gt:18}},{age:{$lt:17}}],sex:'m'},{_id:0})


	年龄大于等于17的男生，或者 姓名叫Lily

	db.class0.find({$or:[{age:{$gte:17},sex:'m'},{name:'Lily'}]},{_id:0})
**数组类型查找**
    数组： 一组数据的有序集合，用[]表示
          * 有序性
	  * 数组中的元素可以是不同的数据类型

    查找数组中包含某一项
	
	e.g.  查找数组中包含大于90的文档
	db.class2.find({score:{$gt:90}},{_id:0})

    查找数组中同时包含多项的  $all
        
	e.g.  查找数组中同时包含83 88 的
	db.class2.find({score:{$all:[83,88]}},{_id:0})

    根据数组元素个数查找  $size

        e.g.  查找数组中包含两个元素的
	db.class2.find({score:{$size:2}},{_id:0})

    选择数组的显示部分 $slice (用于field参数)
     
        e.g.  显示数组的前2项
	db.class2.find({},{_id:0,score:{$slice:2}})

	e.g.  跳过第一项显示后面两项
	db.class2.find({},{_id:0,score:{$slice:[1,2]}})
**其他查找操作符**
    $exists  判断一个域是否存在  值为bool
    
    e.g. 查找不存在sex域的文档 （true表示存在，false不存在）
    db.class0.find({sex:{$exists:false}},{_id:0})

    $mod  通过除数和余数查找文档

    e.g. 查找年龄除以2余数为1的
    db.class0.find({age:{$mod:[2,1]}},{_id:0})

    $type  根据值的数据类型筛选

    e.g. 查找age数据类型为1的文档
    db.class0.find({age:{$type:1}},{_id:0})

    * 数据类型和数字对照表参看文档 $type说明
**数据处理函数**
    db.collection.distinct(field)
    功能： 获取某个集合值的范围

    e.g. 获取class0中age域的值
         db.class0.distinct('age')

    pretty()
    功能: 将find结果格式化显示

    limit(n)
    功能： 显示find结果的前n条文档
    
    e.g.  显示查找结果的前5条
    db.class0.find({},{_id:0}).limit(5)

    skip(n)
    功能： 跳过前n条文档，显示后面的内容
 
    e.g.  跳过前5条文档，显示后面内容
    db.class0.find({},{_id:0}).skip(5)


    count（）
    功能： 对查找结果统计计数
    
    e.g. 统计有多少年来大于17的文档
    db.class0.find({age:{$gt:17}}).count()

    sort({field:1/-1})
    功能：对查找文档按照某个域的值排序
    参数：表示要排序的域

    e.g. 对查找文档按年龄升序排序（1表示升序-1表示降序）
    db.class0.find({},{_id:0}).sort({age:1})

    复合排序：对多个域进行排序，当第一排序项相同时，参考第二排序项排序

    e.g.  年龄相同时，按照name排序
    db.class0.find({},{_id:0}).sort({age:1,name:1})
    函数的连续调用

        * 当一个函数的返回结果仍然是文档集合，可以继续调用函数
        
	e.g. 查找年龄最大三名同学文档信息
	db.class0.find({},{_id:0}).sort({age:-1}).limit(3)

        * 可以对文档集合通过序列号直接选择

        e.g. 获取查找结果第二项
	     db.class0.find({},{_id:0})[1]

**文档删除操作**<br>
**mongo :   db.collection.deleteOne(query)**
	   
     e.g. 删除第一个年龄小于40的
	   db.class1.deleteOne({age:{$lt:40}})

	  db.collection.deleteMany(query)
	  功能：删除所有复合条件的文档
	  参数： query

	  e.g. 删除所有年龄大于30性别为m的
	   db.class1.deleteMany({age:{$gt:30},sex:'m'})

	  
	  db.collection.remove(query,justOne)
	  功能:删除文档
	  参数： query 筛选条件
	         justOne 默认false 此时同deleteMany
		         设置true  此时同deleteOne
          
	  e.g. 删除第一个性别为m的文档
	  db.class0.remove({sex:'m'},true)

        *  db.student.deleteMany({})可以删除集合中所有文档
 
        db.collection.findOneAndDelete(query)
	功能： 查找某个文档，并删除
	参数： query
	返回： 返回查找到的文档
	
	e.g.  查找第一个年龄为17的文档并删除
	 db.class0.findOneAndDelete({age:17})


# **Day03**
## 修改操作
**mongo: db.collection.updateOne(query,update,upsert)**<br>

       功能： 修改第一个符合条件的文档
       参数： query  筛选条件  用法同find query
             update  要修改的数据项，需要配合修改操作符使用
	         upsert  bool类型 默认表示没有符合筛选条件的文档则不做任何操作
	         如果设置为true 则没有筛选到文档就根于query和update插入文档

      e.g.  将Joy年龄修改为18
      db.class0.updateOne({name:'Joy'},{$set:{age:18}})
	
      e.g.  如果没有符合query条件的文档则插入新的文档
      db.class0.updateOne({name:'Han'},{$set:{age:18}},{upsert:true})

**db.collection.updateMany(query,update,upsert)**<br>

      功能： 修改所有复合条件的文档
      参数： 同updateOne

      e.g.  同时修改所有符合条件的文档
      db.class0.updateMany({age:{$lt:18}},{$set:{age:20}})
**db.collection.update(query,update,upsert,multi)**<br>

      功能: 修改筛选到的文档
      参数：query 筛选条件
            update 修改内容
	    upsert 如果为true则可插入新的文档
	    multi  默认表示只修改第一条符合条件文档
	           设置为true表示修改多条

        e.g. 修改所有人年龄为10岁
	db.class2.update({},{$set:{age:10}},false,true)

**db.collection.findOneAndUpdate(query,update)**<br>

      功能： 查找一个文档并修改
      参数： query 筛选条件
             update 修改内容
      返回： 返回修改之前的文档

      e.g.  查找一个文档并修改年龄为17
      db.class0.findOneAndUpdate({name:'Lily'},{$set:{age:17}})

**db.collection.findOneAndReplace(query,doc)**<br>

      功能： 查找并替换一个文档
      参数： query筛选条件
             doc  替换的文档
      返回： 返回原有文档
      
      e.g.  查找一个文档，并替换为新的文档
      db.class0.findOneAndReplace({name:'Joy'},{'name':'Jame',age:17,sex:'m'})

## 修改器的使用

$set :  修改一个域的值，或者增加一个域

    e.g.  使用set增加一个name域
    db.class0.updateOne({name:{$exists:false}},{$set:{name:'Han'}})

$unset:  删除一个域

     e.g.  删除han的age域
      db.class0.updateOne({name:'Han'},{$unset:{age:''}})


$rename : 修改一个域的域名

    e.g.  修改所有sex域名为gender
    db.class0.updateMany({},{$rename:{sex:'gender'}})

$setOnInsert : 当upsert插入文档时，作为补充的插入内容

    e.g.  当插入新文档时，作为补充插入的 内容
    db.class0.update({name:'Daivl'},{$set:{age:18},$setOnInsert:{gender:'w'}},{upsert:true})

$inc :  加法修改器

    e.g.  所有文档年龄域加1
    db.class0.updateMany({},{$inc:{age:1}})

$mul : 乘法修改器

    e.g.  将han年龄乘以2
     db.class0.updateOne({name:'Han'},{$mul:{age:2}})

**$inc $mul 操作数可以是正数，负数，整数，小数**


$max : 指定某个域的值，如果小于规定值则修改为规定值，大于规定值则不变  

    e.g. 如果age小于20则改为20，大于20则不变
    db.class0.updateOne({name:'Abby'},{$max:{age:20}})

$min : 指定某个域的值，如果大于规定值则修改为规定值，小于规定值则不变  

    e.g.  将年龄大于25的修改为25
     db.class0.updateMany({},{$min:{age:25}})

## 数组修改器

$push : 向数组中添加一项

    e.g.向数组中增加一项86
    db.class2.updateOne({name:'小亮'},{$push:{score:86}})

$pushAll: 向数组中增加多项

    e.g.  向数组中增加两项 5,10
    db.class2.updateOne({name:'小红'},{$pushAll:{score:[5,10]}})

$pull : 从数组中删除某一个值
  
    e.g.  删除小红score域中的5
    db.class2.update({name:'小红'},{$pull:{score:5}})

$pullAll : 同时删除数组中多个值

    e.g.  同时删除数组中的88和10
    db.class2.update({name:'小红'},{$pullAll:{score:[88,10]}})

$pop : 从数组中弹出一项
  
    e.g. 删除小明score中最后一项 （1表示最后一项，-1表示第一项）
    db.class2.update({name:'小明'},{$pop:{score:1}})

$addToSet : 向数组中添加一项，但是不能添加已有的内容

    e.g.  向数组中添加81，如果已经存在则无法添加
    db.class2.update({name:'小明'},{$addToSet:{score:81}})

$each : 对多个值进行逐一操作

    e.g.  同时添加90,10
    db.class2.update({name:'小红'},{$push:{score:{$each:[90,10]}}})

$position: 指定值的插入位置，配合each

    e.g.  向数组1号位置插入5
    db.class2.update({name:'小明'},{$push:{score:{$each:[5],$position:1}}})

$sort : 对数组排序，搭配each使用

    e.g. 对小明score排序，1升序-1降序
    db.class2.update({name:'小明'},{$push:{score:{$each:[],$sort:1}}})

## 时间类型

    获取当前时间：
    1. new Date() 自动生成当前时间

	e.g.
	db.class1.insertOne({book:'Python入门',date:new Date()})

	2. ISODate() 自动获取当前时间
	
	e.g.
	db.class1.insertOne({book:'Python精通',date:ISODate()})

	3. Date()  获取系统当前时间

        e.g.
	db.class1.insertOne({book:'Python放弃',date:Date()})
    
    存储任意时间
        
	ISODate()
	功能： 将指定的时间字符串转为Mongodb时间存储
	参数： 指定时间
	       “2019-01-01 12:12:12”
	       “20190101 11:11:11”
	       “20190101”
        
	e.g.
	db.class1.insertOne({book:'Python之美',date:ISODate("2018-11-20 20:58:30")})

## 时间戳

    valueOf()
    功能： 将ISO date转换为时间戳
    
    e.g.  记录1970.1.1 00:00:00到现在多少毫秒
    db.class1.insertOne({book:'Python涅磐',date:ISODate().valueOf()})

## Null数据类型

    值： null

    1. 表示某个域值为空

    e.g. 表示price域值为空
     db.class1.insertOne({book:'Python放生',price:null})

    2. 表示某个域不存在
    
    e.g. 查找price域为null或者不存在这个域的文档
    db.class1.find({price:null},{_id:0})

## Object类型（内部文档）
    文档中某个域的值还是文档，则该值为Object

    * 当使用内部文档的某个域时，需要外部文档域名 . 内部文档域名的方法引用，引用时需要加引号

    e.g. 通过book.title查找
    db.class3.find({'book.title':'狂人日记'},{_id:0})
    
    e.g. 修改边城价格为35
    db.class3.update({"book.title":'边城'},{$set:{'book.price':35}})

## 通过数组下标直接引用数组项
    在使用数组时，可以直接通过数组域 . 数组下标操作数组的某一项
    
    e.g.  修改小明score中第二项为67
     db.class2.update({name:'小明'},{$set:{'score.1':67}})


## 创建索引
    db.collection.createIndex(index,option)
    功能： 创建索引
    参数： 索引域 和 索引选项

    e.g. 为name域创建索引
         db.class0.createIndex({name:1})
  
    * _id域会自动生成索引，该索引不能删除
    * 1 表示正向索引，-1表示逆向索引
    * 一个集合中不能创建重复的索引
    
    查看集合中索引：    
        db.collection.getIndexes()
    
    定义索引名称
        e.g.  通过索引选项name定义索引名称
        db.class0.createIndex({age:1},{name:'ageIndex'})

    其他索引创建方法

       ensureIndex()
       功能：创建索引
       参数：同createIndex
   
       e.g. 创建方法同createIndex
       db.class0.ensureIndex({gender:1})

       createIndexes([{},{}...])
       功能： 同时创建多个索引
       参数： 数组中填写多个索引项即可

       e.g.  同时创建age_-1  gender_-1两个索引
       db.class0.createIndexes([{age:-1},{gender:-1}])

## 删除索引
    db.collection.dropIndex()
    功能：删除一个索引
    参数: 索引名或者键值对删除

    e.g.  通过名称删除索引
    db.class0.dropIndex("gender_-1")

    e.g. 通过键值对删除
    db.class0.dropIndex({age:-1})

    db.collection.dropIndexes()
    功能： 删除所有索引 （除了_id）

    e.g. 删除class0中所有索引
        db.class0.getIndexes()

## 索引类型

    复合索引 ： 根据多个域创建一个索引

    e.g. 根据name  age两个域创建一个索引
         db.class0.createIndex({name:1,age:-1})

    子文档和数组索引：如果对某个域创建索引，该域的值为子文档或者数组，则对数组或者子文档中某一项进行查找也是索引查找。

    e.g. 如果对book创建索引则该查找也是索引查找
    db.class3.find({'book.title':'围城'},{_id:0})


    唯一索引 ： 要求创建索引的域不能有重复的值

    e.g.  对name域创建唯一索引
    db.class0.createIndex({name:-1},{unique:true})


    稀疏索引 ： 会在创建索引时忽略没有指定域的文档

    e.g. 对gender域创建稀疏索引
    db.class0.createIndex({gender:1},{sparse:true})
## **Day04**
## 聚合操作
    对文档数据进行整理筛选统计

    db.collection.aggregate()
    功能： 完成聚合操作
    参数： 聚合条件，需要配合聚合操作符

    聚合操作符

    $group  分组聚合 往往需要配合一定的统计操作符完成
   
       统计求和： $sum 
       
       e.g. 按照性别分组，获取每组人数
       db.class0.aggregate({$group:{_id:'$gender',num:{$sum:1}}})

$group 

    统计求和 ： $sum
    统计平均数： $avg
       e.g.  按性别分组，求平均年龄
       db.class0.aggregate({$group:{_id:'$gender',avg:{$avg:'$age'}}})
   
    求最大值： $max
       e.g.  按性别分组，求每组最大年龄
       db.class0.aggregate({$group:{_id:'$gender',max:{$max:'$age'}}})

    求最小值： $min
    求第一个数： $first
    求最后一个数： $last


$project ： 用于格式化显示文档内容
    
    * 值的写法同find的field参数
    
    e.g. 按照指定域名显示
    db.class0.aggregate({$project:{_id:0,Name:'$name',Age:'$age'}})

$match : 筛选数据

    * match值写法与find的 query参数相同

    e.g. 筛选年龄大于20的文档
     db.class0.aggregate({$match:{age:{$gt:20}}})

$limit  显示前几条文档

     e.g.  显示前3条文档
     db.class0.aggregate({$limit:3})

$skip  跳过前几条文档
  
     e.g.  跳过前3条显示后面的
      db.class0.aggregate({$skip:3})

$sort  对所选的域排序显示
  
     e.g.  按照年龄排序显示
     db.class0.aggregate({$sort:{age:1}})

## 聚合管道
    指将多个聚合操作合并到一起，即上一个聚合的结果交给下一个聚合继续操作，最终完成一个较复杂的功能

    aggregate([{聚合1},{聚合2}...])

    e.g.  显示年纪最小三位同学，不显示_id
    db.class0.aggregate([{$sort:{age:1}},{$project:{_id:0}},{$limit:3}])

    1. 将所有男生按照年龄排序，不显示_id

       db.class0.aggregate([{$match:{gender:'m'}},{$sort:{age:1}},{$project:{_id:0}}])

    2. 统计一下班级中有无重名同学

       db.class0.aggregate([{$group:{_id:"$name",num:{$sum:1}}},{$match:{num:{$gt:1}}}])
## 固定集合

    指的是mongodb中创建的固定大小的集合

    特点 ： 
    1. 能够淘汰早期数据
    2. 控制集合大小
    3. 结构紧凑，插入查找速度较快
    
    使用 ：日志处理  临时缓存

    创建 ： db.createCollection('log',{capped:true,size:10000,max:10})

    capped : true   表示创建固定集合
    size：10000   表示集合中最多存放多少字节数据
    max：10  表示集合中最多存放多少个文档

## 文件存储
    文件存储数据库方式

    1. 存储路径 ： 将本地文件所在的路径以字符串存储
                    到数据库中。
       优点： 节省数据库空间，从数据库获取存储比较简单
       缺点： 当数据库或者文件发生变动时必须修改数据库存储内容
  
    2. 存储文件本身： 将文件转换为二进制存储到数据库

       优点： 文件随数据库移动，数据在文件即在
       缺点： 占用数据库空间大，存取效率低

## GridFS文件存储方案
    目的：更好的帮助存储MongoDB中超过16M的大文件
    
    方案解释：在mongodb数据库中创建两个集合，共同存储文件。一个存储文件信息，一个存储文件内容。两个集合相互配合。

     fs.files : 存储文件信息（文件名，大小等）
	 fs.chunks: 以二进制存储文件内容

    存储方法：mongodbfiles -d  dbname  put  file
                               数据库      要存的文件
    
     e.g. 将img.jpg 存储到 grid数据库
          mongofiles -d grid put ./img.jpg

    获取方法：mongofiles -d  dbname  get  file

         * file 必须是fs.files中 filename值

	 e.g. 从数据库中获取文件
	      mongofiles -d grid get ./img.jpg
    
    优缺点 ： 
         优点： 存储方便，提供了较好的命令，方便数据库移动

	     缺点： 读写效率低，不建议存储小文件
# **python 模块  --> pymongo 第三方模块**
    安装： sudo pip3 install  pymongo

    操作步骤：
       1. 创建mongodb数据库连接对象
          
	     conn = pymongo.MongoClient('localhost',27017)

       2. 创建数据库操作对象
         
	    db = conn.stu 
        db = conn['stu']

       3. 生成集合对象
         
	    myset = db.class0
	    myset = db['class0']
       
       4. 通过集合对象操作数据库

       5. 关闭数据库连接
          conn.close()


## 插入操作 

    insert_one() 插入一条文档
    insert_many() 插入多条文档
    insert()  插入一条或者多条文档
    save()  插入数据，_id相同时替换原有内容


## 查找操作

    find()
    功能: 查找所有文档
    参数： 同mongo shell find
    返回： 游标对象

    * 所有操作符在python中以字符串方式传入参数结构
    * mongo中 true  false  null 对应python中的True False None

## cursor 对象属性

    next() 获取下一个文档
    limit() 显示前几条文档
    skip()  跳过前几条
    count()  计数
    sort()  排序
    调用limit skip sort 时要求游标必须是完整的没取过值

    find_one()  
    功能 ： 查找一个文档
    参数 ： 同find()
    返回 ： 返回一个字典


## 修改操作

    update_one()  修改一条文档
    update_many() 修改多条文档
    update() 

## 删除操作

    delete_one()  删除一个文档
    delete_many()  删除多个文档
    remove(query,multi=True)  


##索引操作

    create_index()
    功能: 创建索引
    参数： 直接写要创建索引的域名
    e.g.  'name' 表示对name创建正向索引是以元组的形式写入创建索引键值对
    e.g.  [('name',-1)] 表示对name创建逆向索引
    返回： 返回索引名

    list_indexes()  查看索引 

    drop_index() 
    功能： 删除一个索引
    参数： 索引名称

    drop_indexes()  删除所有索引


## 聚合操作

    aggregate([])
    参数： 同mongoshell 中聚合
    返回值： 和find()相同返回一个游标对象


##练习 
1. 将没有性别域的文档删除
2. 给所有文档增加一个域 
	 分数取值范围 60--100
	 score:{'Chinese':xx,'math':xx,'English':xx}
3. 聚合操作，查看所有女生的英语成绩排序，不显示_id项


## 文件操作

    Binary data ： mongodb中二进制格式

    文件存储步骤：
    1. 连接数据库，生成数据库对象，集合对象
    2. 选择要存储的文件 以 rb方式读取
    3. 将读取内容转换为mongodb二进制存储方式
        
	content = bson.binary.Binary(data)
	功能： 将bytes字串数据转换为Mongo的二进制存储        形式
	参数： 要存储的内容
	返回值： 转换后的待存储数据
    4. 将存储内容放入文档，插入数据库
