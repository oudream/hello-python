#!/usr/bin/env python3
# coding: utf-8

"""
文通车牌识别
"""

from ctypes import WINFUNCTYPE, CFUNCTYPE, CDLL, WinDLL
from ctypes import c_int, c_uint, c_ulong, c_ubyte, c_char_p, c_void_p, c_char
from ctypes import Structure, POINTER
from ctypes.wintypes import HWND, UINT


class LOCATION(Structure):
    _fields_ = [
        ('left', c_int),
        ('top', c_int),
        ('right', c_int),
        ('bottom', c_int)
    ]
    
class CAMERA_TIME(Structure):
    _fields_ = [
        ('year', c_int),
        ('month', c_int),
        ('day', c_int),
        ('hour', c_int),
        ('minute', c_int),
        ('second', c_int),
        ('millisecond', c_int)
    ]
    
class IMAGE_INFO(Structure):
    _fields_ = [
        ('width', c_int),
        ('height', c_int),
        ('pitch', c_int),
        ('length', c_int),
        ('reserved', c_char*16),
        ('buff', POINTER(c_ubyte))
    ]
    
class CLIENT_LPRC_PLATE_RESULTEX(Structure):
    _fields_ = [
        ('ip', c_char*16),
        ('color', c_char*8),
        ('license', c_char*16),
        ('location', LOCATION),
        ('shoot_time', CAMERA_TIME),
        ('confidence', c_int),
        ('time', c_int),
        ('direction', c_int),
        ('reserved', c_char*256),
        ('full_image', IMAGE_INFO),
        ('plate_image', IMAGE_INFO)
    ]
    
class CLIENT_LPRC_DEVDATA_INFO(Structure):
    _fields_ = [
        ('ip', c_char*16),
        ('data', POINTER(c_ubyte)),
        ('length', c_ulong),
        ('status', c_int),
        ('reserved', c_char*128)
    ]

def method(prototype):
    class MethodDescriptor(object):
        def __init__(self, func):
            self.func = func
            self.bound_funcs = {} # hold on to references to prevent gc
        def __get__(self, obj, type=None):
            assert obj is not None # always require an instance
            try: return self.bound_funcs[obj,type]
            except KeyError:
                ret = self.bound_funcs[obj,type] = prototype(
                    self.func.__get__(obj, type))
                return ret
    return MethodDescriptor

CALLBACK_CONNECTION_CHANGED = method(CFUNCTYPE(None, c_char_p, c_uint, c_ulong))
CALLBACK_JPEG_STERAM = method(CFUNCTYPE(None, POINTER(CLIENT_LPRC_DEVDATA_INFO), c_ulong))
CALLBACK_REC_RESULT = method(CFUNCTYPE(None, POINTER(CLIENT_LPRC_PLATE_RESULTEX), c_ulong))

class WT_LPR:
    def __init__(self):
        self.lib = WinDLL('WTY.dll')
        self.set_image_path('d:\\tmp')

    def set_callback_rec_result(self, fn):
        self.lib.CLIENT_LPRC_RegDataEx2Event(fn)
        
    def set_callback_connect_status(self, fn):
        self.lib.CLIENT_LPRC_RegCLIENTConnEvent(fn)
        
    def set_callback_jpeg_stream(self, fn):
        self.lib.CLIENT_LPRC_RegJpegEvent(fn)

    def set_image_path(self, path):
        if path[-1] != '\\':
            path += '\\'
            
        self.lib.CLIENT_LPRC_SetSavePath(path.encode('GBK'))
        
    def connect_dev(self, ip, port=8080):
        prototype = WINFUNCTYPE(c_int, UINT, HWND, UINT, c_char_p, c_ulong)
        paramflags = (1, 'port'), (1, 'hWndHandle', None), (1, 'uMsg', 0), (1, 'ip'), (1, 'dwUser', 0)
        sdk_init = prototype(('CLIENT_LPRC_InitSDK', self.lib), paramflags)
        
        _ip = ip.encode('GBK')
        if sdk_init(ip=_ip, port=port) == 0:
            print('Connected {} {}.'.format(ip, self.lib.WTY_CheckStatus(_ip)))            
            return True
            
        print('Cannot connecte to {}.'.format(ip))
        return False
        
    def disconnect_dev(self, ip):
        if self.lib.CLIENT_LPRC_QuitDevice(ip.encode('GBK')) == 0:
            print('Disconnect from {}.'.format(ip))
            return True
            
        print('Cannot disconnect from {}.'.format(ip))
        return False

    def open_gate(self, ip, port=9110):
        # 道闸抬杆
        if self.lib.CLIENT_LPRC_SetRelayClose(ip.encode('GBK'), port) == 0:
            print('Ok')
            return True
            
        print('Fail.')
        return False
        
    def close_gate(self, ip, port=9110):
        # 道闸落杆
        if self.lib.CLIENT_LPRC_DropRod(ip.encode('GBK'), port) == 0:
            print('Ok')
            return True
            
        print('Fail.')
        return False
        
    def trigger(self, ip, port=8080):
        if self.lib.CLIENT_LPRC_SetTrigger(ip.encode('GBK'), port) == 0:
            print('Triggered.')
            return True
            
        print('Fail.')
        return False
        
    def reg_data_evt(self, dat, user):
        print('reg_data_evt')

    def check_con_status(self,ip):
        return self.lib.WTY_CheckStatus(ip.encode('GBK'))

    def __del__(self):
        self.lib.CLIENT_LPRC_QuitSDK()
        
class EPIntegrateBox:
    def __init__(self, ip=None):
        self.dll = CDLL('EPIntegrateBox.dll')
        self.box_type = 4
        self.trans_type = 3
        self.ip_addr = ip

    def set_volume(self, level, ip=None):
        if ip is None:
            ip_addr = self.ip_addr
        else:
            ip_addr = ip

        if ip_addr is None:
            return False

        r = self.dll.EP_SetVolumeEx(self.box_type, \
            ip_addr.encode('gbk'), 
            self.trans_type,
            level, 
            False)
        print('vol: ', r)

    def display(self, text, line_num, color=2, ip=None):
        if ip is None:
            ip_addr = self.ip_addr
        else:
            ip_addr = ip

        if ip_addr is None:
            return False

        r = self.dll.EP_DisplayEx(self.box_type, \
            ip_addr.encode('gbk'), 
            line_num, 
            text.encode('gbk'),
            color, 
            self.trans_type,
            False)

        return r == 1

    def tts(self, text, ip=None, _type=0):
        if ip is None:
            ip_addr = self.ip
        else:
            ip_addr = ip

        if ip_addr is None:
            return False

        text_encode = text.encode('gbk')
        r = self.dll.EP_PlayVoiceEx(self.box_type, \
            ip_addr.encode('gbk'), 
            _type, 
            text_encode,
            self.trans_type,
            False)
        
        return r == 1

if __name__ == '__main__':
    import time
    
    #typedef void (*CLIENT_LPRC_DataEx2Callback)(CLIENT_LPRC_PLATE_RESULTEX *recResultEx,LDWORD dwUser);
    @CFUNCTYPE(None, POINTER(CLIENT_LPRC_PLATE_RESULTEX), c_ulong)
    def callback_data_ex2(dat, user):
        content = dat.contents
        print('识别结果：{}[{}]@{}，可信度：{}'.format(
            content.license.decode('gbk'), 
            content.color.decode('gbk'), 
            content.ip.decode('gbk'), content.confidence))
            
    # typedef void (*CLIENT_LPRC_ConnectCallback)(char *chCLIENTIP, UINT nStatus, LDWORD dwUser)
    @CFUNCTYPE(None, c_char_p, c_uint, c_ulong)
    def callback_lprc_connect(ip, status, userdata):
        #if status != conn_status:
        #    conn_status = status
        #    print('{} status changed: {}'.format(ip, status))
        pass
    
    target = '10.31.58.113'
    
    lpr = WT_LPR()
    
    lpr.set_callback_connect_status(callback_lprc_connect)
    lpr.set_callback_rec_result(callback_data_ex2)
    
    lpr.connect_dev(target)
    #lpr.open_gate(target)
    
    lpr.trigger(target)
    
    while True:
        try:
            time.sleep(5)
            
        except KeyboardInterrupt:
            break
        
    lpr.disconnect_dev(target)
    