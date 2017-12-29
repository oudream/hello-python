# -*- coding:utf-8 -*-
# file: TkinterRCButton.py
#
import Tkinter							# 导入Tkinter模块
root = Tkinter.Tk()
r = Tkinter.StringVar()						# 使用StringVar生成字符串变量用于单选框组件
r.set('1')							# 初始化变量值
radio = Tkinter.Radiobutton(root,				# 生成单选框组件
			variable = r, 				# 设置单选框关联的变量
			value = '1',				# 设置选中单选框时其所关联的变量的值，即r的值
			indicatoron = 0,			# 将单选框绘制成按钮样式
			text = 'Radio1')			# 设置单选框显示的文本
radio.pack()
radio = Tkinter.Radiobutton(root,
			variable = r,
			value = '2',				# 当选中该单选框时r的值为2
			indicatoron = 0,
			text = 'Radio2' )
radio.pack()
radio = Tkinter.Radiobutton(root,
			variable = r,
			value = '3',				# 当选中该单选框时r的值为3
			indicatoron = 0,
			text = 'Radio3' )
radio.pack()
radio = Tkinter.Radiobutton(root,
			variable = r,
			value = '4',				# 当选中该单选框时r的值为4
			indicatoron = 0,
			text = 'Radio4' )
radio.pack()
c = Tkinter.IntVar()						# 使用IntVar生成整型变量用于复选框
c.set(1)
check = Tkinter.Checkbutton(root,
			text = 'Checkbutton',			# 设置复选框的文本
			variable = c,				# 设置复选框关联的变量
			indicatoron = 0,			# 将复选框绘制成按钮样式
			onvalue = 1,				# 当选中复选框时，c的值为1
			offvalue = 2)				# 当未选中复选框时，c的值为2
check.pack()
root.mainloop()
