import socket
import re

ANY = "192.168.91.253"
# ANY = "0.0.0.0"
DES_IP = "239.255.255.250"
SRC_PORT = 1000
DES_PORT = 3702
# xml_str = b'<?xml version="1.0" encoding="utf-8"? <Probe <Uuid B2D5D4D2-808C-40F6-87CD-694C05C2B274</Uuid <Types inquiry</Types </Probe  '
# xml_str = b'<?xml version="1.0" encoding="utf-8"? <Probe <Uuid CB09F608-E016-4EE8-869A-CA186852F12E</Uuid <Types inquiry</Types </Probe  '

#xml_str = b'<?xml version="1.0" encoding="utf-8"?><Envelope xmlns:dn="http://www.onvif.org/ver10/network/wsdl" xmlns="http://www.w3.org/2003/05/soap-envelope"><Header><wsa:MessageID xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">uuid:fc0bad56-5f5a-47f3-8ae2-c94a4e907d70</wsa:MessageID><wsa:To xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">urn:schemas-xmlsoap-org:ws:2005:04:discovery</wsa:To><wsa:Action xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">http://schemas.xmlsoap.org/ws/2005/04/discovery/Probe</wsa:Action></Header><Body><Probe xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.xmlsoap.org/ws/2005/04/discovery"><Types>dn:NetworkVideoTransmitter</Types><Scopes /></Probe></Body></Envelope>';
xml_str = b'<?xml version="1.0" encoding="utf-8"?><Envelope xmlns:tds="http://www.onvif.org/ver10/device/wsdl" xmlns="http://www.w3.org/2003/05/soap-envelope"><Header><wsa:MessageID xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">uuid:75e13db0-cb89-4e4c-af62-676968d06db5</wsa:MessageID><wsa:To xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">urn:schemas-xmlsoap-org:ws:2005:04:discovery</wsa:To><wsa:Action xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">http://schemas.xmlsoap.org/ws/2005/04/discovery/Probe</wsa:Action></Header><Body><Probe xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.xmlsoap.org/ws/2005/04/discovery"><Types>tds:Device</Types><Scopes /></Probe></Body></Envelope>'
xml_str2= b'<?xml version="1.0" encoding="utf-8"?><Envelope xmlns:dn="http://www.onvif.org/ver10/network/wsdl" xmlns="http://www.w3.org/2003/05/soap-envelope"><Header><wsa:MessageID xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">uuid:418bd753-a01d-4c97-942d-17683257cd01</wsa:MessageID><wsa:To xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">urn:schemas-xmlsoap-org:ws:2005:04:discovery</wsa:To><wsa:Action xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">http://schemas.xmlsoap.org/ws/2005/04/discovery/Probe</wsa:Action></Header><Body><Probe xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.xmlsoap.org/ws/2005/04/discovery"><Types>dn:NetworkVideoTransmitter</Types><Scopes /></Probe></Body></Envelope>'

# 创建UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# 允许端口复用
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 绑定监听多播数据包的端口
s.bind((ANY, SRC_PORT))
# 声明该socket为多播类型
s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 255)
# 加入多播组，组地址由第三个参数制定
s.setsockopt(
  socket.IPPROTO_IP,
  socket.IP_ADD_MEMBERSHIP,
  socket.inet_aton(DES_IP) + socket.inet_aton(ANY)
)
s.setblocking(False)
s.sendto(xml_str, (DES_IP, DES_PORT))
s.sendto(xml_str2, (DES_IP, DES_PORT))
while True:
  try:
    data, address = s.recvfrom(4096)
  except Exception as e:
    # print(e)
    pass
  else:
    print(address)
    # print(data)
    try:
      IPv4 = re.search(re.compile(r"<IPv4Address (.*?)</IPv4Address ", re.S), str(data))[1]
      MAC = re.search(re.compile(r"<MAC (.*?)</MAC ", re.S), str(data))[1]
    except TypeError:
      pass
    else:
      # print(data)
      print("IPv4: {}".format(IPv4))
      print("MAC: {}".format(MAC))