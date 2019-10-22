
import threading
import time

def hello(name):
    print(("hello %s\n" % name ))

    global timer
    timer = threading.Timer(2.0, hello, ["Hawk"])
    timer.start()


timer = threading.Timer(2.0, hello, ["Hawk"])
timer.start()
