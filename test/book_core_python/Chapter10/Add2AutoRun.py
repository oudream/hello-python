#  -*- coding: iso-8859-1 -*-
#  file: Add2AutoRun.py
#
import win32api
import win32con
# ÒªÌí¼ÓµÄÏîÖµÃû³Æ
name = 'SetIE'
# ÒªÌí¼ÓµÄPython½Å±¾µÄÂ·¾¶
path = 'C:\\SetIE.py'
# ×¢²á±íÏîÃû
KeyName = 'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
# Òì³£´¦Àí
try:
    # ´ò¿ª×¢²á±íÏî
    key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,\
                              KeyName,\
                              0,\
                              win32con.KEY_ALL_ACCESS)
    # ÉèÖÃÏîÖµ
    win32api.RegSetValueEx(key, name, 0, win32con.REG_SZ, path)
    # ¹Ø±Õ×¢²á±í
    win32api.RegCloseKey(key)
except:
    print 'error'
print 'added that!'
