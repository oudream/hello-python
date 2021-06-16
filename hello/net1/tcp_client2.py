# 导入socket库:
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('192.168.91.200', 2402))
data = bytes.fromhex('68190004000600D20106013D27000000020309636F7572742E696E69')
# data = bytes.fromhex(
#     b'\x68\x19\x00\x04\x00\x06\x00\xD2\x01\x06\x01\x3D\x27\x00\x00\x00\x02\x03\x09\x63\x6F\x75\x72\x74\x2E\x69\x6E\x69')
s.send(data)
# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        print('recv data len: ', len(d))
    else:
        break
