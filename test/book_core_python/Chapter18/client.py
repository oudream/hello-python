# -*- coding:utf-8 -*-
# file: client.py
#
import Tkinter
import socket
class Window:
	def __init__(self, root):								# 创建组件
		label1 = Tkinter.Label(root, text = 'IP')
		label2 = Tkinter.Label(root, text = 'Port')
		label3 = Tkinter.Label(root, text = 'Data')
		label1.place(x = 5, y = 5)
		label2.place(x = 5, y = 30)
		label3.place(x = 5, y = 55)
		self.entryIP = Tkinter.Entry(root)
		self.entryIP.insert(Tkinter.END, '127.0.0.1')
		self.entryPort = Tkinter.Entry(root)
		self.entryPort.insert(Tkinter.END, '1051')
		self.entryData = Tkinter.Entry(root)
		self.entryData.insert(Tkinter.END, 'hello')
		self.Recv = Tkinter.Text(root)
		self.entryIP.place(x = 40, y = 5)
		self.entryPort.place(x = 40, y = 30)
		self.entryData.place(x = 40, y = 55)
		self.Recv.place(y = 105)
		self.send = Tkinter.Button(root, text = '发送数据', command = self.Send)
		self.send.place(x = 40, y = 80)
	def Send(self):										# 按钮事件
		try:										# 异常处理
			ip = self.entryIP.get()							# 获取IP
			port = int(self.entryPort.get())					# 获取端口
			data = self.entryData.get()						# 获取发送数据
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		# 创建socket对象
			client.connect((ip,port))						# 连接服务端
			client.send(data)							# 发送数据
			rdata = client.recv(1024)						# 结束数据
			self.Recv.insert(Tkinter.END, 'Server:' + rdata+ '\n')			# 输出接受的数据
			client.close()								# 关闭连接
		except :
			self.Recv.insert(Tkinter.END, '发送错误\n')
root = Tkinter.Tk()
window = Window(root)
root.mainloop()
