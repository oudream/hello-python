# -*- coding:utf-8 -*-
# file: HelloTkinter.py
#
import Tkinter							# ����Tkinterģ��
root = Tkinter.Tk()						# ����root������
label= Tkinter.Label(root, text="hello, Tkinter!")		# ���ɱ�ǩ
label.pack()							# ����ǩ��ӵ�root������
button1 = Tkinter.Button(root, text="Button1")			# ����button1
button1.pack(side=Tkinter.LEFT)					# ��button1��ӵ�root������
button2 = Tkinter.Button(root, text="Button2")			# ����button2
button2.pack(side=Tkinter.RIGHT)				# ��button2��ӵ�root������
root.mainloop()							# ������Ϣѭ��
