# -*- coding:utf-8 -*-
# file: pyOpenGLWindow.py
#
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
class OpenGLWindow:
	def __init__(self, width = 640, height = 480, title = 'PyOpenGL'):	# 初始化
		glutInit(sys.argv)						# 传递命令行参数
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)	# 设置显示模式
		glutInitWindowSize(width, height)				# 设置窗口大小
		self.window = glutCreateWindow(title)				# 创建窗口
		glutDisplayFunc(self.Draw)					# 设置场景绘制函数
		self.InitGL(width, height)					# 调用OpenGL初始化函数
	def Draw(self):								# 绘制场景
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)		# 清除屏幕和深度缓存
		glLoadIdentity()						# 重置观察矩阵
		glutSwapBuffers()						# 交换缓存
	def InitGL(self, width, height):					# OpenGL初始化函数
		glClearColor(0.0, 0.0, 0.0, 0.0)				# 设为黑色背景 
		glClearDepth(1.0)						# 设置深度缓存
		glDepthFunc(GL_LESS)						# 设置深度测试类型
		glEnable(GL_DEPTH_TEST)						# 允许深度测试
		glShadeModel(GL_SMOOTH)						# 启动平滑阴影
		glMatrixMode(GL_PROJECTION)					# 设置观察矩阵
		glLoadIdentity()						# 重置观察矩阵
		gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)	# 计算屏幕高宽比
		glMatrixMode(GL_MODELVIEW)					# 设置观察矩阵
	def MainLoop(self):							# 进入消息循环
		glutMainLoop()
window = OpenGLWindow()								# 创建窗口
window.MainLoop()								# 进入消息循环
