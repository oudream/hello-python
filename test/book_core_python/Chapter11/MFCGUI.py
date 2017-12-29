# -*- coding:utf-8 -*-
# file: MFCGUI.py
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
            		(100, 100, 400, 300), None, 0, None)
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
