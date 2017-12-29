# -*- coding:utf-8 -*-
# file: wxEditor.py
#
import wx											# 导入wxPython
class CreateMenu():										# 创建菜单类
	def __init__(self, parent):
		self.menuBar = wx.MenuBar()							# 创建菜单条
		self.file = wx.Menu()								# 创建菜单
		self.open = self.file.Append(-1, '打开')
		self.save = self.file.Append(-1, '保存')
		self.saveas = self.file.Append(-1, '另存为')
		self.file.AppendSeparator()	
		self.close = self.file.Append(-1, '退出')
		self.menuBar.Append(self.file, '文件(&F)')
		self.edit = wx.Menu()
		self.undo = self.edit.Append(-1, '撤消')
		self.redo = self.edit.Append(-1, '重做')
		self.edit.AppendSeparator()
		self.cut = self.edit.Append(-1, '剪切')
		self.copy = self.edit.Append(-1, '复制')
		self.paste = self.edit.Append(-1, '粘贴')
		self.edit.AppendSeparator()
		self.selectall = self.edit.Append(-1, '全选')
		self.menuBar.Append(self.edit,'编辑(&E)')
		self.view = wx.Menu()
		self.color = self.view.AppendCheckItem(1051, '设为黑色')
		self.trans = self.view.Append(-1, '设置透明度')
		self.menuBar.Append(self.view, '查看(&V)')
		self.help = wx.Menu()
		self.about = self.help.Append(-1, '关于')
		self.menuBar.Append(self.help, '帮助(&H)')
		parent.SetMenuBar(self.menuBar)							# 向框架窗口中添加菜单

class MyApp(wx.App):										# 通过继承创建类
	def OnInit(self):									# 重载OnInit方法
		self.file = ''
		self.width = 600
		self.height = 480
		self.frame = wx.Frame(parent = None,title = 'wxPython Notebook',
				size = (self.width,self.height))				# 生成框架窗口
		self.panel = wx.Panel(self.frame, -1)						# 生成面板
		self.menu = CreateMenu(self.frame)						# 生成菜单
		self.text = wx.TextCtrl(self.panel,						# 生成文本框
				-1, 
				pos = (2,2),
				size = (self.width-10, self.height-50),
				style = wx.HSCROLL | wx.TE_MULTILINE)
		self.Bind(wx.EVT_MENU, self.OnOpen, self.menu.open)				# 绑定事件
		self.Bind(wx.EVT_MENU, self.OnSave, self.menu.save)
		self.Bind(wx.EVT_MENU, self.OnSaveAs, self.menu.saveas)
		self.Bind(wx.EVT_MENU, self.OnClose, self.menu.close)
		self.Bind(wx.EVT_MENU, self.OnUndo, self.menu.undo)
		self.Bind(wx.EVT_MENU, self.OnRedo, self.menu.redo)
		self.Bind(wx.EVT_MENU, self.OnCut, self.menu.cut)
		self.Bind(wx.EVT_MENU, self.OnCopy, self.menu.copy)
		self.Bind(wx.EVT_MENU, self.OnPaste, self.menu.paste)
		self.Bind(wx.EVT_MENU, self.OnSelectAll, self.menu.selectall)
		self.Bind(wx.EVT_MENU, self.OnColor, self.menu.color)
		self.Bind(wx.EVT_MENU, self.OnTrans, self.menu.trans)
		self.Bind(wx.EVT_MENU, self.OnAbout, self.menu.about)
		self.Bind(wx.EVT_RIGHT_DOWN, self.OnRClick)
		self.Bind(wx.EVT_SIZE, self.Resize)
		self.frame.Show()
		return True
	def OnOpen(self, event):								# 处理打开命令
		dialog = wx.FileDialog(None, 'wxPython Notebook', style = wx.OPEN) 
		if dialog.ShowModal() == wx.ID_OK:
			self.file = dialog.GetPath()
			file = open(self.file)
			self.text.write(file.read())
			file.close()
		dialog.Destroy()
	def OnSave(self, event):								# 处理保存命令
		if self.file == '':
			dialog = wx.FileDialog(None, 'wxPython Notebook', style =  wx.SAVE)
			if dialog.ShowModal() == wx.ID_OK:
				self.file = dialog.GetPath()
				self.text.SaveFile(self.file)
			dialog.Destroy()
		else:
			self.text.SaveFile(self.file)
	def OnSaveAs(self, event):								# 处理另存为命令
		dialog = wx.FileDialog(None, 'wxPython Notebook', style =  wx.SAVE)
		if dialog.ShowModal() == wx.ID_OK:
			self.file = dialog.GetPath()
			self.text.SaveFile(self.file)
		dialog.Destroy()
	def OnClose(self, event):								# 处理退出命令
		self.frame.Destroy()
	def OnAbout(self, event):								# 处理关于命令
		wx.MessageBox('A simple editor!', 'wxPython Notebook', wx.OK)
	def OnRClick(self, event):								# 处理右键事件
		pos = (event.GetX(),event.GetY())
		self.panel.PopupMenu(self.menu.edit, pos)
	def OnUndo(self, event):								# 处理撤消命令
		self.text.Undo()
	def OnRedo(self, event):								# 处理重做命令
		self.text.Redo()
	def OnCut(self, event):									# 处理剪切命令
		self.text.Cut()
	def OnCopy(self, event):								# 处理复制命令
		self.text.Copy()
	def OnPaste(self, event):								# 处理粘贴命令
		self.text.Paste()
	def OnSelectAll(self, event):								# 处理全选命令
		self.text.SelectAll()
	def OnColor(self, event):								# 处理设为黑色命令
		if self.menu.view.IsChecked(1051):
			self.text.SetBackgroundColour('black')
			self.text.SetForegroundColour('green')
			self.text.Refresh()
		else:
			self.text.SetBackgroundColour('white')
			self.text.SetForegroundColour('black')
			self.text.Refresh()
	def OnTrans(self, event):								# 处理设置透明度命令
		r = wx.GetNumberFromUser('请选择透明度','',
				'wxPython Notebook',80, min = 30)
		if r != -1:
			self.frame.SetTransparent((r* 255/100))
			self.frame.Refresh()
	def Resize(self, event):								# 处理窗口改变大小命令
		newsize = self.frame.GetSize()
		width = newsize.GetWidth() - 10
		height = newsize.GetHeight() - 50
		self.text.SetSize((width,height))
		self.text.Refresh()
app = MyApp()
app.MainLoop()
