import threading

import time


def f(f_stop):
    # do something here ...
    if not f_stop.is_set():
        localtime = time.localtime(time.time())
        # call f() again in 60 seconds
        print("f - 本地时间为 :", localtime)
        threading.Timer(0.8, f, [f_stop]).start()


g_times = 0


def g(f_stop):
    global g_times
    g_times += 1
    if (g_times > 1):
        return
    # do something here ...
    if not f_stop.is_set():
        localtime = time.localtime(time.time())
        # call f() again in 60 seconds
        print("g - 本地时间为 :", localtime)
        threading.Timer(1.1, g, [f_stop]).start()


f_stop = threading.Event()
# start calling f now and every 60 sec thereafter
f(f_stop)
g(f_stop)

# stop the thread when needed
# f_stop.set()
