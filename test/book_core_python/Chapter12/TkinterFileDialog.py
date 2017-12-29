# -*- coding:utf-8 -*-
# file: TkinterFileDialog.py
#
import Tkinter										# 导入Tkinter模块
import tkFileDialog									# 导入tkFileDialog模块
def FileOpen():										# 按钮事件处理函数
	r = tkFileDialog.askopenfilename(title = 'Python Tkinter',			# 创建打开文件对话框
			filetypes=[('Python', '*.py *.pyw'),('All files', '*')]	)	# 指定文件类型为Python脚本
	print r										# 输出返回值
def FileSave():										# 按钮事件处理函数
	r = tkFileDialog.asksaveasfilename(title = 'Python Tkinter',			# 创建保存文件对话框
			initialdir=r'E:\Python\code',					# 指定初始化目录
			initialfile = 'test.py')					# 指定初始化文件
	print r
root = Tkinter.Tk()
button1 = Tkinter.Button(root,text = 'File Open',					# 创建按钮
		command = FileOpen)							# 指定按钮事件处理函数
button1.pack(side='left')
button2 = Tkinter.Button(root,text = 'File Save',
		command = FileSave)							# 指定按钮事件处理函数
button2.pack(side='left')
root.mainloop()										# 进入消息循环

