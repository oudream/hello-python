# -*- coding:utf-8 -*-
# file: TkinterDraw.py
#
import Tkinter											# 导入Tkinter模块
class MyButton:											# 定义按钮类
	def __init__(self,root,canvas,label,type):						# 类初始化
		self.root = root								# 保存引用值
		self.canvas = canvas
		self.label = label
		if type == 0:									# 根据类型创建按钮
			button = Tkinter.Button(root,text = 'DrawLine',
					command = self.DrawLine)
		elif type == 1:
			button = Tkinter.Button(root,text = 'DrawArc',
					command = self.DrawArc)
		elif type == 2:
			button = Tkinter.Button(root,text = 'DrawRec',
					command = self.DrawRec)
		else :
			button = Tkinter.Button(root,text = 'DrawOval',
					command = self.DrawOval)
		button.pack(side = 'left')
	def DrawLine(self):									# DrawLine按钮事件处理函数
		self.label.text.set('Draw Line')
		self.canvas.SetStatus(0)
	def DrawArc(self):									# DrawArc按钮事件处理函数
		self.label.text.set('Draw Arc')
		self.canvas.SetStatus(1)
	def DrawRec(self):									# DrawRec按钮事件处理函数
		self.label.text.set('Draw Rectangle')
		self.canvas.SetStatus(2)
	def DrawOval(self):									# DrawOval按钮事件处理函数
		self.label.text.set('Draw Oval')
		self.canvas.SetStatus(3)
class MyCanvas:											# 定义Canvas类
	def __init__(self,root):
		self.status = 0									# 保存引用值
		self.draw = 0
		self.root = root
		self.canvas = Tkinter.Canvas(root,bg = 'white',					# 生成Canvas组件
				width = 600,
				height = 480)
		self.canvas.pack()
		self.canvas.bind('<ButtonRelease-1>',self.Draw)					# 绑定事件到左键
		self.canvas.bind('<Button-2>',self.Exit)					# 绑定事件到中键
		self.canvas.bind('<Button-3>',self.Del)						# 绑定事件到右键
		self.canvas.bind_all('<Delete>',self.Del)					# 绑定事件到Delete键
		self.canvas.bind_all('<KeyPress-d>',self.Del)					# 绑定事件到d键
		self.canvas.bind_all('<KeyPress-e>',self.Exit)					# 绑定事件到e键
	def Draw(self,event):									# 绘图事件处理函数
		if self.draw == 0: 								# 判断是否绘图
			self.x = event.x
			self.y = event.y
			self.draw = 1
		else:										# 根据self.status绘制不同图形
			if self.status == 0:
				self.canvas.create_line(self.x,self.y,
						event.x,event.y)
				self.draw = 0
			elif self.status == 1:
				self.canvas.create_arc(self.x,self.y,
						event.x,event.y)
				self.draw = 0
			elif self.status == 2:
				self.canvas.create_rectangle(self.x,self.y,
						event.x,event.y)
				self.draw = 0
			else:
				self.canvas.create_oval(self.x,self.y,
						event.x,event.y)
				self.draw = 0
	def Del(self,event):									# 当按下右键或d键则删除图形
		items = self.canvas.find_all()
		for item in items:
			self.canvas.delete(item)
	def Exit(self,event):									# 当按下中键或e键则退出
		self.root.quit()
	def SetStatus(self,status):								# 设置绘制的图形
		self.status = status
class MyLabel:											# 定义标签类
	def __init__(self,root):								# 类初始化
		self.root = root								# 保存引用
		self.canvas = canvas
		self.text = Tkinter.StringVar()							# 生成标签引用变量
		self.text.set('Draw Line')
		self.label = Tkinter.Label(root,textvariable = self.text,			# 生成标签
				fg = 'red',width = 50)
		self.label.pack(side = 'left')
root = Tkinter.Tk()										# 生成主窗口
canvas = MyCanvas(root)										# 生成绘图组件
label = MyLabel(root)										# 生成标签
MyButton(root,canvas,label,0)									# 生成按钮
MyButton(root,canvas,label,1)
MyButton(root,canvas,label,2)
MyButton(root,canvas,label,3)
root.mainloop()											# 进入消息循环
