# -*- coding:utf-8 -*-
# file: DllMenu.py
#
import win32ui
import win32api
from win32con import *
from pywin.mfc import window
# 定义窗口类
class MyWnd(window.Wnd):
	def __init__ (self):
		window.Wnd.__init__(self, win32ui.CreateWnd ())
	 	self._obj_.CreateWindowEx(WS_EX_CLIENTEDGE, \
           		win32ui.RegisterWndClass(0, 0, COLOR_WINDOW + 1), \
            		'MFC GUI', WS_OVERLAPPEDWINDOW, \
            		(10, 10, 800, 500), None, 0, None)
		dll = win32ui.LoadLibrary('Res.dll')				# 载入DLL文件
		m = win32ui.LoadMenu(7001,dll)					# 载入菜单
		self._obj_.SetMenu(m)						# 向创建添加菜单
	# 重载OnClose方法
	def OnClose(self):
		self.EndModalLoop(0)
	# 重载OnPaint方法，在窗口中输出“MFC GUI”
	def OnPaint(self):
		dc,ps = self.BeginPaint()
		dc.DrawText('MFC GUI',
			self.GetClientRect(),
			DT_SINGLELINE | DT_CENTER | DT_VCENTER)
		self.EndPaint(ps)

w = MyWnd()				# 生成窗口对象			
w.ShowWindow()				# 显示窗口
w.UpdateWindow()			# 刷新窗口
w.RunModalLoop(1)			# 进入消息循环
