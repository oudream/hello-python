#!/usr/bin/env python3
# coding: utf-8

#---------------------------------------------
#  gcl_sdk python接口
#  卢良斌
#  2018/03/27
#---------------------------------------------

import os,sys,time,datetime
from ctypes import *
from struct import *
import ygct_common


#yx
class GCL_YX_T(Structure):
    _fields_:[
        ('address',c_int),
        ('value', c_int),
        ('quality', c_int),
        ('datetime', c_longlong)
        ]
#yc
class GCL_YC_T(Structure):
    _fields_:[
        ('address',c_int),
        ('value', c_double),
        ('quality', c_int),
        ('datetime', c_longlong)
        ]
#yw    
class GCL_YW_T(Structure):
    _fields_:[
        ('address',c_int),
        ('value', c_char*128),
        ('quality', c_int),
        ('datetime', c_longlong)
        ]
    
#attach    
class GCL_PSM_ATTACH(Structure):
    _fields_:[
        ('reason',c_int),
        ('containerId', c_int),
        ('sourceId', c_int),
        ('targetId', c_int),
        ('tag', c_int)
        ]


CALLBACK_SDK_ERR      = ygct_common.method(CFUNCTYPE(None, c_int))
CALLBACK_SDK_MSG      = ygct_common.method(CFUNCTYPE(None, c_char_p, c_char_p,c_int, POINTER(GCL_PSM_ATTACH)))
CALLBACK_SDK_FILE     = ygct_common.method(CFUNCTYPE(None, c_char_p,POINTER(GCL_PSM_ATTACH)))
CALLBACK_SDK_RT_REQ   = ygct_common.method(CFUNCTYPE(None, POINTER(GCL_PSM_ATTACH)))
CALLBACK_SDK_RT_REV   = ygct_common.method(CFUNCTYPE(None, c_int,c_char_p,c_int,c_int,POINTER(GCL_PSM_ATTACH)))



class GCL_SDK:
    def __init__(self):
        self.lib = CDLL("gcl_sdk")

    def reg_err_notify(self,fn):
        return self.lib.gci_register_error_notify(fn)

    def unreg_err_notify(self,fn):
        return self.lib.gci_unregister_error_notify(fn)
        
    def reg_msg_cmd_notify(self,fn):
        return self.lib.gci_register_message_command_notify(fn)
    
    def unreg_msg_cmd_notify(self,fn):
        return self.lib.gci_unregister_message_command_notify(fn)

    def reg_file_transfer_notify(self,fn):
        return self.lib.gci_register_file_transfer_notify(fn)
    
    def unreg_file_transfer_notify(self,fn):
        return self.lib.gci_unregister_file_transfer_notify(fn)
        
    def reg_file_transfer_result_notify(self,fn):
        return self.lib.gci_register_file_transfer_result_notify(fn)
    
    def unreg_file_transfer_result_notify(self,fn):
        return self.lib.gci_unregister_file_transfer_result_notify(fn)
        
    def reg_rt_rev_notify(self,fn):
        return self.lib.gci_register_realtime_data_post_notify(fn)
    
    def unreg_rt_rev_notify(self,fn):
        return self.lib.gci_unregister_realtime_data_post_notify(fn)
        
    def init(self,argc,argv):
        return self.lib.gci_init(argc,argv)

    def uninit(self):
        return self.lib.gci_cleanup()

    def send_msg(self,cmd,pram,lenth):
        return self.lib.gci_message_command_send(cmd,pram,lenth,None)

    def send_yx_array(self,v):
        if len(v) >0:
            buff = b''
            for e in v:
                buff += (pack('=iiiq',e.address, e.value, e.quality, e.datetime))                
            
            return self.lib.gci_realtime_data_post(0x01010203, buff, 20,len(v), None)
            
        return -1
            
    def send_yc_array(self,v):
        if len(v) >0:
            buff = b''            
            for e in v:
                buff += (pack('=idiq',e.address, e.value, e.quality, e.datetime))

            return self.lib.gci_realtime_data_post(0x0101021C,buff,24,len(v),None)
            
        return -1
               
    def send_yw_array(self,v):
        if len(v) >0:
            buff = b''            
            for e in v:
                buff += (pack('=isiq',e.address, e.value, e.quality, e.datetime))
                
            return self.lib.gci_realtime_data_post(0x0101022F,buff,144,len(v),None)
            

        return -1

