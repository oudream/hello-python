import threading


def hello(name):
    print(("hello %s\n" % name))

    global timer
    global times
    times += 1
    if times > 5:
        return
    timer = threading.Timer(2.0, hello, ["Hawk"])
    timer.start()


times = 0

timer = threading.Timer(2.0, hello, ["Hawk"])
timer.start()
