#!bin/bash
#获取当前时间
a='woshi a'
time=$(date +"%Y%m%d20") 

b='ls'
echo $time
#scp -r 
echo $a
your_name="qinjx"
echo $your_name
echo ${your_name} $time

# 字符串
your_name="runoob"
# 使用双引号拼接
greeting="hello, "$your_name" !"
greeting_1="hello, ${your_name} !"
echo $greeting  $greeting_1
# 使用单引号拼接
greeting_2='hello, '$your_name' !'
greeting_3='hello, ${your_name} !'
echo $greeting_2  $greeting_3
#截取字符串长度
string="runoob is a great site"
echo ${string:1:4} # 输出 unoo
echo ${time:0:5}

#数组
array_name=(v0 v1 v2 v3)


valuen=${array_name[1]}

echo $valuen


echo ${array_name[1]}

my_array=(A B "C" D)

echo "第一个元素为: ${my_array[0]}"
echo "第二个元素为: ${my_array[1]}"
echo "第三个元素为: ${my_array[2]}"
echo "第四个元素为: ${my_array[3]}"