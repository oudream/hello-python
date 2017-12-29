# -*- coding:utf-8 -*-
# file: wxPythonMenu.py
#
import wx											# 导入wxPython
class MyApp(wx.App):										# 通过继承创建类
	def OnInit(self):									# 重载OnInit方法
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,170))		# 生成框架窗口
		panel = wx.Panel(frame, -1)							# 生成面板
		menuBar = wx.MenuBar()								# 创建菜单条
		menu = wx.Menu()								# 创建菜单
		open = menu.Append(-1, 'Open')							# 向菜单中添加Open
		exit = menu.Append(-1, 'Save')							# 向菜单中添加Save
		menu.AppendSeparator()								# 向菜单中添加分隔符
		close = menu.Append(-1, 'Close')						# 向菜单中添加Close
		menuBar.Append(menu, '&File')							# 向菜单条中添加File
		menu = wx.Menu()								# 重新创建菜单
		copy = menu.Append(-1, 'Copy')							# 向菜单中添加Copy
		paste = menu.Append(-1, 'Paste')						# 向菜单中添加Paste
		cut = menu.Append(-1, 'Cut')							# 向菜单中添加Cut 
		menu.AppendSeparator()								# 向菜单中添加分隔符
		selectall = menu.Append(-1, 'SelectAll')					# 向菜单中添加SelectAll
		menuBar.Append(menu, '&Edit')							# 向菜单条中添加Edit
		menu = wx.Menu()								# 重新创建菜单
		about = menu.Append(-1, 'About')						# 向菜单中添加About
		menuBar.Append(menu, '&Help')							# 向菜单条中添加Help
		frame.SetMenuBar(menuBar)							# 向框架窗口中添加菜单
		frame.Show()									# 显示窗口
		return True
app = MyApp()
app.MainLoop()
