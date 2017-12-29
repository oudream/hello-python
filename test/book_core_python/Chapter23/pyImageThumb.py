# -*- coding:utf-8 -*-
# file: pyImageThumb.py
#
import os										# 导入模块
import Image
import Tkinter
import tkFileDialog
import tkMessageBox
class Window:
	def __init__(self):
		self.root = root = Tkinter.Tk()						# 创建窗口
		self.Image = Tkinter.StringVar()
		self.status = Tkinter.StringVar()
		self.mstatus = Tkinter.IntVar()
		self.fstatus = Tkinter.IntVar()
		self.Image.set('bmp')
		self.mstatus.set(0)
		self.fstatus.set(0)
		label = Tkinter.Label(root, text = '输入百分比')
		label.place(x = 5, y = 5)
		self.entryNew = Tkinter.Entry(root)
		self.entryNew.place(x = 65, y = 5)
		self.checkM = Tkinter.Checkbutton(root, text ='批量转换',
				command = self.OnCheckM,
				variable = self.mstatus,
				onvalue = 1,
				offvalue = 0)
		self.checkM.place(x = 5, y = 30)
		label = Tkinter.Label(root, text = '选择文件')
		label.place(x = 5, y = 55)
		self.entryFile = Tkinter.Entry(root)
		self.entryFile.place(x=55, y = 55)
		self.buttonBrowserFile = Tkinter.Button(root, text = '浏览',
				command = self.BrowserFile)
		self.buttonBrowserFile.place(x=200, y = 55)
		label = Tkinter.Label(root, text = '选择目录')
		label.place(x = 5, y = 80)
		self.entryDir = Tkinter.Entry(root,
				state = Tkinter.DISABLED)
		self.entryDir.place(x=55, y = 80)
		self.buttonBrowserDir = Tkinter.Button(root, text = '浏览',
				command = self.BrowserDir,
				state = Tkinter.DISABLED)
		self.buttonBrowserDir.place(x=200, y = 80)

		self.checkF = Tkinter.Checkbutton(root, text ='改变文件格式',
				command = self.OnCheckF,
				variable = self.fstatus,
				onvalue = 1,
				offvalue = 0)
		self.checkF.place(x = 5, y = 110)
		frame = Tkinter.Frame(root)
		frame.place(x = 10, y = 130)
		labelTo = Tkinter.Label(frame, text = 'To')
		labelTo.pack(anchor='w')
		self.rBmp = Tkinter.Radiobutton(frame, variable = self.Image, 
				value = 'bmp', text = 'BMP',
				state = Tkinter.DISABLED)
		self.rBmp.pack(anchor='w')
		self.rJpg = Tkinter.Radiobutton(frame, variable = self.Image, 
				value = 'jpg', text = 'JPG',
				state = Tkinter.DISABLED)
		self.rJpg.pack(anchor='w')
		self.rGif = Tkinter.Radiobutton(frame, variable = self.Image, 
				value = 'gif', text = 'GIF',
				state = Tkinter.DISABLED)
		self.rGif.pack(anchor='w')
		self.rPng = Tkinter.Radiobutton(frame, variable = self.Image, 
				value = 'png', text = 'PNG',
				state = Tkinter.DISABLED) 
		self.rPng.pack(anchor='w')
		self.buttonConv = Tkinter.Button(root, text = '转换',
				command = self.Conv)
		self.buttonConv.place(x=100, y = 175)
		self.labelStatus = Tkinter.Label(root,textvariable=self.status)
		self.labelStatus.place(x=80, y = 205)
	def MainLoop(self):									# 进入消息循环
		self.root.minsize(250,250)
		self.root.maxsize(250,250)
		self.root.mainloop()
	def BrowserDir(self):									# 选择路径
		directory = tkFileDialog.askdirectory(title='Python')
		if directory:
			self.entryDir.delete(0, Tkinter.END)
			self.entryDir.insert(Tkinter.END, directory)
	def BrowserFile(self):									# 选择文件
		file = tkFileDialog.askopenfilename(title = 'Python Music Player',
			filetypes=[('JPG', '*.jpg'), ('BMP', '*.bmp'),
				('GIF', '*.gif'), ('PNG', '*.png')])
		if file:
			self.entryFile.delete(0, Tkinter.END)
			self.entryFile.insert(Tkinter.END, file)
	def OnCheckM(self):									# 设置组件状态
		if not self.mstatus.get():
			self.entryDir.config(state = Tkinter.DISABLED)
			self.entryFile.config(state = Tkinter.NORMAL)
			self.buttonBrowserDir.config(state = Tkinter.DISABLED)
			self.buttonBrowserFile.config(state = Tkinter.NORMAL)
		else:
			self.entryDir.config(state = Tkinter.NORMAL)
			self.entryFile.config(state = Tkinter.DISABLED)
			self.buttonBrowserDir.config(state = Tkinter.NORMAL)
			self.buttonBrowserFile.config(state = Tkinter.DISABLED)
	def OnCheckF(self):									# 设置组件状态
		if not self.fstatus.get():
			self.rBmp.config(state = Tkinter.DISABLED)
			self.rJpg.config(state = Tkinter.DISABLED)
			self.rGif.config(state = Tkinter.DISABLED)
			self.rPng.config(state = Tkinter.DISABLED)
		else:
			self.rBmp.config(state = Tkinter.NORMAL)
			self.rJpg.config(state = Tkinter.NORMAL)
			self.rGif.config(state = Tkinter.NORMAL)
			self.rPng.config(state = Tkinter.NORMAL)
	def Conv(self):										# 转换图片
		n = 0
		if self.mstatus.get():
			path = self.entryDir.get()
			if path == '':
				tkMessageBox.showerror('Python Tkinter','请输入路径')
				return
			filenames = os.listdir(path)
			if self.fstatus.get():
				f = self.Image.get()
				for filename in filenames:
					if filename[-3:] in ('bmp','jpg','gif','png'):
			       			self.make(path + '/' + filename, f)
						n = n + 1
			else:
				for filename in filenames:
					if filename[-3:] in ('bmp','jpg','gif','png'):
			       			self.make(path + '/' + filename)
						n = n + 1
		else:
			file = self.entryFile.get()
			if file == '':
				tkMessageBox.showerror('Python Tkinter','请选择文件')
				return
			if self.fstatus.get():
				f = self.Image.get()
				self.make(file, f)
				n = n + 1
			else:
				self.make(file)
				n = n + 1
		self.status.set('成功转换%d图片' % n)
	def make(self, file, format = None):							# 生成缩略图
		im = Image.open(file)
    		mode = im.mode
   		if mode not in ('L', 'RGB'):
			im = im.convert('RGB')
		width, height = im.size
		s = self.entryNew.get()
		if s == '':
			tkMessageBox.showerror('Python Tkinter','请输入百分比')
			return
		else:
			n = int(s)
		nwidth = width * n / 100
		nheight = height * n / 100
		thumb = im.resize((nwidth,nheight), Image.ANTIALIAS)
		if format:
			thumb.save(file[:(len(file) - 4)] + '_thumb.' + format)
		else:
			thumb.save(file[:(len(file) - 4)] + '_thumb' + file[-4:])
window = Window()
window.MainLoop()
