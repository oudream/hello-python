import os

def TestFileWrite1():
    try:
        f = open("/fff/001.txt", 'w')
        if f != None:
            bs = b'abc123'
            for i in range(10):
                # f.write(bs)
                f.write(bs)
            f.close()
    except (IOError) as e:
        print(str(e))


#
# if __name__ == '__main__':
#     TestFileWrite1()


def test_write1():
    with open("/fff/002.txt", "wb") as f:
        junk = b"\xCC" * 1028
        f.write(junk)

TestFileWrite1()

# test_write1()
