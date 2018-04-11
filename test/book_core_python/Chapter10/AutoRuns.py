#  -*- coding: iso-8859-1 -*-
#  file: AutoRuns.py
#
# µ¼ÈëËùÐèÒªµÄÄ£¿é
import string
from win32api import *
from win32con import *
# GetValuesº¯ÊýÓÃÓÚ»ñµÃÄ³×¢²á±íÏîÏÂËùÓÐµÄÏîÖµ
def GetValues(fullname):
    # °ÑÍêÕûµÄÏî²ð·Ö³É¸ùÏîºÍ×ÓÏîÁ½²¿·Ö
    name = string.split(fullname,'\\',1)
    # ´ò¿ªÏàÓ¦µÄÏî£¬ÎªÁËÈÃ¸Ãº¯Êý¸üÍ¨ÓÃ
    # Ê¹ÓÃÁË¶à¸öÅÐ¶ÏÓï¾ä
    if name[0] == 'HKEY_LOCAL_MACHINE':
        key = RegOpenKey(HKEY_LOCAL_MACHINE,name[1], 0, KEY_READ)
    elif name[0] == 'HKEY_CURRENT_USER':
        key = RegOpenKey(HKEY_CURRENT_USER,name[1], 0, KEY_READ)
    elif name[0] == 'HKEY_CLASSES_ROOT':
        key = RegOpenKey(HKEY_CLASSES_ROOT,name[1], 0, KEY_READ)
    elif name[0] == 'HKEY_CURRENT_CONFIG':
        key = RegOpenKey(HKEY_CURRENT_CONFIG,name[1], 0, KEY_READ)
    elif name[0] == 'HKEY_USERS':
        key = RegOpenKey(HKEY_USERS,name[1], 0, KEY_READ)
    else:
        print(('err,no key named %s' (name[0])))  
    # ²éÑ¯ÏîµÄÏîÖµÊýÄ¿     
    info = RegQueryInfoKey(key)
    # ±éÀúÏîÖµ»ñµÃÏîÖµÊý¾Ý
    for i in range(0,info[1]):
       ValueName = RegEnumValue(key, i)
       # µ÷ÕûÏîÖµÃû³Æ³¤¶È£¬Ê¹Êä³ö¸üºÃ¿´
       print((string.ljust(ValueName[0],20),ValueName[1]))
    # ¹Ø±Õ´ò¿ªµÄÏî
    RegCloseKey(key)
# ÒòÎªGetValuesº¯Êý±È½ÏÍ¨ÓÃ£¬¿ÉÒÔÔÚÆäËü½Å±¾ÖÐµ÷ÓÃ
# ÕâÀïÏÈ¼ì²é½Å±¾ÊÇ·ñ±»ÆäËü½Å±¾µ÷ÓÃ       
if __name__ == '__main__': 
    # ÒòÎªÒªÒª¼ì²éµÄÏî½Ï¶à£¬¹Ê½«½«Æä·ÅÔÚÁÐ±íÖÐ£¬±ãÓÚÔö¼õ  
    KeyNames = ['HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run',\
                'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce',\
                'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnceEx',\
                'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run',\
                'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce']
    # ±éÀúÁÐ±í£¬µ÷ÓÃGetValuesº¯Êý£¬Êä³öÏîÖµ
    for KeyName in KeyNames:
        print(KeyName)
        GetValues(KeyName) 
