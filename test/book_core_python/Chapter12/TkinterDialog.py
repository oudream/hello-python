# -*- coding:utf-8 -*-
# file: TkinterDialog.py
#
import Tkinter										# 导入Tkinter模块
import tkMessageBox									# 导入tkMesageBox模块
class MyDialog:										# 定义对话框类
   	def __init__(self, root):							# 对话框初始化
        	self.top = Tkinter.Toplevel(root)					# 生成Toplevel组件
		label = Tkinter.Label(self.top, text='Please Input')			# 生成标签组件
		label.pack()
        	self.entry = Tkinter.Entry(self.top)					# 生成文本框组件
        	self.entry.pack()
		self.entry.focus()							# 让文本框获得焦点
        	button = Tkinter.Button(self.top, text='Ok', 				# 生成按钮
				command=self.Ok)					# 设置按钮事件处理函数
		button.pack()
	def Ok(self):									# 定义按钮事件处理函数
		self.input = self.entry.get()						# 获取文本框中内容，保存为input
        	self.top.destroy()							# 销毁对话框
	def get(self):									# 返回在文本框输入的内容
		return self.input
class MyButton():									# 定义按钮类
	def __init__(self, root, type):							# 按钮初始化
		self.root = root							# 保存父窗口引用
		if type == 0:								# 根据类型创建不同按钮
			self.button = Tkinter.Button(root, 
					text='Create',
					command = self.Create)				# 设置Create按钮的事件处理函数
		else:
			self.button = Tkinter.Button(root, 
					text='Quit',
					command = self.Quit)				# 设置Quit按钮的事件处理函数
		self.button.pack()
	def Create(self):								# Create按钮的事件处理函数
		d = MyDialog(self.root)							# 生成对话框
		self.button.wait_window(d.top)						# 等待对话框结束
		tkMessageBox.showinfo('Python','You input:\n' + d.get())		# 获取对话框中输入值，并输出
	def Quit(self):									# Quit按钮的事件处理函数
		self.root.quit()							# 退出主窗口
root = Tkinter.Tk()									# 生成主窗口
MyButton(root,0)									# 生成Create按钮
MyButton(root,1)									# 生成Quit按钮
root.mainloop()										# 进入消息循环
