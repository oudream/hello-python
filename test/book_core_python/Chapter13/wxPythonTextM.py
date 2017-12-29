# -*- coding:utf-8 -*-
# file: wxPythonTextM.py
#
import wx
class MyApp(wx.App):
	def OnInit(self):
		frame = wx.Frame(parent = None,title = 'wxPython',size = (600,400))		# 生成框架窗口
		panel = wx.Panel(frame, -1)							# 生成面板
		label1 = wx.StaticText(panel, -1, 'MultiLine', pos = (280,10))			# 生成标签
		text1 = wx.TextCtrl(panel,							# 生成文本框
				-1,  								# 指定文本框ID
				pos = (10,30),							# 指定文本框位置
				size = (580, 150),style=wx.TE_MULTILINE)			# 指定文本框大小
		label2 = wx.StaticText(panel, -1, 'RichText', pos = (280,190))			# 生成标签
		text2 = wx.TextCtrl(panel,							# 生成文本框
				-1,                                                             # 指定文本框ID
				'Python wxPython',                                              # 指定初始文本
				pos = (10,210),							# 指定文本框位置
				size = (580, 150),						# 指定文本框大小
				style =wx.TE_MULTILINE|wx.TE_RICH)				# 指定文本框为密码框
		text2.SetStyle(0, 6, wx.TextAttr('red', 'blue'))
		frame.Show()
		return True
app = MyApp()
app.MainLoop()
