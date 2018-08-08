from ... import channel


class ChannelB(channel.ChannelBase):
    def __init__(self, name):
        channel.ChannelBase.__init__(self, name)
        # super(channel.ChannelBase, self).__init__(self, name)
        self.name += '.b'


# print('inspect: ')
# print(inspect.getsourcefile(ChannelTcp))

print('i am subb:', __package__)