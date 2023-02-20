# README

## 一、字符串的高级

### 1.len的使用

> 使用len方法来获取字符串的长度

```python
str="HeimaoLST"
print(len(str))
#len()
```

### 2.查找内容find

> 查找指定内容在字符串中是否存在,若存在则返回在字符串中第一次出现的索引值否则返回-1

```python
str="HeimaoLST"
print(str.find("H"))
#str.find(const str)
```

### 3.判断:startswith,endswith

> 判断字符串是不是以特定内容开头或者结尾

```python
str="HeimaoLST"
print(str.startswith("H"))
print(str.endswith("H"))
#str.startswith()
#str.endswith()
```

### 4.统计次数count()

> 统计某个字符在字符串中出现的次数

 ```python
 str="HeimaoLST"
 print(str.count("H"))
 #str.count()
 ```

### 5.替换replace(a,b)

>将字符串中的a用b替换

```python
str="HeimaoLST"
print(str.replace("H",'X'))
```

### 6.字符串分割split

> 将字符串以某字符串为界分割为列表

```python
str="1@1@1@1"
print(str.split("@"))
```

### 7. 修改大小写upper(),lower()

> 将字符串中的大小写转换
>
> ex:  abbcD-->ABBCD

```python
str.upper()
str.lower()
```

### 8.去空格strip() 

> 将字符串两边的空格去除
>
> 注:不可去除中间出现的空格
>
> "      b      "-->"b"

```python
str.strip()
```

### 9.插入元素join()

> split()的逆操作
>
> str='a'
>
> str.join("HeimaoLST")
>
> -->HaeaiamaaaoaLaSaT

```python
str.join("XXX")
```

## 二、列表的高级使用(增删改查)

### 1.增加元素

#### I.append方法(追加)

> 在列表元素后面追加元素

```python
Date = ["AAA","BBB"]
Date.append("CCC")
->["AAA","BBB","CCC"]
```

#### II.insert方法(插入)

> 在任意位置插入新元素

```python
Date = ["AAA","BBB","DDD"]
Date.insert(2,"CCC")
->["AAA","BBB","CCC","DDD"]
#index为你想插入数据的那个下标
insert(index,object)

```

#### III.extend方法(合并)

> 将两个列表合并 
>
> 类似于append追加不过操作对象是列表

```
Date=[1,2,3]
Date1=[4,5]
Date.extend(Date1)
Date->[1,2,3,4,5]
```

### 2.删除元素

#### I.del根据下标进行删除

```python
Name=["AAA","BBB","CCC"]
del Name[2]
Name->["AAA"，"BBB"]
```

#### II.pop删除最后一个元素

```python
Name=["AAA","BBB","CCC"]
Name.pop()
Name->["AAA","BBB"]
```

#### III.根据元素的值进行删除

```python
Name=["AAA","BBB","CCC"]
Name.remove("CCC")
Name->["AAA","BBB"]
```

### 3.修改元素

#### I.通过使用下标直接修改

```
Date=[1,2,3,4]
Date[3]=5
Date->[1,2,3,5]
```

### 4.查找元素

#### 通过in/not in 来判断是否在列表中

```python
food_list=["胡辣汤","豆腐脑","热干面"]
food=input("请输入一种食物：")
if food in food_list:
	print("在")
else:
	print("不在") 
# if food not in food_list    
```

## 三、元组相关

### 元组的不可修改性

元组的大概逻辑和列表相似（可以通过下标访问对应元素 也可以打印出整个列表）

但是元组无法进行修改

```python
date=(1,2,3,4)
date[3]=1
##无法进行上述操作
```

## 四、对字符串，元组，列表进行切片操作

### 切片

切片是指对操作对象截取其中一部分的操作

切片的语法：[起始:结束:步长] 也可以简化使用[起始:结束]

注意：选取的区间从起始位开始到结束位的前一位结束即“左闭右开” 步长表示间隔

```python
str="HeimaoLST"
str[4] #a
str[3:7] #maoL  
str[1:] #eimaoLST
str[:4] #Heim
str[1:5:2] #em
```

## 五、字典的高级使用

### 4.查

#### I.使用[]方式直接访问

当访问不存在的key时会报错

```python
peo={'name':"XX",'age':18}
peo["name"]
```

#### II.使用.get方式来访问

当访问不存在的key时会返回None

```
peo={'name':"XX",'age':18}
peo.get("name")
```

## 六、文件操作

### 1.文件的打开与关闭

python通过使用open()函数来对文件进行操作

open("文件名/文件的路径"，操作模式)

```、
f=open("test.txt",'w')//打开文件
f.write("Hello World")
f.close()//关闭文件
```

### 2.文件的读取与写入

关键函数：write()，read()；

```python
fp=open("demo.txt",'w')//使用w模式进行写入操作时，会覆盖掉原有文件 而a模式为为在文件末尾追加内容
fp.write("im here\n")
fp=open("demo.txt",'a')
fp.write("Hello world\n"*5)
fp=open("demo.txt",'r')
print(fp.read())//read()读取文件的所有内容
print(fp.readline())//readline()逐行读取文件的内容，但只会读取一行
print(fp.readlines())//readlines()逐行读取文件的所有内容并且把每一行的内容以列表的形式保存

```

### 3.文件的序列化与反序列化

有事我们会遇到将列表写入文件的情况 但列表位于内存中 且write只支持写入字符串

因此会存在 由内存数据-->字节数据的操作 该操作被称作"序列化" ”反序列化”同理

python中的json模块帮助我们完成这一操作

#### I.文件的序列化

dumps /dump

```python
import json
names=['xx','xxx','xxxx']
fp=open("test.txt",'w')
name=json.dumps(names)
fp.write(name)
fp.close()
#-----
json.dump(names,fp)
fp.close
### dump()可以看做是将转换与写入整合为了一个函数 但仍需要手动关闭文件

```

#### II.文件的反序列化

loads/load

```python
import json
fp=open("test.txt",'r')
content=fp.read()
fp.close()
keys=json.loads(content)
#----
keys=json.loads(fp)
fp.close()
```

### 4.文件的异常处理

在使用文件时应该做好异常处理来进行反馈\

使用try except来进行处理

```
try：
	fp=open()
	fp.read()
except Erro:
	"Try again"
```

## 七、Urllib的使用

### 1.使用urllib来对页面资源进行下载

```python
import urllib.request
##下载网页
'''
url = "http://www.bilibili.com"
urllib.request.urlretrieve(url,"bilibili.html")
'''
##下载图片
'''
url_img='https://hbimg.b0.upaiyun.com/8372431cc945ac007941a4d7c4fbc2bcf1aa31bd437d5-OiQB88_fw658'
urllib.request.urlretrieve(url_img,'img.jpg')
'''
#下载视频
'''
url_video="xx"
urllib.request.urlretrieve(url_video,'video.mp4')
'''
```

### 2.请求对象的定制

对方服务器可能会有一定的反爬虫机制 这个时候为了使用爬虫，我们需要对我们的UA进行定制

```python

import urllib.request
url = 'https://www.baidu.com'
##定义请求头
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0'
	}
##定制请求对象
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
```

### 3.对内容进行编码

#### I.quote方法

quote方法来源于urllib.parse用于对文字进行转码处理

```
urllib.parse.quote(name)
```

```python
import urllib.request
import urllib.parse
# url = "https://www.baidu.com/s?wd=卢本伟"
##中间进行了一次转码操作，但是我们人类不方便手动转码 因此转码操作很有必要
url = "https://www.baidu.com/s?wd=%E5%8D%A2%E6%9C%AC%E4%BC%9F"
name = "卢本伟"
unicode = urllib.parse.quote(name)
print(unicode)
```

#### II.urlencode方法

urlencode可以对多个参数进行转码操作

```python
import urllib.request
import urllib.parse
# url = "https://www.baidu.com/s?wd=卢本伟&sex=男&loca=CN"
##中间进行了一次转码操作，但是我们人类不方便手动转码 因此转码操作很有必要
url = "https://www.baidu.com/s?wd=%E5%8D%A2%E6%9C%AC%E4%BC%9F&sex=%E7%94%B7&loca=CN"
##urlencode操作的对象是字典 使用时需要先将参数加入到字典中
Date = {
   'wd':'卢本伟','sex':'男','loca':'CN'
}
New_Date = urllib.parse.urlencode(Date)
print(New_Date)
```

### 4.POST方法的处理

以百度翻译为例

```python
import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0'
   }
Date = {
   'kw':'super'
}
##post请求的参数必须要进行编码
##注意两次encode
Date = urllib.parse.urlencode(Date).encode('utf-8')

##post请求的内容并不能直接拼接而是以字节数据地形式发送
request = urllib.request.Request(url,Date,headers)
response = urllib.request.urlopen(request)

#不要忘了解码
content = response.read().decode('utf-8')
print(content)
```
