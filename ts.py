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
print('HHHHHHHHH     HHHHHHHHH                      iiii                                                             LLLLLLLLLLL                SSSSSSSSSSSSSSS TTTTTTTTTTTTTTTTTTTTTTT')
print('H:::::::H     H:::::::H                     i::::i                                                            L:::::::::L              SS:::::::::::::::ST:::::::::::::::::::::T')
print('H:::::::H     H:::::::H                      iiii                                                             L:::::::::L             S:::::SSSSSS::::::ST:::::::::::::::::::::T')
print('HH::::::H     H::::::HH                                                                                       LL:::::::LL             S:::::S     SSSSSSST:::::TT:::::::TT:::::T')
print('  H:::::H     H:::::H      eeeeeeeeeeee    iiiiiii    mmmmmmm    mmmmmmm     aaaaaaaaaaaaa      ooooooooooo     L:::::L               S:::::S            TTTTTT  T:::::T  TTTTTT')
print('  H:::::H     H:::::H    ee::::::::::::ee  i:::::i  mm:::::::m  m:::::::mm   a::::::::::::a   oo:::::::::::oo   L:::::L               S:::::S                    T:::::T        ')
print('  H::::::HHHHH::::::H   e::::::eeeee:::::ee i::::i m::::::::::mm::::::::::m  aaaaaaaaa:::::a o:::::::::::::::o  L:::::L                S::::SSSS                 T:::::T        ')
print('  H:::::::::::::::::H  e::::::e     e:::::e i::::i m::::::::::::::::::::::m           a::::a o:::::ooooo:::::o  L:::::L                 SS::::::SSSSS            T:::::T        ')
print('  H:::::::::::::::::H  e:::::::eeeee::::::e i::::i m:::::mmm::::::mmm:::::m    aaaaaaa:::::a o::::o     o::::o  L:::::L                   SSS::::::::SS          T:::::T        ')
print('  H::::::HHHHH::::::H  e:::::::::::::::::e  i::::i m::::m   m::::m   m::::m  aa::::::::::::a o::::o     o::::o  L:::::L                      SSSSSS::::S         T:::::T        ')
print('  H:::::H     H:::::H  e::::::eeeeeeeeeee   i::::i m::::m   m::::m   m::::m a::::aaaa::::::a o::::o     o::::o  L:::::L                           S:::::S        T:::::T        ')
print('  H:::::H     H:::::H  e:::::::e            i::::i m::::m   m::::m   m::::ma::::a    a:::::a o::::o     o::::o  L:::::L         LLLLLL            S:::::S        T:::::T        ')
print('HH::::::H     H::::::HHe::::::::e          i::::::im::::m   m::::m   m::::ma::::a    a:::::a o:::::ooooo:::::oLL:::::::LLLLLLLLL:::::LSSSSSSS     S:::::S      TT:::::::TT      ')
print('H:::::::H     H:::::::H e::::::::eeeeeeee  i::::::im::::m   m::::m   m::::ma:::::aaaa::::::a o:::::::::::::::oL::::::::::::::::::::::LS::::::SSSSSS:::::S      T:::::::::T      ')
print('H:::::::H     H:::::::H  ee:::::::::::::e  i::::::im::::m   m::::m   m::::m a::::::::::aa:::a oo:::::::::::oo L::::::::::::::::::::::LS:::::::::::::::SS       T:::::::::T      ')
print('HHHHHHHHH     HHHHHHHHH    eeeeeeeeeeeeee  iiiiiiiimmmmmm   mmmmmm   mmmmmm  aaaaaaaaaa  aaaa   ooooooooooo   LLLLLLLLLLLLLLLLLLLLLLLL SSSSSSSSSSSSSSS         TTTTTTTTTTT      ')
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