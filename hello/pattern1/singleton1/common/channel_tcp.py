from . import channel


class ChannelTcp(channel.ChannelBase):
    def __init__(self, name):
        channel.ChannelBase.__init__(self, name)
        # super(channel.ChannelBase, self).__init__(self, name)
        self.name += '.tcp'


# print('inspect: ')
# print(inspect.getsourcefile(ChannelTcp))
