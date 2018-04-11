from common import glovar


class Show:
    def showchange(self):
        if glovar.x != 1:
            print('show x change')
        else:
            print('show x=1')
