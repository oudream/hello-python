# -*- coding:utf-8 -*-
# file: SimpleHello.py
#
import wx
app = wx.PySimpleApp()
frame = wx.Frame(parent = None,title = 'Simple hello')
frame.Show(True)
app.MainLoop()