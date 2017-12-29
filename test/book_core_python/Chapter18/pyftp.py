# -*- coding:utf-8 -*-
# file: pyftp.py
#
import string
from ftplib import FTP								# 从ftplib模块中导入FTP
bufsize = 1024									# 设置缓冲区大小
def Get(filename):								# 下载文件
	command = 'RETR ' + filename
	ftp.retrbinary(command, open(filename,'wb').write, bufsize)
	print '下载成功'
def Put(filename):								# 上传文件
	command = 'STOR ' + filename
	filehandler = open(filename,'rb')
	ftp.storbinary(command,filehandler,bufsize)
	filehandler.close()
	print '上传成功'
def PWD():									# 获取当前目录
	print ftp.pwd()
def Size(filename):								# 获取文件大小
	print ftp.size(filename)
def Help():									# 输出帮助
	print '''
	==================================
		Simple Python FTP 
	==================================
	cd		进入文件夹
	delete		删除文件
	dir		获取当前文件列表
	get		下载文件
	help		帮助
	mkdir		创建文件夹
	put		上传文件
	pwd		获取当前目录
	rename		重命名文件
	rmdir		删除文件夹
	size		获取文件大小
	'''
server = raw_input('请输入FTP服务器地址:')					# 获取服务器地址
ftp = FTP(server)								# 连接到服务器地址
username = raw_input('请输入用户名:')						# 获取用户名
password = raw_input('请输入密码:')						# 获取字典
ftp.login(username,password)              					# 登录FTP
print ftp.getwelcome()								# 获取欢迎信息
actions  = {'dir':ftp.dir, 'pwd': PWD, 'cd':ftp.cwd, 'get':Get,			# 命令与对应的函数字典
		'put':Put, 'help':Help, 'rmdir': ftp.rmd, 
		'mkdir': ftp.mkd, 'delete':ftp.delete,
		'size':Size, 'rename':ftp.rename}
while True:									# 命令循环
	print 'pyftp>',								# 输出提示符
	cmds = raw_input()							# 获取输入
	cmd = string.split(cmds)						# 将输入按空格分割
	try:									# 异常处理
		if len(cmd) == 1:						# 判断命令是否有参数
			if string.lower(cmd[0]) == 'quit':			# 如果命令为quit则退出循环
				break
			else:
				actions[string.lower(cmd[0])]()			# 调用与命令对应的函数
		elif len(cmd) == 2:						# 处理命令有一个参数的情况
			actions[string.lower(cmd[0])](cmd[1])			# 调用与命令对应的函数
		elif len(cmd) == 3:						# 处理命令有两个参数的情况
			actions[string.lower(cmd[0])](cmd[1],cmd[2])		# 调用与命令对应的函数
		else:
			print '输入错误'
	except:
		print '命令出错'
ftp.quit()									# 端口连接
