# ORM
## 创建数据库
```python 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 数据库名称
        'NAME': 'photo',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

```
## 数据库同步
1. ./manage.py makemigrations<br/>作用：将每个应用下的models.py文件生成一个数据库中间文件并保存在migrations的目录中
2. ./manage.py migrate<br/>作用：将每个应用下的migrations目录中的中间文件同步到数据库中
3. ./manage.py inspectdb > 文件名.py --->通过数据库自动导出Models

## 编写Models 
1. 字段类型(Field Types)
   1. BooleanField()
      ```python
      isActive = models.BooleanField(default=True)
      ```
   2. CharField()   
      ```python
      name = models.CharField(max_length=30)
      ```

   3. DateField()   
      ```python
      publicate_date = models.DateField()
      ```
   4. DateTimeField()
      ```python
      pub_date = models.DateTimeField('date published')
      ```
   5. DecimalField() 
   6. FloatField()   
      ```python
      ａ= models.FloatField(…，max_digits=5，       decimal_places=2)
      ```
   7. IntegerField() 
      ```python
      a = models.IntegerField()
      STATUS_DRAFT = 2
      STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DRAFT, '草稿'),
        )


      status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
      ```
   8. EmailField()   
      a = models.EmailField(null=True)
      ```
   9. URLField()     
      ```python 
      url = models.URLField()
      ```

   10. ImageField() 
      ```python 
      img = img = models.ImageField(
        upload_to='static/upload/landscape',
        verbose_name='风景')
      ```
   11. TextField()   
      ```python
      content = models.TextField(verbose_name="正文", help_text="正文必须为MarkDown格式")
      ```

## 所有字段类型
    1、models.AutoField　　

               自增列 = int(11)
               如果没有的话，默认会生成一个名称为 id 的列
               如果要显式的自定义一个自增列，必须设置primary_key=True。

     
    2、models.CharField　　

               字符串字段
        　　必须设置max_length参数

     
    3、models.BooleanField　　

               布尔类型=tinyint(1)
        　　不能为空，可添加Blank=True

     
    4、models.ComaSeparatedIntegerField　　

               用逗号分割的数字=varchar
        　　继承CharField，所以必须 max_lenght 参数

     
    5、models.DateField

               日期类型 date
        　　DateField.auto_now：保存时自动设置该字段为现在日期，最后修改日期
               DateField.auto_now_add：当该对象第一次被创建是自动设置该字段为现在日期，创建日期。

     
    6、models.DateTimeField　　

               日期时间类型 datetime
        　　同DateField的参数

     
    7、models.Decimal　　

               十进制小数类型 = decimal
               DecimalField.max_digits：数字中允许的最大位数
               DecimalField.decimal_places：存储的十进制位数

     
    8、models.EmailField　　

        　　一个带有检查 Email 合法性的 CharField

     
    9、models.FloatField　　

               浮点类型 = double

     
    10、models.IntegerField　　

               整形

     
    11、models.BigIntegerField　　

               长整形
        　　integer_field_ranges = {

        　　　　'SmallIntegerField': (-32768, 32767),

        　　　　'IntegerField': (-2147483648, 2147483647),

        　　　　'BigIntegerField': (-9223372036854775808, 9223372036854775807),

        　　　　'PositiveSmallIntegerField': (0, 32767),

        　　　　'PositiveIntegerField': (0, 2147483647),

        　　}

     
    12、models.GenericIPAddressField　　

                一个带有检查 IP地址合法性的 CharField

     
    13、models.NullBooleanField　　

               允许为空的布尔类型

     
    14、models.PositiveIntegerFiel　　

               正整数

     
    15、models.PositiveSmallIntegerField　　

               正smallInteger

     
    16、models.SlugField　　

               减号、下划线、字母、数字

     
    17、models.SmallIntegerField　　

               数字
        　　数据库中的字段有：tinyint、smallint、int、bigint

     
    18、models.TextField　　

                大文本。默认对应的form标签是textarea。

     
    19、models.TimeField　　

               时间 HH:MM[:ss[.uuuuuu]]

     
    20、models.URLField　　

                一个带有URL合法性校验的CharField。

     
    21、models.BinaryField　　

               二进制
               存储二进制数据。不能使用filter函数获得QuerySet。

     
    22、models.ImageField   

               图片
               ImageField.height_field、ImageField.width_field：如果提供这两个参数，则图片将按提供的高度和宽度规格保存。
               该字段要求 Python Imaging 库Pillow。
               会检查上传的对象是否是一个合法图片。

     
    23、models.FileField(upload_to=None[, max_length=100, ** options])

               文件
               FileField.upload_to：一个用于保存上传文件的本地文件系统路径，该路径由 MEDIA_ROOT 中设置
               这个字段不能设置primary_key和unique选项.在数据库中存储类型是varchar，默认最大长度为100

     
    24、models.FilePathField(path=None[, math=None, recursive=False, max_length=100, **options])

               FilePathField.path：文件的绝对路径，必填
               FilePathField.match：用于过滤路径下文件名的正则表达式，该表达式将用在文件名上（不包括路径）。
               FilePathField.recursive：True 或 False，默认为 False，指定是否应包括所有子目录的路径。
               例如：FilePathField(path="/home/images", match="foo.*", recursive=True)

                             将匹配“/home/images/foo.gif”但不匹配“/home/images/foo/bar.gif”    

  

## 常用字段类型
1. primary_key<br/>作用：指定当前列为主键
2. null<br/>作用：指定当前字段是否允许为空,默认为False,不能为空
3. default<br/>作用：指定当前字段的默认值
4. db_column<br/>作用：指定当前字段映射到表的列的名称
5. db_index<br/>作用：指定是否为当前列增加索引,设置为True表示增加索引
6. unique<br/>作用：指定当前列是否为唯一，设置为True表示该列值唯一 
## django 模型models 字段常用参数
    1、null

                如果是True，Django会在数据库中将此字段的值置为NULL，默认值是False

     
    2、blank

        　　如果为True时django的 Admin 中添加数据时可允许空值，可以不填。如果为False则必须填。默认是False。
               null纯粹是与数据库有关系的。而blank是与页面必填项验证有关的

     
    3、primary_key = False

        　  主键，对AutoField设置主键后，就会代替原来的自增 id 列

     
    4、auto_now 和 auto_now_add

        　　auto_now   自动创建---无论添加或修改，都是当前操作的时间
        　　auto_now_add  自动创建---永远是创建时的时间

     
    5、choices

              一个二维的元组被用作choices，如果这样定义，Django会select box代替普通的文本框，
              并且限定choices的值是元组中的值
              GENDER_CHOICE = (
                    (u'M', u'Male'),
                    (u'F', u'Female'),
              )
              gender = models.CharField(max_length=2,choices = GENDER_CHOICE)

     
    6、max_length

                字段长度

     
    7、default

                默认值

     
    8、verbose_name　　

               Admin中字段的显示名称，如果不设置该参数时，则与属性名。

     
    9、db_column　　

               数据库中的字段名称

     
    10、unique=True　　

              不允许重复

     
    11、db_index = True　　

             数据库索引

     
    12、editable=True　　

              在Admin里是否可编辑

     
    13、error_messages=None　　

              错误提示

     
    14、auto_created=False　　

              自动创建

     
    15、help_text　　

              在Admin中提示帮助信息

     
    16、validators=[]

                 验证器

     
    17、upload-to

                文件上传时的保存上传文件的目录


## 数据库的CRUD操作
**注意：Django中的数据库查询操作的核心时QuerrySet

1. 增加数据