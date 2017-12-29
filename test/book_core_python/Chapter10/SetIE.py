#  -*- coding: iso-8859-1 -*-
#  file: SetIE.py
#
import datetime
import string
import win32api
import win32con
# ÒªÐÞ¸ÄµÄ×¢²á±íÏî
keyname = 'Software\Microsoft\Internet Explorer\Main'
# ÒªÉèÖÃÎªÖ÷Ò³µÄÍøÖ·
page = 'www.python.org'
# »ñÈ¡µ±Ç°ÈÕÆÚ
today = datetime.date.today()
# ½«ÈÕÆÚ¸ñÊ½»¯ÎªxxxxÄêxxÔÂxxÈÕµÄÐÎÊ½
title = today.strftime('%Y')+'Äê'+today.strftime('%m')+'ÔÂ'+today.strftime('%d')+'ÈÕ'
# Òì³£´¦Àí
try:
    # ´ò¿ª×¢²á±íÏî£¬»ñµÃ¾ä±ú
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, keyname, 0, win32con.KEY_ALL_ACCESS)
    # ¶ÁÈ¡"Start Page"µÄÏîÖµÊý¾Ý
    StartPage = win32api.RegQueryValueEx(key, 'Start Page')
except:
    print 'error'
else:
    # ÅÐ¶ÏÖ÷Ò³ÊÇ·ñÎªÒªÐÞ¸ÄµÄÖ÷Ò³£¬Èç¹û²»ÊÇÔòÐÞ¸Ä
    if StartPage[0] != page:
        win32api.RegSetValueEx(key, 'Start Page', 0, win32con.REG_SZ, page)
    # ÉèÖÃIEµÄ±êÌâÀ¸ÎªxxxxÄêxxÔÂxxÈÕ
    win32api.RegSetValueEx(key, 'Window Title', 0, win32con.REG_SZ, title)
    # ¹Ø±Õ×¢²á±í
    win32api.RegCloseKey(key)    