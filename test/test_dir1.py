import sys
import os
import glob


class TestDir1:
    @classmethod
    def scan1(cls):
        for root, dirs, files in os.walk("f:\\XMLSpy2013"):
            for dir in dirs:
                print(os.path.join(root, dir).encode('utf-8'))
            for file in files:
                print(os.path.join(root, file).encode('utf-8'))

    @staticmethod
    def scan2():
        for filename in os.listdir(r'f:\XMLSpy2013'):
            print(filename)

    @staticmethod
    def scan3():
        for filename in glob.glob(r'f:\XMLSpy2013\*.xml'):
            print(filename)

    @staticmethod
    def scan4():
        if sys.version_info < (3, 0):
            def processDirectory(args, dirname, filenames):
                print('Directory', dirname)
                for filename in filenames:
                    print(' File', filename)

            os.path.walk(r'f:\XMLSpy2013', processDirectory, None)


TestDir1.scan1()
print('\n\n\n')
TestDir1.scan2()
print('\n\n\n')
TestDir1.scan3()
print('\n\n\n')
TestDir1.scan4()
