# -*- coding:utf-8 -*-
# file: Dialog.py
#
import win32ui								# 导入win32ui模块
import win32con 							# 导入win32con模块
from pywin.mfc import dialog						# 从pywin.mfc导入dialog
class MyDialog(dialog.Dialog):						# 重载对话框初始化方法
	def OnInitDialog(self):						# 调用父类的对话框初始化方法
		dialog.Dialog.OnInitDialog(self)			# 重载OnOK方法
	def OnOK(self):							#
		win32ui.MessageBox('Press Ok',	\
				'Python',	\
				win32con.MB_OK)
		self.EndDialog(1)
	def OnCancel(self):						# 重载OnCancel方法
		win32ui.MessageBox('Press Cancel',\
				'Python',	  \
				win32con.MB_OK)
		self.EndDialog(1)
style = (win32con.DS_MODALFRAME  |					# 定义对话框样式
	     win32con.WS_POPUP 	 |
	     win32con.WS_VISIBLE |
	     win32con.WS_CAPTION |
	     win32con.WS_SYSMENU |
	     win32con.DS_SETFONT)
childstyle = (win32con.WS_CHILD |					# 定义控件样式
	  win32con.WS_VISIBLE)
buttonstyle = win32con.WS_TABSTOP | childstyle				# 定义按钮样式
di = ['Python',								# 设置对话框属性 
	(0,0,300,180),
	style,
	None,
	(8, "MS Sans Serif")]
ButOK = (['Button',							# 设置OK按钮属性
	"OK",
	win32con.IDOK,
	(80,150, 50, 14), 
	buttonstyle | win32con.BS_PUSHBUTTON])
ButCancel = (['Button',							# 设置Cancel按钮属性
		"Cancel",
		win32con.IDCANCEL,
		(160, 150, 50, 14),
		buttonstyle | win32con.BS_PUSHBUTTON])
Stadic = (['Static',							# 设置标签属性
		'Python Dialog',
		12,
		(130,50,60,14),
		childstyle])
Edit = (['Edit',							# 设置文本框属性
		'',
		13,
		(130,80,60,14),
		childstyle|win32con.ES_LEFT|
		win32con.WS_BORDER|win32con.WS_TABSTOP])
init = []								# 初始化信息列表
init.append(di)
init.append(ButOK)
init.append(ButCancel)
init.append(Stadic)
init.append(Edit)
mydialog = MyDialog(init)						# 生成对话框实例对象
mydialog.DoModal()							# 创建对话框

