#!/usr/bin/env python3
# coding: utf-8

#---------------------------------------------
#  绿塘煤矿业务
#  卢良斌
#  2018/03/27
# ---------------------------------------------
#
import os,sys,datetime,time
import sqlite3
from gcl_sdk import *

from wt_lpr import WT_LPR, EPIntegrateBox, LOCATION, CAMERA_TIME, \
    IMAGE_INFO, CLIENT_LPRC_PLATE_RESULTEX, \
    CLIENT_LPRC_DEVDATA_INFO, \
    CALLBACK_CONNECTION_CHANGED, CALLBACK_JPEG_STERAM, CALLBACK_REC_RESULT
from ctypes import CFUNCTYPE, POINTER, c_char_p, c_uint, c_ulong


class WT_IPC:

    def __init__(self):
        self.ip = None
        self.lpr = WT_LPR()
        self.box = EPIntegrateBox()
        self.txt = []
        self.connnect = False
        self.last_time_con = 0
        self.last_time_test = 0
        self.status = -1
        self.conn = sqlite3.connect('lpr.db', check_same_thread = False)

    def init(self,ip):
        self.ip = ip

    def reconnet(self):
            if (time.time() - self.last_time_con)>60:
                print("check connec")
                self.last_time_con = time.time()
                if self.lpr.check_con_status(self.ip)>0:
                    self.connect_dev()

    def test(self):
        if self.connnect:
            if (time.time() - self.last_time_test)>60:
                self.last_time_test = time.time()
                self.play_tts('热烈欢迎')
                self.trigger()

    def connect_dev(self):
        if self.lpr.connect_dev(self.ip):
            self.connnect = True
            self.init_box()
        else:
            self.connnect = False

    def init_box(self):
        if  self.connnect:
            self.box.set_volume(100, ip=self.ip)
            self.box.display('远光共创', 1, ip=self.ip)
            self.box.display('欢迎你~', 2, ip=self.ip)
            self.box.display('        ', 3, ip=self.ip)
            self.box.display('        ', 4, ip=self.ip)

    def disconnect_dev(self):
        if  self.connnect:
            self.lpr.disconnect_dev(self.ip)
            self.connnect = False

    def trigger(self):
        if  self.connnect:
           self.lpr.trigger(self.ip)

    def open_gate(self):
        if  self.connnect:
            self.lpr.open_gate(self.ip)

    def close_gate(self):
        if  self.connnect:
            self.lpr.close_gate(self.ip)

    def play_tts(self,txt):
        if self.connnect:
            self.box.tts(txt,self.ip)

    def ip_valid(self):
        if not self.ip:
            return False
        return True

    def deal_lprc_connect(self,ip,status, userdata):
        if status != self.status:
            self.status = status
            print('{} status changed: {}'.format(ip, status))

    def deal_lprc_rec_data(self, data, userdata):
        content = data.contents
        print('识别结果：{}[{}]@{}，可信度：{}'.format(
            content.license.decode('gbk'),
            content.color.decode('gbk'),
            content.ip.decode('gbk'), content.confidence))
        jpeg_data = bytearray(content.full_image.length)
        for i in range(content.full_image.length):
            jpeg_data[i] = content.full_image.buff[i]
        self.update_result(content.license.decode('gbk'), content.confidence, jpeg_data)

    def deal_lprc_jpeg_stream(self,dat, userdata):
        content = dat.contents
        jpeg_data = bytearray(content.length)
        for i in range(content.length):
            jpeg_data[i] = content.data[i]

#      self.update_image(jpeg_data)


    def update_result(self, license, confidence, jpeg_data=None):

        # now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        cur = self.conn.cursor()
        # 保存记录
        # cur.execute('insert into result (licence, confidence, _datetime) values(?,?,?)', (license, confidence, now))
        # self.conn.commit()

        # 查询车主
        cur.execute('select ower from LP where licence=? and enabled=1', (license, ))
        ret = cur.fetchone()
        if not ret:
            self.box.display('尚未登记', 3, color=1, ip=self.ip)
            self.box.display('        ', 4, ip=self.ip)
            self.box.tts(text='车辆未登记，请联系相关负责人', ip=self.ip)
            return

        txt = '{} 欢迎光临'.format(ret[0])
        self.box.tts(text=txt, ip=self.ip)
        self.box.display(license, 3, color=3, ip=self.ip)
        self.box.display(ret[0], 4, ip=self.ip)

class WT_IPC_CB:
    def __init__(self,obj):
        self.parent=obj
        self.cb_status = False

    def set_callbacks(self,ip):
        if not self.cb_status :
            obj =  self.parent.get_ipc(ip)
            if obj:
                obj.lpr.set_callback_rec_result(self.callback_lprc_rec_data)
                obj.lpr.set_callback_connect_status(self.callback_lprc_connect)
                # obj.lpr.set_callback_jpeg_stream(self.callback_lprc_jpeg_stream)
                self.cb_status = True
                print('set_callbacks',ip)

    @CALLBACK_CONNECTION_CHANGED
    def callback_lprc_connect(self, ip, status, userdata):
        # print('callback_lprc_connect',ip)
        obj =  self.parent.get_ipc(ip)
        if obj:
            obj.deal_lprc_connect(ip, status, userdata)
        else:
            print('callback_lprc_connect obj is null',ip)

    @CALLBACK_REC_RESULT
    def callback_lprc_rec_data(self, data, userdata):
        content = data.contents
        print('callback_lprc_rec_data',content.ip)
        obj =  self.parent.get_ipc(content.ip)
        if obj:
            obj.deal_lprc_rec_data(data,userdata)
        else:
            print('callback_lprc_rec_data obj is null',content.ip)


    @CALLBACK_JPEG_STERAM
    def callback_lprc_jpeg_stream(self, data, userdata):
        content = data.contents
        # print('callback_lprc_jpeg_stream',content.ip)
        obj =  self.parent.get_ipc(content.ip)
        if obj:
            obj.deal_lprc_jpeg_stream(data,userdata)
        # else:
            # print('callback_lprc_jpeg_stream obj is null',content.ip)


# 绿塘煤矿车牌识别业务
class LT_BI:
    def __init__(self):
       self.ipcs = []
       self.ipc_cb = WT_IPC_CB(self)

    def append(self,ip):
        ipc = WT_IPC()
        ipc.init(ip)
        self.ipcs.append(ipc)
        self.ipc_cb.set_callbacks(ip)

    def get_ipc(self,ip):
        #sIp = ip.decode('GBK')
        for e in self.ipcs:
            if e.ip.encode('GBK') == ip or e.ip == ip:
                return e
        return None

    def work(self):
        mySdk = GCL_SDK()

        iAttach = GCL_PSM_ATTACH()
        iAttach.reason = 0
        iAttach.containerId = 0
        iAttach.sourceId = 1
        iAttach.targetId = 1
        iAttach.tag = 0

        iYx = GCL_YX_T()
        iYc = GCL_YC_T()
        iYw = GCL_YW_T()

        iYx.address = 0x01000000
        iYx.value = 0
        iYx.quality = 1
        iYx.datetime = 0

        iYc.address = 0x02000000
        iYc.value = 0.0
        iYc.quality = 1
        iYc.datetime = 0

        print(iAttach,iAttach.sourceId)

        print(len(sys.argv))

        for i in range(0, len(sys.argv)):
            print ("pram", i, sys.argv[i])

        print ("path",os.path.abspath('.'))

        pStr  = c_char_p()
        sTemp = os.path.abspath('.')+"\\"
        pStr.value = sTemp.encode('gbk')

        mySdk.init(1,byref(pStr))

        while True:
            for ipc in self.ipcs:
                ipc.reconnet()
                # ipc.test()

            yxs = []

            yxs.append(iYx)
            iRet = mySdk.send_yx_array(yxs)
            iYx.address+=1
            iYx.value += 1

            if iYx.address>0x0100000F:
                iYx.address = 0x01000000

            ycs = []
            ycs.append(iYc)
            iRet = mySdk.send_yc_array(ycs)

            iYc.address += 1
            iYc.value   += 1.1

            if iYc.address>0x0200000F:
                iYc.address = 0x02000000

            time.sleep(1)

        mySdk.uninit()

if __name__ == '__main__':
    ltbi = LT_BI()
    ltbi.append('10.31.58.113')
    ltbi.work()
