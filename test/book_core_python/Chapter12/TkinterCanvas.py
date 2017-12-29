# -*- coding:utf-8 -*-
# file: TkinterCanvas.py
#
import Tkinter								# 导入Tkinter模块
root = Tkinter.Tk()
canvas = Tkinter.Canvas(root,
			width = 600,					# 指定Canvas组件的宽度
			height = 480,					# 指定Canvas组件的高度
			bg = 'white')					# 指定Canvas组件的背景色
im = Tkinter.PhotoImage(file='python.gif')				# 使用PhotoImage打开图片
canvas.create_image(300,50,image = im)					# 使用create_image将图片添加到Canvas组件中
canvas.create_text(302,77,						# 使用create_text方法在坐标（302，77）处绘制文字
		text = 'Use Canvas'					# 所绘制文字的内容
		,fill = 'gray')						# 所绘制文字的颜色为灰色
canvas.create_text(300,75,
		text = 'Use Canvas',
		fill = 'blue')
canvas.create_polygon(290,114,316,114,330,130,				# 使用create_polygon方法绘制六边形
		      310,146,284,146,270,130)
canvas.create_oval(280,120,320,140,					# 使用create_oval方法绘制椭圆
		fill = 'white')						# 设置椭圆用白色填充
canvas.create_line(250,130,350,130)					# 使用create_line绘制一条从（250,130）到（350,130）的直线
canvas.create_line(300,100,300,160)
canvas.create_rectangle(90,190,510,410,					# 使用create_rectangle绘制一个矩形
		width=5)						# 设置矩形线宽为5个像素
canvas.create_arc(100, 200, 500, 400, 					# 使用create_arc绘制圆弧
		start=0, extent=240, 					# 设置圆弧的起止角度
		fill="pink")						# 设置圆弧填充颜色
canvas.create_arc(103,203,500,400, 
		start=241, extent=118, 
		fill="red")
canvas.pack()								# 将Canvas添加到主窗口
root.mainloop()

