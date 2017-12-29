# -*- coding:utf-8 -*-
# file: pyDirectSound.py
#
import pywintypes									# 导入模块
import struct
from win32com.directsound import directsound
import Tkinter
import tkFileDialog
WAV_HEADER_SIZE = struct.calcsize('<4sl4s4slhhllhh4sl')					# 设置WAV头
class Window:
	def __init__(self):
		self.root = root = Tkinter.Tk()						# 创建组件
		buttonAdd = Tkinter.Button(root, text = 'Add',
				command = self.add)
		buttonAdd.pack(side = 'left')
		buttonPlay = Tkinter.Button(root, text = 'Play',
				command = self.play)
		buttonPlay.pack(side = 'left')
		buttonStop = Tkinter.Button(root, text = 'Stop',
				command = self.stop)
		buttonStop.pack(side = 'left')
	def MainLoop(self):								# 进入消息循环
		self.root.mainloop()
	def add(self):									# 添加播放文件
		self.file = tkFileDialog.askopenfilename(
				title = 'Python DirectSound',
				filetypes=[('WAV', '*.wav')])
	def play(self):									# 播放文件
		f = open(self.file, 'rb')						# 打开文件
		header = f.read(WAV_HEADER_SIZE)					# 读取WAV文件头
		(riff, riffsize, wave, fmt, fmtsize, 
			format, nchannels, samplespersecond,
			datarate, blockalign, bitspersample, 
			data, size) =\
	 	struct.unpack('<4sl4s4slhhllhh4sl', header)				# 获取参数值
	    	if riff != 'RIFF' or fmtsize != 16 or fmt != 'fmt ' or data != 'data':	# 判断文件格式
			raise 'Data Error'
		wfx = pywintypes.WAVEFORMATEX()						# 创建WAVEFORMATEX结构
		wfx.wFormatTag = format
		wfx.nChannels = nchannels
		wfx.nSamplesPerSec = samplespersecond
		wfx.nAvgBytesPerSec = datarate
		wfx.nBlockAlign = blockalign
		wfx.wBitsPerSample = bitspersample
		d = directsound.DirectSoundCreate(None, None)				# 使用DirectSound播放声音
		d.SetCooperativeLevel(None, directsound.DSSCL_PRIORITY)
		sdesc = directsound.DSBUFFERDESC()
		sdesc.dwFlags = (
				directsound.DSBCAPS_STICKYFOCUS | 
				directsound.DSBCAPS_CTRLPOSITIONNOTIFY
				)
		sdesc.dwBufferBytes = size
		sdesc.lpwfxFormat = wfx
		self.buffer = buffer = d.CreateSoundBuffer(sdesc, None)
		buffer.Update(0, f.read(size))
		buffer.Play(0)
	def stop(self):
		self.buffer.Stop()							# 停止
window = Window()
window.MainLoop()
