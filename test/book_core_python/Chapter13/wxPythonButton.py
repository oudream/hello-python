# -*- coding:utf-8 -*-
# file: wxPythonButton.py
#
import wx									# 导入wxPython
class MyApp(wx.App):								# 通过继承创建类
	def OnInit(self):							# 重载OnInit方法
		frame = wx.Frame(parent = None,title = 'Button')		# 生成框架窗口
		panel = wx.Panel(frame, -1)					# 生成面板
		button = wx.Button(panel,					# 向面板添加按钮
				-1,						# 指定按钮ID
				'Button',					# 指定按钮上的文本
				pos=(50,50))					# 指定按钮在面板上的位置
		frame.Show()							# 显示窗口
		return True
app = MyApp()									# 类实例化
app.MainLoop()									# 进入消息循环
