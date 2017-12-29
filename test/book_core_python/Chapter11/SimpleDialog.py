# -*- coding:utf-8 -*-
# file: SimpleDialog.py
#
import win32ui							# 导入Win32ui模块
import win32con							# 导入win32con模块 
from pywin.mfc import dialog					# 导入pywin.mfc中的dialog模块
class MyDialog(dialog.Dialog):					# 通过继承dialog.Dialog生成对话框类
	def OnInitDialog(self):					# 重载初始化函数
		dialog.Dialog.OnInitDialog(self)		# 调用父类的初始化函数
style = (win32con.DS_MODALFRAME  |
	     win32con.WS_POPUP 	 |
	     win32con.WS_VISIBLE |
	     win32con.WS_CAPTION |
	     win32con.WS_SYSMENU |
	     win32con.DS_SETFONT)
di = ['Python',							# 设置对话框属性，设置标题为“Python”
	(0,0,300,180),						# 设置对话框位置及大小
	style,							# 设置对话框样式
	None,							# 设置对话框扩展样式
	(8, "MS Sans Serif")]					# 设置对话框字体及大小
init = []							# 定义对话框初始化参数列表
init.append(di) 
mydialog = MyDialog(init)					# 生成对话框实例对象
mydialog.DoModal()						# 显示对话框	
