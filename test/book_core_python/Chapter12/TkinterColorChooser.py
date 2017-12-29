# -*- coding:utf-8 -*-
# file: TkinterColorChooser.py
#
import Tkinter										# 导入Tkinter模块
import tkColorChooser									# 导入tkColorChooser模块
def ChooseColor():									# 按钮事件处理函数
	r = tkColorChooser.askcolor(title = 'Python Tkinter')				# 创建颜色选择对话框
	print r										# 输出返回值
root = Tkinter.Tk()
button = Tkinter.Button(root,text = 'Choose Color',					# 创建按钮
		command = ChooseColor)							# 指定按钮事件处理函数
button.pack()
root.mainloop()										# 进入消息循环
