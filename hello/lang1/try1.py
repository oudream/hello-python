print("hello world")

a = [1,2,4,6]

for i in a :
    print(i)

import os

try:
    f = open("c:/1.txt")
    print("F Close")
    if not f:
        pass
    f.close()
except IOError :
    print("IOError")
    pass


##with open("c:\\0.txt") as f:
##    for s in f:
##        print s
##
##f = open("c:\\0.txt")
##try:
##    f = open("c:\\0.txt")
##    if f != None:
##        s = f.readline()
##    print "1:%s" % s
##finally:
##    f.close()
##    
##print "end"
