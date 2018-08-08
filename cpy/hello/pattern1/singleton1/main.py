import inspect
import sys

print(sys.path)

from .common import channel
from .test import test_channel1
from .common import channel_udp
from .common import channel_tcp
from .common.suba.subb import channel_b
from .sample import sample_channel1

class Main:
    pass


#
# print('-----xxxxxxx-----')
#
# path = os.path.dirname(channel.__file__)
# print('module.filePath: ', path)
#
# print('inspect: ', __doc__)
# print('inspect: ', inspect.getsourcefile(Main))
#
moduleMain = inspect.getmodule(Main)
print('inspect: ', moduleMain)

sample_channel1.sampleChannel11()
test_channel1.testChannel11()

channel.ChannelManager.createChannel('a')
channel.ChannelManager.createChannel('b')
upd = channel_udp.ChannelUdp('c')
tcp = channel_tcp.ChannelTcp('e')
b = channel_b.ChannelB('f')

test_channel1.testChannel11()
sample_channel1.sampleChannel11()

if __name__ == '__main__':
    print('i am main...: ', __name__)
    print('locals(): ')
    d = dict(locals())
    for k, v in d.items():
        print(k, v)
