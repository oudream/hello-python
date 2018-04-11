import os
import const_value

def TestFileWrite1():
    try:
        f = open("t:/a.txt", 'w')
        if f != None:
            for i in range(10):
                f.write(str(i) + '\n')
            f.close()
    except (IOError) as e:
        print(str(e))


def replaceFilesBytes(sPath):
    const = const_value.ConstValue()
    const.CHUNK_SIZE = 2048

    print(sPath)

    def read(file_obj):
        """
        逐件读取文件
        默认块大小：2KB
        """
        while True:
            data = file_obj.read(const.CHUNK_SIZE)  # 每次读取指定的长度
            if not data:
                break
            yield data

    def replace(chuck):
        newChuck = bytes(1024)

    def replaceFileBytes(sFilePath):
        with open(sFilePath, 'rb', encoding='utf-8') as f:
            for chuck in read(f):
                replace(chuck)

    for root, dirs, files in os.walk(sPath):
        for file in files:
            print((os.path.join(root, file).encode('utf-8')))
        for dir in dirs:
            print((os.path.join(root, dir).encode('utf-8')))


if __name__ == '__main__':
    replaceFilesBytes(r'F:\gcl3deploy\data\gcl_svr_rtdbs\20180326')
    # TestFileWrite1()
else:
    replaceFilesBytes(r'F:\gcl3deploy\data\gcl_svr_rtdbs\20180326')

