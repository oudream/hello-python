# -*- coding:utf-8 -*-
# file: pyOpenGLTexture.py
#
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import Image
class OpenGLWindow:
	def __init__(self, width = 640, height = 480, title = 'PyOpenGL'):	# 初始化
		glutInit(sys.argv)						# 传递命令行参数
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)	# 设置显示模式
		glutInitWindowSize(width, height)				# 设置窗口大小
		self.window = glutCreateWindow(title)				# 创建窗口
		glutDisplayFunc(self.Draw)					# 设置场景绘制函数
		glutIdleFunc(self.Draw)						# 设置空闲时场景绘制函数
		self.InitGL(width, height)					# 调用OpenGL初始化函数
		self.x = 0.2							# 旋转角度增量
		self.y = 0.2
		self.z = 0.2
	def Draw(self):								# 绘制场景
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)		# 清除屏幕
		glLoadIdentity()						# 重置观察矩阵
		glTranslatef(0.0,0.0,-5.0)					# 移动位置
		glRotatef(self.x,1.0,0.0,0.0)					# 绕X轴旋转
		glRotatef(self.y,0.0,1.0,0.0)					# 绕Y轴旋转
		glRotatef(self.z,0.0,0.0,1.0)					# 绕Z轴旋转
		glBegin(GL_QUADS)			    			# 绘制立方体
		glTexCoord2f(0.0, 0.0) 						# 对前面进行贴图
		glVertex3f(-1.0, -1.0,  1.0)
		glTexCoord2f(1.0, 0.0) 
		glVertex3f( 1.0, -1.0,  1.0)
		glTexCoord2f(1.0, 1.0) 
		glVertex3f( 1.0,  1.0,  1.0)
		glTexCoord2f(0.0, 1.0) 
		glVertex3f(-1.0,  1.0,  1.0)
		glTexCoord2f(1.0, 0.0) 						# 对后面进行贴图
		glVertex3f(-1.0, -1.0, -1.0)
		glTexCoord2f(1.0, 1.0) 
		glVertex3f(-1.0,  1.0, -1.0)
		glTexCoord2f(0.0, 1.0) 
		glVertex3f( 1.0,  1.0, -1.0)
		glTexCoord2f(0.0, 0.0)
		glVertex3f( 1.0, -1.0, -1.0)
		glTexCoord2f(0.0, 1.0) 						# 对顶面进行贴图 
		glVertex3f(-1.0,  1.0, -1.0)
		glTexCoord2f(0.0, 0.0) 
		glVertex3f(-1.0,  1.0,  1.0)
		glTexCoord2f(1.0, 0.0) 
		glVertex3f( 1.0,  1.0,  1.0)
		glTexCoord2f(1.0, 1.0) 
		glVertex3f( 1.0,  1.0, -1.0)
		glTexCoord2f(1.0, 1.0) 						# 对底面进行贴图
		glVertex3f(-1.0, -1.0, -1.0)
		glTexCoord2f(0.0, 1.0) 
		glVertex3f( 1.0, -1.0, -1.0)
		glTexCoord2f(0.0, 0.0) 
		glVertex3f( 1.0, -1.0,  1.0)
		glTexCoord2f(1.0, 0.0)
		glVertex3f(-1.0, -1.0,  1.0)
		glTexCoord2f(1.0, 0.0) 						# 对右侧面进行贴图
		glVertex3f( 1.0, -1.0, -1.0)
		glTexCoord2f(1.0, 1.0) 
		glVertex3f( 1.0,  1.0, -1.0)
		glTexCoord2f(0.0, 1.0) 
		glVertex3f( 1.0,  1.0,  1.0)
		glTexCoord2f(0.0, 0.0) 
		glVertex3f( 1.0, -1.0,  1.0)
		glTexCoord2f(0.0, 0.0) 						# 对左侧面进行贴图
		glVertex3f(-1.0, -1.0, -1.0)
		glTexCoord2f(1.0, 0.0) 
		glVertex3f(-1.0, -1.0,  1.0)
		glTexCoord2f(1.0, 1.0) 
		glVertex3f(-1.0,  1.0,  1.0)
		glTexCoord2f(0.0, 1.0) 
		glVertex3f(-1.0,  1.0, -1.0)
		glEnd()			
		glutSwapBuffers()						# 交换缓存
		self.x = self.x + 0.2						# 旋转角度增加
		self.y = self.y + 0.2
		self.z = self.z + 0.2
	def InitGL(self, width, height):					# OpenGL初始化函数
    		self.LoadTextures()						# 载入纹理
    		glEnable(GL_TEXTURE_2D)						# 允许纹理映射
		glClearColor(0.0, 0.0, 0.0, 0.0)				# 设为黑色背景 
		glClearDepth(1.0)						# 设置深度缓存
		glDepthFunc(GL_LESS)						# 设置深度测试类型
		glEnable(GL_DEPTH_TEST)						# 允许深度测试
		glShadeModel(GL_SMOOTH)						# 启动平滑阴影
		glMatrixMode(GL_PROJECTION)					# 设置观察矩阵
		glLoadIdentity()						# 重置观察矩阵
		gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)	# 计算屏幕高宽比
		glMatrixMode(GL_MODELVIEW)					# 设置观察矩阵
	def LoadTextures(self):							# 载入纹理图片
		image = Image.open('python.bmp')				# 打开图片
		width = image.size[0]						# 图像宽度
		height = image.size[1]						# 图像高度
		image = image.tostring('raw', 'RGBX', 0, -1)			# 转换图像
		glBindTexture(GL_TEXTURE_2D, glGenTextures(1))   		# 创建纹理
		glPixelStorei(GL_UNPACK_ALIGNMENT,1)
		glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 
				0, GL_RGBA, GL_UNSIGNED_BYTE, image)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
	def MainLoop(self):							# 进入消息循环
		glutMainLoop()
window = OpenGLWindow()								# 创建窗口
window.MainLoop()								# 进入消息循环
