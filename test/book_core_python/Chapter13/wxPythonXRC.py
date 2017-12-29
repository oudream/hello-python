# -*- coding:utf-8 -*-
# file: wxPythonXRC.py
#
import wx
from wx import xrc
class MyApp(wx.App):
	def OnInit(self):
		self.res = xrc.XmlResource('res.xrc')						# 载入资源文件
		self.frame = self.res.LoadFrame(None, 'frame')					# 从资源文件中载入frame
		self.panel = xrc.XRCCTRL(self.frame, 'panel')					# 载入panel
		self.label = xrc.XRCCTRL(self.panel, 'label')					# 载入label
		self.text = xrc.XRCCTRL(self.panel, 'text')					# 载入text
		self.button = xrc.XRCCTRL(self.panel, 'button')					# 载入button
		self.Bind(wx.EVT_BUTTON, self.OnButton, self.button)				# 绑定按钮事件
		self.frame.Show()
		return True
	def OnButton(self, event):								# 处理按钮事件
		wx.MessageBox('You input:'+self.text.GetValue(), 'wxPython', wx.OK)
app = MyApp(False)
app.MainLoop()
