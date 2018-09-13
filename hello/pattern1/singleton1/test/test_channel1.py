from ..common import channel


def testChannel11():
    channel.ChannelManager.createChannel('test')
    print('channel.ChannelManager.getChannels.len: ', len(channel.ChannelManager.getChannels()))
