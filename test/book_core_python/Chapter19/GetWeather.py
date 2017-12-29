# -*- coding:utf-8 -*-
# file: GetWeather.py
#
import urllib
import re
import Tkinter
import datetime
class Window:
	def __init__(self, root):
		self.root = root									# 创建组件
		self.label = Tkinter.Label(root, text = '输入城市:')
		self.label.place(x = 5, y = 15)
		self.entryCity = Tkinter.Entry(root)
		self.entryCity.place(x = 65, y = 15)
		self.get = Tkinter.Button(root, 
				text = '获取天气', command = self.Get)
		self.get.place(x = 230, y = 15)
		self.edit = Tkinter.Text(root,width = 200,height = 150)
		self.edit.place(y = 50)
	def Get(self):
		city = self.entryCity.get().encode('utf-8')						# 获取城市
		addr = 'http://weather.cn.yahoo.com/weather.html?city=%s'				# 查看天气地址
		cityencode = urllib.quote(city)								# 对中文进行编码
		data = urllib.urlopen(addr % cityencode)						# 打开网页
		s = data.read()										# 获取网页数据
		m = re.compile(r'(?<=dt_d...).+?(?=</div)',re.S|re.I|re.U)				# 编译正则表达
		weather = re.compile(r'(?<=ft1..).+?(?=</span)',re.S|re.I|re.U)
		hitp = re.compile(r'(?<=hitp..).+?(?=</span)',re.S|re.I|re.U)
		lotp = re.compile(r'(?<=lotp..).+?(?=</span)',re.S|re.I|re.U)
		today = datetime.date.today()								# 获得当前日期
		year = today.strftime('%Y')								# 日期格式化
		month = today.strftime('%m')
		day = today.strftime('%d')
		days = ['今天','明天','后天']
		a = 0
		for i in m.findall(s):									# 循环处理天气
			d = str(int(day)+a)
			dates = '%s-%s-%s' % (year, month, d)
			self.edit.insert(Tkinter.END, 							# 输出日期和城市
					'%s%s(%s)\n' % (city, days[a],dates))
			a = a + 1
			for j in weather.findall(i):
				self.edit.insert(Tkinter.END, j +'\n')					# 输出天气
			for k in hitp.findall(i):
				self.edit.insert(Tkinter.END, '最高温度: ')
				self.edit.insert(Tkinter.END, k +'\n')					# 输高最高温度
			for l in lotp.findall(i):
				self.edit.insert(Tkinter.END, '最低温度: ')				# 输出最低温度
				self.edit.insert(Tkinter.END, l +'\n')
			self.edit.insert(Tkinter.END, 
					'******************************\n')
		data.close()
root = Tkinter.Tk()
window = Window(root)
root.minsize(300,245)
root.mainloop()
