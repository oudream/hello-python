# -*- coding:utf-8 -*-
# file: TkinterPopupmenu.py
#
import Tkinter 
root = Tkinter.Tk()
menu = Tkinter.Menu(root, tearoff=0)				# 创建菜单
menu.add_command(label="Copy")					# 向弹出式菜单中添加Copy命令
menu.add_command(label="Paste")					# 向弹出式菜单中添加Paste命令
menu.add_separator()						# 向弹出式菜单中添加分隔符
menu.add_command(label="Cut")					# 向弹出式菜单中添加Cut命令
def popupmenu(event):						# 定义右键事件处理函数
    menu.post(event.x_root, event.y_root)			# 显示菜单
root.bind("<Button-3>", popupmenu)				# 在主窗口中绑定右键事件
root.mainloop()
