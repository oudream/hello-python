# -*- coding:utf-8 -*-
# file: wxPythonButtonEvent.py
#
import wx											# 导入wxPython
class MyApp(wx.App):										# 通过继承创建类
	def OnInit(self):									# 重载OnInit方法
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,170))		# 生成框架窗口
		panel = wx.Panel(frame, -1)							# 生成面板
		self.button1 = wx.Button(panel, -1, 'Button1', pos=(50, 50))			# 添加Button1
		self.Bind(wx.EVT_BUTTON, 							# 绑定按钮事件
			self.OnButton1, 							# 指定事件响应函数
			self.button1)								# 指定按钮
		self.button2 = wx.Button(panel, -1, 'Button2',pos = (150,50))
		self.Bind(wx.EVT_BUTTON,							# 绑定按钮事件 
			self.OnButton2,                                                         # 指定事件响应函数
			self.button2)								# 指定按钮
		self.button1.SetDefault()							# 将Button1设置为默认按钮
		frame.Show()									# 显示窗口
		return True
	def OnButton1(self, event):								# 按钮事件响应函数
		self.button2.SetLabel('Button1')						# 更改Button2的文字
		self.button2.SetDefault()							# 将Button2设置为默认按钮
		self.button1.SetLabel('Button2')						# 更改Button1的文字
	def OnButton2(self, event):								# 按钮事件响应函数
		self.button1.SetLabel('Button1')						# 更改Button1的文字
		self.button1.SetDefault()							# 将Button1设置为默认按钮
		self.button2.SetLabel('Button2')						# 更改Button2的文字
app = MyApp()
app.MainLoop()
