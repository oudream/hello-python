import os

def TestFileWrite1():
    try:
        f = open("t:/a.txt", 'w')
        if f != None:
            for i in range(10):
                f.write(str(i)+'\n')
            f.close()
    except (IOError) as e:
        print str(e)


        
    
if __name__ == '__main__':
    TestFileWrite1()
