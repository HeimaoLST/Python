# _*_ coding: utf-8 _*_
# ------ -------------------------
# @Author : HeimaoLST
# @Github :
# -------------------------------
# @File : ts.py
# @Software : PyCharm
# @Time : 2023/2/16 14:25
# -------------------------------
import urllib.request
import urllib.parse
import json
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
obj = json.loads(content)
#print(type(obj))
print(obj)
print(obj["data"][0]['v'])
print(obj["data"][0])