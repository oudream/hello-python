#  -*- coding:utf-8 -*-
#  file: ModifyMemory.py
#
from ctypes import *
# 定义_PROCESS_INFORMATION结构体
class _PROCESS_INFORMATION(Structure):
	_fields_ = [('hProcess', c_void_p),
		    ('hThread', c_void_p),
		    ('dwProcessId', c_ulong),
		    ('dwThreadId', c_ulong)]
# 定义_STARTUPINFO结构体
class _STARTUPINFO(Structure):
	_fields_ = [('cb',c_ulong),
  		    ('lpReserved', c_char_p),  
  		    ('lpDesktop', c_char_p),  
  		    ('lpTitle', c_char_p), 
  		    ('dwX', c_ulong),
  		    ('dwY', c_ulong), 
  		    ('dwXSize', c_ulong),
  		    ('dwYSize', c_ulong), 
  		    ('dwXCountChars', c_ulong),
  		    ('dwYCountChars', c_ulong), 
  		    ('dwFillAttribute', c_ulong), 
  		    ('dwFlags', c_ulong),
  		    ('wShowWindow', c_ushort),  
  		    ('cbReserved2', c_ushort), 
  		    ('lpReserved2', c_char_p),  
  		    ('hStdInput', c_ulong),  
  		    ('hStdOutput', c_ulong),
  		    ('hStdError', c_ulong)]
# 定义NORMAL_PRIORITY_CLASS
NORMAL_PRIORITY_CLASS = 0x00000020
# 加载kernel32.dll
kernel32 = windll.LoadLibrary("kernel32.dll")
# 获得CreateProcess函数地址
CreateProcess = kernel32.CreateProcessA
# 获得ReadProcessMemory函数地址
ReadProcessMemory = kernel32.ReadProcessMemory
# 获得WriteProcessMemory函数地址
WriteProcessMemory = kernel32.WriteProcessMemory
TerminateProcess = kernel32.TerminateProcess
# 声明结构体
ProcessInfo = _PROCESS_INFORMATION()
StartupInfo = _STARTUPINFO()
# 要进行修改的文件
file = 'ModifyMe.exe'
# 要修改的内存地址
address = 0x0040103c
# 缓冲区地址
buffer = c_char_p("_") 
# 读入的字节数
bytesRead = c_ulong(0)
# 缓冲区大小
bufferSize =  len(buffer.value)
# 创建进程
if CreateProcess(file, 0, 0, 0, 0, NORMAL_PRIORITY_CLASS, 0, 0, byref(StartupInfo), byref(ProcessInfo)):
	# 读取要修改的内存地址，以判断是否是要修改的文件
	if ReadProcessMemory(ProcessInfo.hProcess, address, buffer, bufferSize, byref(bytesRead)):
		if buffer.value == '\x74':
			# 修改缓冲区内值，将其写入内存
			buffer.value = '\x75'
			# 修改内存
			if WriteProcessMemory(ProcessInfo.hProcess, address, buffer, bufferSize, byref(bytesRead)):
				print '成功改写内存!'
			else:
				print '写内存错误!'
		else:
			print '打开了错误的文件!'
			# 如果不是要修改的文件，则终止进程
			TerminateProcess(ProcessInfo.hProcess,0)
	else:
		print '读内存错误!'
else:
	print '不能创建进程!'
