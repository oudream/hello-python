# -*- coding:utf-8 -*-
# file: wxPythonTextS.py
#
import wx
class MyApp(wx.App):
	def OnInit(self):
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,200))		# 生成框架窗口
		panel = wx.Panel(frame, -1)							# 生成面板
		label1 = wx.StaticText(panel, -1, 'wxPython', pos = (120,20))			# 生成标签
		label2 = wx.StaticText(panel, -1, 'User Name:',pos = (10,50)) 			# 生成标签
		text = wx.TextCtrl(panel,							# 生成文本框
				-1,  								# 指定文本框ID
				pos = (100,50),							# 指定文本框位置
				size = (160, -1))						# 指定文本框大小
		label3 = wx.StaticText(panel, -1, "Password:",pos = (10,100))			# 生成标签
		password = wx.TextCtrl(panel,							# 生成文本框
				-1,                                                             # 指定文本框ID
				"password",                                                     # 指定初始文本
				pos = (100,100),						# 指定文本框位置
				size = (160, -1),						# 指定文本框大小
				style=wx.TE_PASSWORD)						# 指定文本框为密码框
		frame.Show()
		return True
app = MyApp()
app.MainLoop()

