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
print('verson:0.1')
print("欢迎使用本英->汉词典(事实上也可以汉->英)，作者为HeimaoLST")
print('遇到bug的话不用通知我，你们说的其实我都知道，只是不想改罢了(')
print('PS：代码开源了，知道怎么解决的话最好帮我修一下')
print('未来它可能会更新，希望它能帮到你')
while True:

	Date = {
		'kw': 'happy'
	}
	Date['kw'] = input("请输入你想查询的单词:")

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
	#print(obj)
	# print(obj["data"][0]['v'])
	temp = obj.get('data','未找到相关单词')
	if(len(temp)==0):
		print("查不到欸，会不会是打错了？")
	else:
		print('相关词如下：')
		for i in temp:
			key = i['k']
			value = i['v']
			print(key,value)