class Human:
    def __init__(self):
        self._name = '_name'
        self.__name = '__name'
        self.name = 'name'

    def say(self):
        print(('i am ', self.__class__.__name__))


