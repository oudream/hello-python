# -*- coding:utf-8 -*-
# file: TkinterButton.py
#
import Tkinter							# 导入Tkinter模块
root = Tkinter.Tk()
button1 = Tkinter.Button(root, 			
			anchor = Tkinter.E,			# 指定文本对齐方式
			text = 'Button1',			# 指定按钮上的文本
			width = 40,				# 指定按钮的宽度，相当于40个字符
			height = 5)				# 指定按钮的高度，相当于5行字符
button1.pack()							# 将按钮添加到窗口
button2 = Tkinter.Button(root, 			
			text = 'Button2',	
			bg = 'blue')				# 指定按钮的背景色
button2.pack()
button3 = Tkinter.Button(root, 			
			text = 'Button3',	
			width = 14,				# 指定按钮的宽度
			height = 1)				# 指定按钮的高度
button3.pack()
button4 = Tkinter.Button(root, 			
			text = 'Button4',	
			width = 60,		
			height = 5,		
			state = Tkinter.DISABLED)		# 指定按钮为禁用状态
button4.pack()
root.mainloop()							# 进入消息循环
