# -*- coding:utf-8 -*-
# file: httpurl.py
#
import Tkinter
import urllib
class Window:
	def __init__(self, root):
		self.root = root
		self.entryUrl = Tkinter.Entry(root) 					# 创建组件
		self.entryUrl.place(x = 5, y = 15)
		self.get = Tkinter.Button(root, 
				text = '下载页面', command = self.Get)
		self.get.place(x = 120, y = 15)
		self.edit = Tkinter.Text(root)
		self.edit.place(y = 50)
	def Get(self):
		url = self.entryUrl.get()						# 获取URL
		page = urllib.urlopen(url)						# 打开URL
		data = page.read()							# 读取URL内容
		self.edit.insert(Tkinter.END, data)					# 将内容输出到文本框
		page.close()
root = Tkinter.Tk()
window = Window(root)
root.minsize(600,480)
root.mainloop()

