# -*- coding:utf-8 -*-
# file: pyImageConv.py
#
import os										# 导入模块
import Image
import Tkinter
import tkFileDialog
import tkMessageBox
class Window:										# 创建窗口
	def __init__(self):
		self.root = root = Tkinter.Tk()						# 创建组件
		label = Tkinter.Label(root, text = '选择目录')
		label.place(x = 5, y = 5)
		self.entry = Tkinter.Entry(root)
		self.entry.place(x=55, y = 5)
		self.buttonBrowser = Tkinter.Button(root, text = '浏览',
				command = self.Browser)
		self.buttonBrowser.place(x=200, y = 5)
		frameF = Tkinter.Frame(root)
		frameF.place(x = 5, y = 30)
		frameT = Tkinter.Frame(root)
		frameT.place(x = 100, y = 30)
		self.fImage = Tkinter.StringVar()					# 生成关联变量
		self.tImage = Tkinter.StringVar()
		self.status = Tkinter.StringVar()
		self.fImage.set('.bmp')
		self.tImage.set('.bmp')
		labelFrom = Tkinter.Label(frameF, text = 'From')
		labelFrom.pack(anchor='w')
		labelTo = Tkinter.Label(frameT, text = 'To')
		labelTo.pack(anchor='w')
		frBmp = Tkinter.Radiobutton(frameF, variable = self.fImage, 
				value = '.bmp', text = 'BMP' )
		frBmp.pack(anchor='w')
		frJpg = Tkinter.Radiobutton(frameF, variable = self.fImage, 
				value = '.jpg', text = 'JPG' )
		frJpg.pack(anchor='w')
		frGif = Tkinter.Radiobutton(frameF, variable = self.fImage, 
				value = '.gif', text = 'GIF' )
		frGif.pack(anchor='w')
		frPng = Tkinter.Radiobutton(frameF, variable = self.fImage, 
				value = '.png', text = 'PNG' )
		frPng.pack(anchor='w')
		trBmp = Tkinter.Radiobutton(frameT, variable = self.tImage, 
				value = '.bmp', text = 'BMP' )
		trBmp.pack(anchor='w')
		trJpg = Tkinter.Radiobutton(frameT, variable = self.tImage, 
				value = '.jpg', text = 'JPG' )
		trJpg.pack(anchor='w')
		trGif = Tkinter.Radiobutton(frameT, variable = self.tImage, 
				value = '.gif', text = 'GIF' )
		trGif.pack(anchor='w')
		trPng = Tkinter.Radiobutton(frameT, variable = self.tImage, 
				value = '.png', text = 'PNG' )
		trPng.pack(anchor='w')
		self.buttonConv = Tkinter.Button(root, text = '转换',
				command = self.Conv)
		self.buttonConv.place(x=100, y = 150)
		self.labelStatus = Tkinter.Label(root,textvariable=self.status)
		self.labelStatus.place(x=50, y = 175)
	def MainLoop(self):									# 进入消息循环
		self.root.minsize(250,200)
		self.root.maxsize(250,200)
		self.root.mainloop()
	def Browser(self):									# 浏览目录
		directory = tkFileDialog.askdirectory(title='Python')
		if directory:
			self.entry.delete(0, Tkinter.END)
			self.entry.insert(Tkinter.END, directory)
	def Conv(self):										# 转换文件格式
		n = 0
		t = self.tImage.get()
		f = self.fImage.get()
		path = self.entry.get()
		if path == '':
			tkMessageBox.showerror('Python Tkinter','请输入路径')
			return
		filenames = os.listdir(path)
		os.mkdir(path + '/' + t[-3:])
		for filename in filenames:
			if filename[-4:] == f:
		       		Image.open(path + '/' +filename).save(path +
						'/' + t[-3:] + '/' + filename[:-4] + t)
				n = n + 1
		self.status.set('成功转换%d张图片' % n)
window = Window()
window.MainLoop()
