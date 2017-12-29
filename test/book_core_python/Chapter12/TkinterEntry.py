# -*- coding:utf-8 -*-
# file: TkinterEntry.py
#
import Tkinter								# 导入Tkinter模块
root = Tkinter.Tk()
entry1 = Tkinter.Entry(root,						# 生成单行文本框组件
			show = '*',)					# 输入文本框中的字符被显示为“*”
entry1.pack()								# 将文本框添加到窗口中
entry2 = Tkinter.Entry(root,
			show = '#',					# 输入文本框中的字符被显示为“#”
			width = 50)					# 将文本框的宽度设置为50
entry2.pack()
entry3 = Tkinter.Entry(root,
			bg = 'red',					# 将文本框的背景色设置为红色
			fg = 'blue')					# 将文本框的前景色设置为蓝色
entry3.pack()
entry4 = Tkinter.Entry(root,
			selectbackground = 'red',			# 将选中文本的背景色设置为红色
			selectforeground = 'gray')			# 将选中文本的前景色设置为灰色
entry4.pack()
entry5 = Tkinter.Entry(root,
			state = Tkinter.DISABLED)			# 将文本框设置为禁用
entry5.pack()
edit1 = Tkinter.Text(root,						# 生成多行文本框组件
			selectbackground = 'red',			# 将选中文本的背景色设置为红色
			selectforeground = 'gray')			# 将选中文本的前景色设置为灰色
edit1.pack()
root.mainloop()								# 进入消息循环
