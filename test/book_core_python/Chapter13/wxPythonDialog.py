# -*- coding:utf-8 -*-
# file: wxPythonDialog.py
#
import wx											# 导入wxPython
class MyApp(wx.App):										# 通过继承创建类
	def OnInit(self):									# 重载OnInit方法
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,170))		# 生成框架窗口
		panel = wx.Panel(frame, -1)							# 生成面板
		self.button = wx.Button(panel, -1, 'Show Dialog', pos=(100, 50))		# 添加Button
		self.Bind(wx.EVT_BUTTON, self.OnButton, self.button)
		frame.Show()									# 显示窗口
		return True
	def OnButton(self, event):								# 按钮事件响应函数
		dialog = MyDialog()
		r = dialog.ShowModal()								# 获取返回值
		if r == wx.ID_OK:								# 判断是否单击对话框的Ok按钮
			wx.MessageBox('You input:' + dialog.text.GetValue(),			# 弹出消息框
					'wxPython', wx.OK)
		dialog.Destroy()								# 销毁对话框
class MyDialog(wx.Dialog):									# 定义对话框类
	def __init__(self):									# 初始化
		wx.Dialog.__init__(self, None, -1, 'wxDilog',size=(300, 170))			# 调用父类的初始化方法
		label = wx.StaticText(self, -1, 'Simple Dialog',pos = (120,20))			# 生成标签
		self.text = wx.TextCtrl(self, -1, pos = (100,50), size = (160, -1))		# 生成文本框
		self.ok = wx.Button(self, wx.ID_OK, "OK", pos=(50, 80))				# 生成OK按钮	
		self.cancel = wx.Button(self, wx.ID_CANCEL, "Cancel",pos=(200, 80))		# 生成Cancel按钮
app = MyApp()
app.MainLoop()
