from ..common import channel


def sampleChannel11():
    channel.ChannelManager.createChannel('sample')
    print('channel.ChannelManager.getChannels.len: ', len(channel.ChannelManager.getChannels()))
