# -*- coding:utf-8 -*-
# file: pypop.py
#
import poplib
import re
import Tkinter
class Window:
	def __init__(self, root):								# 创建组件
		label1 = Tkinter.Label(root, text = 'POP3')
		label2 = Tkinter.Label(root, text = 'Port')
		label3 = Tkinter.Label(root, text = '用户名')
		label4 = Tkinter.Label(root, text = '密码')
		label1.place(x = 5, y = 5)
		label2.place(x = 5, y = 30)
		label3.place(x = 5, y = 55)
		label4.place(x = 5, y = 80)
		self.entryPOP = Tkinter.Entry(root)
		self.entryPort = Tkinter.Entry(root)
		self.entryUser = Tkinter.Entry(root)
		self.entryPass = Tkinter.Entry(root, show = '*')
		self.entryPort.insert(Tkinter.END, '110')
		self.entryPOP.place(x = 40, y = 5)
		self.entryPort.place(x = 40, y = 30)
		self.entryUser.place(x = 40, y = 55)
		self.entryPass.place(x = 40, y = 80)
		self.get = Tkinter.Button(root, text = '收取邮件', command = self.Get)
		self.get.place(x = 60, y = 120)
		self.text = Tkinter.Text(root)
		self.text.place(y=150)
	def Get(self):										# 按钮事件
		try:										# 异常处理
			host = self.entryPOP.get()						# 获取服务器地址
			port = int(self.entryPort.get())					# 获取端口
			user = self.entryUser.get()						# 获取用户名
			pw = self.entryPass.get()						# 获取密码
			pop = poplib.POP3(host)							# 创建POP3实例
    			pop.user(user)								# 登录服务器
			pop.pass_(pw)
			stat = pop.stat()							# 获取状态
			self.text.insert(Tkinter.END, 						# 输出状态
					'Status: %d message(s), %d bytes\n' % stat)
			rx_headers  = re.compile(r"^(From|To|Subject)")				# 编译正则表达
			for n in range(stat[0]):
			        response, lines, bytes = pop.top(n + 1, 10)			# 收取邮件的前10行
				self.text.insert(Tkinter.END, 
						"Message %d (%d bytes)\n" % (n+1, bytes))
        			self.text.insert(Tkinter.END, "-" * 30 + '\n')
       				self.text.insert(Tkinter.END, 					# 输出匹配到的内容
						"\n".join(filter(rx_headers.match, lines)))
				self.text.insert(Tkinter.END, '\n')
       				self.text.insert(Tkinter.END, "-" * 30  + '\n')
		except :
			self.text.insert(Tkinter.END, '接受错误\n')
root = Tkinter.Tk()
window = Window(root)
root.mainloop()
