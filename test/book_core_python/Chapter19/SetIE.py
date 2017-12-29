#  -*- coding: utf-8 -*-
#  file: SetIE.py
#
import datetime
import string
import win32api
import win32con
import urllib
import re
# 要修改的注册表项
keyname = 'Software\Microsoft\Internet Explorer\Main'
# 要设置为主页的网址
page = 'www.python.org'
# 获取当前日期
today = datetime.date.today()
# 将日期格式化为xxxx年xx月xx日的形式
title = today.strftime('%Y')+'年'+today.strftime('%m')+'月'+today.strftime('%d')+'日'
# 天气预报地址，需根据需要修改
addr = 'http://weather.cn.yahoo.com/weather.html?city=%E5%AE%9C%E6%98%8C'
# 获取网页，并处理数据
data = urllib.urlopen(addr)
s = data.read()	
m = re.compile(r'(?<=dt_d...).+?(?=</div)',re.S|re.I|re.U)
weather = re.compile(r'(?<=ft1..).+?(?=</span)',re.S|re.I|re.U)
hitp = re.compile(r'(?<=hitp..).+?(?=</span)',re.S|re.I|re.U)
lotp = re.compile(r'(?<=lotp..).+?(?=</span)',re.S|re.I|re.U)
results = m.findall(s)
w = weather.findall(results[0])
ht = hitp.findall(results[0])
lt = lotp.findall(results[0])
data.close()
title = title + '【天气】' + w[0]+ '|' +  ht[0] + '/' + lt[0]
# 对title重新编码，防止乱码
title = title.decode('utf-8').encode('gbk')
# 异常处理
try:
    # 打开注册表项，获得句柄
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, keyname, 0, win32con.KEY_ALL_ACCESS)
    # 读取"Start Page"的项值数据
    StartPage = win32api.RegQueryValueEx(key, 'Start Page')
except:
    print 'error'
else:
    # 判断主页是否为要修改的主页，如果不是则修改
    if StartPage[0] != page:
        win32api.RegSetValueEx(key, 'Start Page', 0, win32con.REG_SZ, page)
    # 设置IE的标题栏为xxxx年xx月xx日
    win32api.RegSetValueEx(key, 'Window Title', 0, win32con.REG_SZ, title)
    # 关闭注册表
    win32api.RegCloseKey(key)    
