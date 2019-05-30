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




















