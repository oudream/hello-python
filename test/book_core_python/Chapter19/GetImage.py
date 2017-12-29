# -*- coding:utf-8 -*-
# file: GetImage.py
#
import Tkinter
import urllib
import HTMLParser
class MyHTMLParser(HTMLParser.HTMLParser):						# 创建HTML解析类
	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)
		self.gifs = []								# 创建列表，保存gif
		self.jpgs = []								# 创建列表，保存jpg
	def handle_starttag(self, tags, attrs):						# 处理起始标记
		if tags == 'img':							# 处理图片
			for attr in attrs:
				for t in attr:
					if 'gif' in t:
						self.gifs.append(t)			# 添加到gif列表
					elif 'jpg' in t:
						self.jpgs.append(t)			# 添加到jpg列表
					else:
						pass
	def get_gifs(self):								# 返回gif列表
		return self.gifs
	def get_jpgs(self):								# 返回jpg列表
		return self.jpgs
class Window:
	def __init__(self, root):
		self.root = root							# 创建组件
		self.label = Tkinter.Label(root, text = '输入URL:')
		self.label.place(x = 5, y = 15)
		self.entryUrl = Tkinter.Entry(root,width = 30) 
		self.entryUrl.place(x = 65, y = 15)
		self.get = Tkinter.Button(root, 
				text = '获取图片', command = self.Get)
		self.get.place(x = 280, y = 15)
		self.edit = Tkinter.Text(root,width = 470,height = 600)
		self.edit.place(y = 50)
	def Get(self):
		url = self.entryUrl.get()						# 获取URL
		page = urllib.urlopen(url)						# 打开URL
		data = page.read()							# 读取URL内容
		parser = MyHTMLParser()							# 生成实例对象
		parser.feed(data)							# 处理HTML数据
		self.edit.insert(Tkinter.END, '====GIF====\n')				# 输出数据
		gifs = parser.get_gifs()
		for gif in gifs:
			self.edit.insert(Tkinter.END, gif + '\n')
		self.edit.insert(Tkinter.END, '===========\n')
		self.edit.insert(Tkinter.END, '====JPG====\n')
		jpgs = parser.get_jpgs()
		for jpg in jpgs:
			self.edit.insert(Tkinter.END, jpg + '\n')
		self.edit.insert(Tkinter.END, '===========\n')
		page.close()
root = Tkinter.Tk()
window = Window(root)
root.minsize(600,480)
root.mainloop()
