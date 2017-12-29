# -*- coding:utf-8 -*-
# file: wxPythonCheckRadio.py
#
import wx
class MyApp(wx.App):
	def OnInit(self):
		frame = wx.Frame(parent = None,title = 'wxPython',size = (300,200))		# 生成框架窗口
		panel = wx.Panel(frame, -1)							# 生成面板
		self.radio1 = wx.RadioButton(panel, 						# 生成单选框
				-1, 								# 指定单选框ID
				'Radio1',							# 指定单选框文本
				pos=(10, 40),							# 指定单选框位置
				style=wx.RB_GROUP)						# 指定单选框样式
		self.radio2 = wx.RadioButton(panel,						# 生成框架窗口
				-1, 								# 指定单选框ID
				'Radio2',							# 指定单选框文本
				pos=(10, 80))							# 指定单选框位置
		self.radio3 = wx.RadioButton(panel, 						# 生成单选框
				-1, 								# 指定单选框ID
				'Radio3', 							# 指定单选框文本
				pos=(10, 120))							# 指定单选框位置
		self.check = wx.CheckBox(panel, 						# 生成复单选框
				-1, 								# 指定复单选框ID
				'CheckBox',							# 指定复单选框文本
				pos = (120, 40),						# 指定复选框位置
				size = (150, 20))						# 指定复选框大小
		self.button1 = wx.Button(panel,-1,'Radio',pos = (120,80))			# 生成按钮
		self.button2 = wx.Button(panel,-1,'Check',pos = (120,120))
		self.Bind(wx.EVT_BUTTON, self.OnButton1, self.button1)				# 绑定按钮事件
		self.Bind(wx.EVT_BUTTON, self.OnButton2, self.button2)
		frame.Show()
		return True
	def OnButton1(self, event):								# 按钮事件处理方法
		if self.radio1.GetValue():							# 判断Radio1是否选中
			self.button1.SetLabel('Radio1')
		elif self.radio2.GetValue():							# 判断Radio2是否选中
			self.button1.SetLabel('Radio2')
		else:
			self.button1.SetLabel('Radio3')
	def OnButton2(self, event):								# 按钮事件处理方法
		if self.check.IsChecked():							# 判断CheckBox是否选中
			self.button2.SetLabel('Checked')
		else:
			self.button2.SetLabel('UnChecke')
app = MyApp()
app.MainLoop()
