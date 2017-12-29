# -*- coding:utf-8 -*-
# file: wxPythonStandardDialog.py
#
import wx
class MyApp(wx.App):
	def OnInit(self):
		self.frame = wx.Frame(parent = None,title = 'wxPython',size = (300,200))		# 生成框架窗口
		panel = wx.Panel(self.frame, -1)							# 生成面板
		self.button1 = wx.Button(panel,-1,'Input String',pos = (100,20))			# 生成按钮
		self.button2 = wx.Button(panel,-1,'Input Password',pos = (100,70))
		self.button3 = wx.Button(panel,-1,'Input Number',pos = (100,120))
		self.Bind(wx.EVT_BUTTON, self.OnButton1, self.button1)					# 绑定按钮事件
		self.Bind(wx.EVT_BUTTON, self.OnButton2, self.button2)
		self.Bind(wx.EVT_BUTTON, self.OnButton3, self.button3)
		self.frame.Show()
		return True
	def OnButton1(self, event):
		r = wx.GetTextFromUser('wxPython','String', 'Default')					# 创建文本输入框
		wx.MessageBox(r, 'wxPython',wx.OK)							# 创建MessageBox
	def OnButton2(self, event):
		r = wx.GetPasswordFromUser('wxPython','Password')					# 创建密码输入框
		wx.MessageBox(r, 'wxPython',wx.OK)							# 创建MessageBox
	def OnButton3(self, event):
		r = wx.GetNumberFromUser('Input Number','Number','wxPython',80)				# 创建整数输入框
		wx.MessageBox(str(r), 'wxPython',wx.OK)							# 创建MessageBox
app = MyApp()
app.MainLoop()
