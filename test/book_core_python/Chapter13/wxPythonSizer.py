# -*- coding:utf-8 -*-
# file: wxPythonSizer.py
#
import wx
class MyApp(wx.App):
	def OnInit(self):
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,200))		# 生成框架窗口
		panel = wx.Panel(frame, -1)							# 生成面板
		sizer = wx.GridSizer(rows=3, cols=3)						# 创建一个三行三列的sizer
		sizer.AddSpacer(0)								# 向sizer中添加一个空项
		label = wx.StaticText(panel, -1, 'label')					# 生成标签
		sizer.Add(label,flag = wx.ALIGN_CENTER)						# 向sizer添加标签居中对齐
		sizer.AddSpacer(0)	
		button1 = wx.Button(panel, -1, 'Button1')					# 生成按钮
		sizer.Add(button1,flag = wx.ALIGN_CENTER)					# 向sizer中添加按钮
		sizer.AddSpacer(0)
		button2 = wx.Button(panel, -1, 'Button2')					# 生成按钮
		sizer.Add(button2,flag = wx.ALIGN_CENTER)					# 向sizer中添加按钮
		sizer.AddSpacer(0)
		text = wx.TextCtrl(panel, -1, size = (100,20))					# 生成文本框
		sizer.Add(text)									# 向sizer中添加文本框
		sizer.AddSpacer(0)
		panel.SetSizer(sizer)								# 向面板中添加sizer
		frame.Show()
		return True
app = MyApp()
app.MainLoop()
