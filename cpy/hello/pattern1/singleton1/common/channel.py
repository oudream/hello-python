class ChannelBase:
    def __init__(self, name):
        self.name = name
        print('ChannelBase New: ', self.name)

    def __del__(self):
        print('ChannelBase Del: ', self.name)


class ChannelManager:
    _channels = []

    @classmethod
    def createChannel(cls, name):
        channel = ChannelBase(name)
        cls._channels.append(channel)
        return channel

    @classmethod
    def findChannel(cls, name):
        for channel in cls._channels:
            if channel.name == name:
                return channel
        return None

    @classmethod
    def deleteChannel(cls, name):
        for i in range(len(cls._channels) - 1, -1, -1):
            channel = cls._channels[i]
            if channel.name == name:
                cls._channels.pop(i)
                return True
        return False

    __instance = None

    @classmethod
    def instance(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = cls(*args, **kwargs)
        return cls.__instance

    @classmethod
    def getChannels(cls):
        return cls._channels
