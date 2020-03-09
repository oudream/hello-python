import sys
import os
import glob


def TestDir1():
    # @classmethod
    def scan1():
        for root, dirs, files in os.walk("F:\\vmware"):
            for file in files:
                print((os.path.join(root, file).encode('utf-8')))
            for dir in dirs:
                print((os.path.join(root, dir).encode('utf-8')))

    # @staticmethod
    def scan2():
        for filename in os.listdir(r'F:\\vmware'):
            print(filename)

    # @staticmethod
    def scan3():
        for filename in glob.glob(r'F:\\vmware\\**\\*.vmdk', recursive=True):
            # for filename in glob.glob(r'F:\\vmware\\*\\*.vmdk', recursive=True):
            # for filename in glob.glob(r'F:\\vmware\\*\\*\\*.vmdk', recursive=True):
            print(filename)

    # @staticmethod
    def scan4():
        if sys.version_info < (3, 0):
            def processDirectory(args, dirname, filenames):
                print(('Directory', dirname))
                for filename in filenames:
                    print((' File', filename))

            os.path.walk(r'F:\\vmware', processDirectory, None)

    print('-----------------------------------------------------------------------------------------------------------')
    print('----scan1------scan1-----scan1-----------------------------------------------------------------------------')
    print('-----------------------------------------------------------------------------------------------------------')
    scan1()
    print('\n\n\n')
    print('-----------------------------------------------------------------------------------------------------------')
    print('----scan2------scan2-----scan2-----------------------------------------------------------------------------')
    print('-----------------------------------------------------------------------------------------------------------')
    scan2()
    print('\n\n\n')
    print('-----------------------------------------------------------------------------------------------------------')
    print('----scan3------scan3-----scan3-----------------------------------------------------------------------------')
    print('-----------------------------------------------------------------------------------------------------------')
    scan3()
    print('\n\n\n')
    print('-----------------------------------------------------------------------------------------------------------')
    print('----scan4------scan4-----scan4-----------------------------------------------------------------------------')
    print('-----------------------------------------------------------------------------------------------------------')
    scan4()


# TestDir1()

def testCreateDir():
    sPath = 'f:/d/dd/ddd/a/aa/aaa'
    if not os.path.exists(sPath):
        os.makedirs(sPath)
    print((os.path.isdir(sPath)))


testCreateDir()
