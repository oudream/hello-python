# -*- coding:utf-8 -*-
# file: pyOpenGLDraw2D.py
#
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math
class OpenGLWindow:
	def __init__(self, width = 640, height = 480, title = 'PyOpenGL'):	# 初始化
		glutInit(sys.argv)						# 传递命令行参数
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)	# 设置显示模式
		glutInitWindowSize(width, height)				# 设置窗口大小
		self.window = glutCreateWindow(title)				# 创建窗口
		glutDisplayFunc(self.Draw)					# 设置场景绘制函数
		self.InitGL(width, height)					# 调用OpenGL初始化函数
	def Draw(self):								# 绘制场景
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()						# 重置观察矩阵
		glTranslatef(-2.0, 2.0, -6.0)					# 移动位置
		glBegin(GL_LINES)						# 绘制直线
		glVertex3f(0.0, 0.0, 0.0)					# 直线第一点坐标
		glVertex3f(2.0, 0.0, 0.0)					# 直线第二点坐标
		glEnd()								# 结束绘制
		glTranslatef(3.0, 0.0, 0.0)					# 移动位置
		glBegin(GL_POLYGON)						# 通过绘制多边形来模拟圆
		i = 0
		while( i <= 3.14 *2 ):
			x = 0.5 * math.cos(i)
			y = 0.5 * math.sin(i)
			glVertex3f(x, y, 0.0)
			i = i + 0.01
		glEnd()
		glTranslatef(-2, -3.0, 0.0)					# 移动位置
		glBegin(GL_POLYGON)                 				# 绘制三角行
		glVertex3f(0.0, 1.0, 0.0)
		glVertex3f(1.0, -1.0, 0.0)
		glVertex3f(-1.0, -1.0, 0.0)
		glEnd()
		glTranslatef(2.5, 0.0, 0.0)					# 移动位置
		glBegin(GL_QUADS)                   				# 绘制四边形
		glVertex3f(-1.0, 1.0, 0.0)
		glVertex3f(1.0, 1.0, 0.0)
		glVertex3f(1.0, -1.0, 0.0)
		glVertex3f(-1.0, -1.0, 0.0)
		glEnd()
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
