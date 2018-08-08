from . import channel


class ChannelUdp(channel.ChannelBase):
    def __init__(self, name):
        channel.ChannelBase.__init__(self, name)
        # super(channel.ChannelBase, self).__init__(self, name)
        self.name += '.udp'
