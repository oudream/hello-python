# -*- coding:utf-8 -*-
# file: pysmtp.py
#
import smtplib
import Tkinter
class Window:
	def __init__(self, root):								# 创建组件
		label1 = Tkinter.Label(root, text = 'SMTP')
		label2 = Tkinter.Label(root, text = 'Port')
		label3 = Tkinter.Label(root, text = '用户名')
		label4 = Tkinter.Label(root, text = '密码')
		label5 = Tkinter.Label(root, text = '收件人')
		label6 = Tkinter.Label(root, text = '主题')
		label7 = Tkinter.Label(root, text = '发件人')
		label1.place(x = 5, y = 5)
		label2.place(x = 5, y = 30)
		label3.place(x = 5, y = 55)
		label4.place(x = 5, y = 80)
		label5.place(x = 5, y = 105)
		label6.place(x = 5, y = 130)
		label7.place(x = 5, y = 155)
		self.entryPOP = Tkinter.Entry(root)
		self.entryPort = Tkinter.Entry(root)
		self.entryUser = Tkinter.Entry(root)
		self.entryPass = Tkinter.Entry(root, show = '*')
		self.entryTo = Tkinter.Entry(root)
		self.entrySub = Tkinter.Entry(root)
		self.entryFrom = Tkinter.Entry(root)
		self.entryPort.insert(Tkinter.END, '25')
		self.entryPOP.place(x = 50, y = 5)
		self.entryPort.place(x = 50, y = 30)
		self.entryUser.place(x = 50, y = 55)
		self.entryPass.place(x = 50, y = 80)
		self.entryTo.place(x = 50, y = 105)
		self.entrySub.place(x = 50, y = 130)
		self.entryFrom.place(x = 50, y = 155)
		self.get = Tkinter.Button(root, text = '发送邮件', command = self.Get)
		self.get.place(x = 60, y = 180)
		self.text = Tkinter.Text(root)
		self.text.place(y=200)
	def Get(self):										# 按钮事件
		try:										# 异常处理
			host = self.entryPOP.get()						# 获取服务器地址
			port = int(self.entryPort.get())					# 获取端口
			user = self.entryUser.get()						# 获取用户名
			pw = self.entryPass.get()						# 获取密码
			fromaddr = self.entryFrom.get()						# 获取发件人
			toaddr = self.entryTo.get()						# 获取收件人
			subject = self.entrySub.get()						# 获取主题
			text = self.text.get(1.0, Tkinter.END)					# 获取邮件内容
			msg = ("From: %s\nTo: %s\nSubject: %s\n\n"				# 生成邮件头
       				% (fromaddr, toaddr, subject))
			msg = msg + text
			smtp = smtplib.SMTP(host,port)						# 连接服务器
			smtp.set_debuglevel(1)							# 设置调试级别
			smtp.login(user,pw)							# 登录服务器
			smtp.sendmail(fromaddr, toaddr, msg)					# 发送邮件
			smtp.quit()								# 断开服务器
		except :
			self.text.insert(Tkinter.END, '发送错误\n')
root = Tkinter.Tk()
window = Window(root)
root.minsize(600,480)
root.mainloop()
