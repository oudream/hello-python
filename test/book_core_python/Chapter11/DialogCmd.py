# -*- coding:utf-8 -*-
# file: DialogCmd.py
#
import win32ui								# 导入win32ui模块
import win32con 							# 导入win32con模块
from pywin.mfc import dialog						# 从pywin.mfc导入dialog
class MyDialog(dialog.Dialog):						# 通过继承dialog.Dialog生成对话框类
	def OnInitDialog(self):						# 重载对话框初始化方法
		dialog.Dialog.OnInitDialog(self)			# 调用父类的对话框初始化方法
		self.HookCommand(self.OnButton1,1051)			# 设置消息处理方法 
		self.HookCommand(self.OnButton2,1052) 
	def OnButton1(self,wParam,lParam):				# 处理Button1点击消息
		win32ui.MessageBox('Button1',	\
				'Python',	\
				win32con.MB_OK)
		self.EndDialog(1)
	def OnButton2(self,lParam,wParam):				# 处理Button2点击消息
		text = self.GetDlgItemText(1054)
		win32ui.MessageBox(text,	\
				'Python',	\
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
Button1 = (['Button',							# 设置OK按钮属性
	'Button1',
	1051,
	(80,150, 50, 14), 
	buttonstyle | win32con.BS_PUSHBUTTON])
Button2 = (['Button',							# 设置Cancel按钮属性
	'Button2',
	1052,
	(160, 150, 50, 14),
	buttonstyle | win32con.BS_PUSHBUTTON])
Stadic = (['Static',							# 设置标签属性
	'Python Dialog',
	1053,
	(130,50,60,14),
	childstyle])
Edit = (['Edit',							# 设置文本框属性
	'',
	1054,
	(130,80,60,14),
	childstyle|win32con.ES_LEFT|
	win32con.WS_BORDER|win32con.WS_TABSTOP])
init = []								# 初始化信息列表
init.append(di)
init.append(Button1)
init.append(Button2)
init.append(Stadic)
init.append(Edit)
mydialog = MyDialog(init)						# 生成对话框实例对象
mydialog.DoModal()							# 创建对话框



