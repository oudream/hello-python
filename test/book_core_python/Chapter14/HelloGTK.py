# -*- coding:utf-8 -*-
# file: HelloGTK.py
#
import pygtk					# 导入pygtk模块
pygtk.require('2.0')				# 设置pygtk所需的gtk版本
import gtk					# 导入gtk模块
window = gtk.Window()				# 创建窗口对象
window.set_title('PyGTK')			# 设置窗口标题
window.set_default_size(300, 200)		# 设置窗口大小
window.show()					# 显示窗口
gtk.main()					# 进入消息循环
