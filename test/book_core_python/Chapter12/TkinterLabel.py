# -*- coding:utf-8 -*-
# file: TkinterLabel.py
#
import Tkinter								# 导入Tkinter模块
root = Tkinter.Tk()
label1 = Tkinter.Label(root,
			anchor = Tkinter.E,				# 设置文本的位置
			bg = 'blue',					# 设置标签背景色
			fg = 'red',					# 设置标签前景色
			text = 'Python',				# 设置标签中的文本
			width = 30,					# 设置标签的宽度为30
			height = 5)					# 设置标签的的高度为5
label1.pack()
label2 = Tkinter.Label(root,
			text = 'Python GUI\nTkinter',			# 设置标签中的文本，在字符串中使用换行符
			justify = Tkinter.LEFT,				# 设置多行文本为左对齐
			width = 30,
			height = 5)
label2.pack()
label3 = Tkinter.Label(root,
			text = 'Python GUI\nTkinter',
			justify = Tkinter.RIGHT,			# 设置多行文本为右对齐
			width = 30,
			height = 5)
label3.pack()
label4 = Tkinter.Label(root,
			text = 'Python GUI\nTkinter',
			justify = Tkinter.CENTER,			# 设置多行文本为剧中对齐
			width = 30,
			height = 5)
label4.pack()
root.mainloop()
