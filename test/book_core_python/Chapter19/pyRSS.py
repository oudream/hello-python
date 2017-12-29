# -*- coding:utf-8 -*-
# file: pyRSS.py
#
import Tkinter
import urllib
import xml.parsers.expat
class MyXML:									# XML解析类
	def __init__(self, edit):
		self.parser = xml.parsers.expat.ParserCreate()			# 生成XMLParser
		self.parser.StartElementHandler = self.start			# 起始标记处理方法
		self.parser.EndElementHandler = self.end			# 结束标记处理方法
		self.parser.CharacterDataHandler = self.data			# 字符数据处理方法
		self.title = False						# 状态标志
		self.date = False
		self.edit = edit						# 多行文本框对象
	def start(self, name, attrs):						# 起始标记处理方法
		if name == 'title':						# 判断是否为title元素
			self.title = True					# 标志设为真
		elif name == 'pubDate':						# 判断是否为pubDate
			self.date = True					# 标志设为真
		else:
			pass
	def end(self, name):							# 结束标记处理
		if name == 'title':
			self.title = False					# 标志设为假
		elif name == 'pubDate':
			self.date = False					# 标志设为假
		else:
			pass
	def data(self,data):							# 字符数据处理方法
		if self.title:							# 根据标志状态输出数据
			self.edit.insert(Tkinter.END,
					'******************************\n')
			self.edit.insert(Tkinter.END, 'Title: ')
			self.edit.insert(Tkinter.END, data + '\n')
		elif self.date:
			self.edit.insert(Tkinter.END, 'Date: ')
			self.edit.insert(Tkinter.END, data + '\n')
		else:
			pass
	def feed(self, data):
		self.parser.Parse(data, 0)
class Window:
	def __init__(self, root):
		self.root = root							# 创建组件
		self.get = Tkinter.Button(root,
				text = '获取RSS', command = self.Get)
		self.get.place(x = 280, y = 15)
		self.frame = Tkinter.Frame(root, bd=2)
		self.scrollbar = Tkinter.Scrollbar(self.frame)
		self.edit = Tkinter.Text(self.frame,yscrollcommand = self.scrollbar.set,
				width = 96, height = 32)
		self.scrollbar.config(command=self.edit.yview)
		self.edit.pack(side = Tkinter.LEFT)
		self.scrollbar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
		self.frame.place(y = 50)
	def Get(self):
		url = 'http://www.python.org/channews.rdf'
		page = urllib.urlopen(url)						# 打开URL
		data = page.read()							# 读取URL内容
		parser = MyXML(self.edit)						# 生成实例对象
		parser.feed(data)							# 处理XML数据
root = Tkinter.Tk()
window = Window(root)
root.minsize(600,480)
root.maxsize(600,480)
root.mainloop()
