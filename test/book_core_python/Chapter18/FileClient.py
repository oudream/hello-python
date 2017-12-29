# -*- coding:utf-8 -*-
# file: FileClient.py
#
import Tkinter
import tkFileDialog
import socket
import os
class Window:
	def __init__(self, root):								# 创建组件
		label1 = Tkinter.Label(root, text = 'IP')
		label2 = Tkinter.Label(root, text = 'Port')
		label3 = Tkinter.Label(root, text = '文件')
		label1.place(x = 5, y = 5)
		label2.place(x = 5, y = 30)
		label3.place(x = 5, y = 55)
		self.entryIP = Tkinter.Entry(root)
		self.entryIP.insert(Tkinter.END, '127.0.0.1')
		self.entryPort = Tkinter.Entry(root)
		self.entryPort.insert(Tkinter.END, '1051')
		self.entryData = Tkinter.Entry(root)
		self.entryData.insert(Tkinter.END, 'hello')
		self.entryIP.place(x = 40, y = 5)
		self.entryPort.place(x = 40, y = 30)
		self.entryData.place(x = 40, y = 55)
		self.send = Tkinter.Button(root, text = '发送文件', command = self.Send)
		self.openfile = Tkinter.Button(root, text = '浏览', command = self.Openfile)
		self.send.place(x = 40, y = 80)
		self.openfile.place( x = 170, y = 55)
	def Send(self):										# 按钮事件
		try:										# 异常处理
			ip = self.entryIP.get()							# 获取IP
			port = int(self.entryPort.get())					# 获取端口
			filename = self.entryData.get()						# 获取发送数据
			tt = filename.split('/')
			name = tt[len(tt)-1]
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		# 创建socket对象
			client.connect((ip,port))						# 连接服务端
			client.send(name)							# 发送数据
			file = os.open(filename, os.O_RDONLY | os.O_EXCL|os.O_BINARY)		# 打开文件
			while 1:								# 发送文件
				data = os.read(file,1024)
				if not data:
					break
				client.send(data)
			os.close(file)								# 关闭文件
			client.close()								# 关闭连接
		except :
			print '发送错误'
	def Openfile(self):
		r = tkFileDialog.askopenfilename(title = 'Python Tkinter',			# 创建打开文件对话框
			filetypes=[('All files', '*'),('Python', '*.py *.pyw')])
		if r:
			self.entryData.delete(0, Tkinter.END)
			self.entryData.insert(Tkinter.END, r)
		
root = Tkinter.Tk()
window = Window(root)
root.mainloop()

