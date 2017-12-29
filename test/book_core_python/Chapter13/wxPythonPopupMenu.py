# -*- coding:utf-8 -*-
# file: wxPythonPopupMenu.py
#
import wx											# 导入wxPython
class MyApp(wx.App):										# 通过继承创建类
	def OnInit(self):									# 重载OnInit方法
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,170))		# 生成框架窗口
		self.panel = wx.Panel(frame, -1)						# 生成面板
		menuBar = wx.MenuBar()								# 创建菜单条
		self.menu = wx.Menu()								# 创建菜单
		open = self.menu.Append(-1, 'Open')
		save = self.menu.Append(-1, 'Save')
		self.menu.AppendSeparator()	
		close = self.menu.Append(-1, 'Close')
		menuBar.Append(self.menu, '&File')
		frame.SetMenuBar(menuBar)							# 向框架窗口中添加菜单
		self.Bind(wx.EVT_RIGHT_DOWN, self.OnRClick)					# 绑定右键事件
		frame.Show()
		return True
	def OnRClick(self, event):
		pos = (event.GetX(),event.GetY())						# 获得鼠标点击坐标
		self.panel.PopupMenu(self.menu, pos)						# 显示菜单
app = MyApp()
app.MainLoop()
