# -*- coding:utf-8 -*-
# file: wxPythonStatic.py
#
import wx
class MyApp(wx.App):
	def OnInit(self):
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,200))		# 生成框架窗口
		panel = wx.Panel(frame, -1)							# 生成面板
		label1 = wx.StaticText(panel,							# 生成标签
				-1, 								# 指定标签ID
				'Python', 							# 指定标签中文本
				size = (160,20),						# 指定标签大小
				pos = (60,10),							# 指定标签位置
				style = wx.ALIGN_RIGHT)						# 指定标签样式，右对齐
		label2 = wx.StaticText(panel,							# 生成标签
				-1, 								# 指定标签ID
				'Python',							# 指定标签中文本
				size = (160,20),						# 指定标签大小
				pos = (60,50),							# 指定标签位置
				style = wx.ALIGN_CENTER)					# 指定标签样式，剧中对齐
		label2.SetForegroundColour('red')						# 指定标签前景色
		label2.SetBackgroundColour('black')						# 指定标签背景色
		label3 = wx.StaticText(panel,							# 生成标签
				-1, 								# 指定标签ID
				'Python\nwxPython',						# 在文本中使用换行符
				size = (160,40),						# 指定标签大小
				pos = (60,90))							# 指定标签位置
		frame.Show()
		return True
app = MyApp()
app.MainLoop()
