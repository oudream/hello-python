# -*- coding:utf-8 -*-
# file: wxPythonMenuEvent.py
#
import wx											# 导入wxPython
class MyApp(wx.App):										# 通过继承创建类
	def OnInit(self):									# 重载OnInit方法
		self.frame = wx.Frame(parent = None,title = 'wxPython',size = (300,170))	# 生成框架窗口
		self.panel = wx.Panel(self.frame, -1)						# 生成面板
		menuBar = wx.MenuBar()								# 创建菜单条
		self.menu = wx.Menu()								# 创建菜单
		open = self.menu.Append(-1, 'Open')
		save = self.menu.Append(-1, 'Save')
		self.menu.AppendSeparator()	
		close = self.menu.Append(-1, 'Close')
		menuBar.Append(self.menu, '&File')
		self.menu = wx.Menu()								# 重新创建菜单
		about = self.menu.Append(-1, 'About')
		menuBar.Append(self.menu, '&Help')
		self.frame.SetMenuBar(menuBar)							# 向框架窗口中添加菜单
		self.Bind(wx.EVT_MENU, self.OnOpen, open)					# 绑定菜单事件
		self.Bind(wx.EVT_MENU, self.OnSave, save)
		self.Bind(wx.EVT_MENU, self.OnClose, close)
		self.Bind(wx.EVT_MENU, self.OnAbout, about)
		self.Bind(wx.EVT_RIGHT_DOWN, self.OnRClick)
		self.frame.Show()
		return True
	def OnOpen(self, event):								# 处理Open命令
		dialog = wx.FileDialog(None, 'wxPython', style = wx.OPEN) 			# 创建打开文件对话框
		dialog.ShowModal()
		dialog.Destroy()
	def OnSave(self, event):								# 处理Save命令
		dialog = wx.FileDialog(None, 'wxPython', style =  wx.SAVE)			# 创建保存文件对话框
		dialog.ShowModal()
		dialog.Destroy()
	def OnClose(self, event):								# 处理Close命令
		self.frame.Destroy()								# 退出程序
	def OnAbout(self, event):								# 处理About命令
		wx.MessageBox('wxPython Menu Event', 'wxPython', wx.OK)				# 创建消息框
	def OnRClick(self, event):								# 处理右键事件
		pos = (event.GetX(),event.GetY())
		self.panel.PopupMenu(self.menu, pos)						# 创建弹出式菜单
app = MyApp()
app.MainLoop()
