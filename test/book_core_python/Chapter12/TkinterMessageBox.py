# -*- coding:utf-8 -*-
# file: TkinterMessageBox.py
#
import Tkinter										# 导入Tkinter模块
import tkMessageBox									# 导入tkMessageBox模块
def cmd():										# 按钮消息处理函数
	global n									# 使用全局变量n
	global buttontext								# 使用全局变量buttontext
	n = n + 1
	if n == 1:									# 判断n的值，显示不同的消息框
		tkMessageBox.askokcancel('Python Tkinter','askokcancel')		# 使用askokcancel函数
		buttontext.set('skquestion')						# 更改按钮上的文字
	elif n == 2:
		tkMessageBox.askquestion('Python Tkinter','skquestion')			# 使用askquestion函数
		buttontext.set('askyesno')
	elif n == 3:
		tkMessageBox.askyesno('Python Tkinter','askyesno')			# 使用askyesno函数
		buttontext.set('showerror')
	elif n == 4:
		tkMessageBox.showerror('Python Tkinter','showerror')			# 使用showerror函数
		buttontext.set('showinfo')
	elif n == 5:
		tkMessageBox.showinfo('Python Tkinter','showinfo')			# 使用showinfo函数
		buttontext.set('showwarning')
	else :
		n = 0									# 将n赋值为0重新开始循环
		tkMessageBox.showwarning('Python Tkinter','showwarning')		# 使用showwarning函数
		buttontext.set('askokcancel')
n = 0											# 为n赋初始值
root = Tkinter.Tk()
buttontext = Tkinter.StringVar()							# 生成关联按钮文字的变量
buttontext.set('askokcancel')								# 设置buttontext值
button = Tkinter.Button(root,								# 生成按钮
		textvariable = buttontext,						# 设置关联变量
		command = cmd)								# 设置事件处理函数
button.pack()
root.mainloop()										# 进入消息循环
