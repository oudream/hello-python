# -*- coding:utf-8 -*-
# file: DllRes.py
#
import win32ui							# 导入Win32ui模块
import win32con							# 导入win32con模块 
from pywin.mfc import dialog					# 导入pywin.mfc中的dialog模块
class MyDialog(dialog.Dialog):					# 通过继承dialog.Dialog生成对话框类
	def OnInitDialog(self):					# 重载初始化函数
		dialog.Dialog.OnInitDialog(self)		# 调用父类的初始化函数
	def OnOK(self):						# 重载OnOK方法
		win32ui.MessageBox('Press Ok',	\
				'Python',	\
				win32con.MB_OK)	
		self.EndDialog(1)
	def OnCancel(self):					# 重载OnCancel方法
		win32ui.MessageBox('Press Cancel',\
				'Python',	  \
				win32con.MB_OK)
		self.EndDialog(1)	
dll = win32ui.LoadLibrary('Res.dll')
l = win32ui.LoadDialogResource(7000,dll)
mydialog = MyDialog(l)						# 生成对话框实例对象
mydialog.DoModal()						# 显示对话框	
