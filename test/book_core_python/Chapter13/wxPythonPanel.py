# -*- coding:utf-8 -*-
# file: wxPythonPanel.py
#
import wx								# 导入wxPython模块
class MyApp(wx.App):							# 通过继承wx.App类创建类
	def OnInit(self):						# 重载OnInit方法
		frame = wx.Frame(parent = None,				# 创建框架窗口
				id=-1, 					# 指定框架ID
				title='Panel', 				# 指定窗口标题
				pos=(100,100),				# 指定窗口位置
				size=(600,480), 			# 指定窗口大小
				style=wx.DEFAULT_FRAME_STYLE,		# 指定窗口样式
				name="frame")				# 指定窗口名
		panel = wx.Panel(frame, -1)				# 向框架窗口添加面板
		frame.Show()						# 显示框架窗口
		return True						# 返回True
app = MyApp()								# 类实例化
app.MainLoop()								# 进入消息循环
