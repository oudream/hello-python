# -*- coding:utf-8 -*-
# file: TkinterSimpleDialog.py
#
import Tkinter										# 导入Tkinter模块
import tkSimpleDialog									# 导入tkSimpleDialog模块
def InStr():										# 按钮事件处理函数
	r = tkSimpleDialog.askstring('Python Tkinter',					# 创建字符串输入对话框
			'Input String',							# 指定提示字符
			initialvalue='Tkinter')						# 指定初始化文本
	print r										# 输出返回值
def InInt():										# 按钮事件处理函数
	r = tkSimpleDialog.askinteger('Python Tkinter','Input Integer')			# 创建整数输入对话框
	print r
def InFlo():										# 按钮事件处理函数
	r = tkSimpleDialog.askfloat('Python Tkinter','Input Float')			# 创建浮点数输入对话框
	print r
root = Tkinter.Tk()
button1 = Tkinter.Button(root,text = 'Input String',					# 创建按钮
		command = InStr)							# 指定按钮事件处理函数
button1.pack(side='left')
button2 = Tkinter.Button(root,text = 'Input Integer',
		command = InInt)							# 指定按钮事件处理函数
button2.pack(side='left')
button2 = Tkinter.Button(root,text = 'Input Float',
		command = InFlo)							# 指定按钮事件处理函数
button2.pack(side='left')
root.mainloop()										# 进入消息循环
