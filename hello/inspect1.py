import inspect

frameinfo = inspect.getframeinfo(inspect.currentframe())

print((frameinfo.filename, frameinfo.lineno))