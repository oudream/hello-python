import os
import sys
import time
import datetime
import operator
import inspect
import re

# import test_inspect1
# import test_closure1
# import test_object1
# import test_dir1
# import test_list2dict1
# import test_copyfile1
# import test_inspect1

# s = os.path.basename(os.getcwd())

man = '''
    -sf /dirName/appName -tf /dirName
    -sf appName -ct debug|release
    -sf /dirName/appName
'''

print((sys.platform))

print((os.path.isabs(r'\a')))

frameinfo = inspect.getframeinfo(inspect.currentframe())

deployDir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(frameinfo.filename))))

print(deployDir)
print('---')

sf = frameinfo.filename

# sf =
print((os.getcwd()))
print((os.path.abspath(os.getcwd())))
print((os.path.dirname(os.path.abspath(os.getcwd()))))
print(sf)
print((os.path.dirname(os.path.abspath(sf))))

m = re.search('multi', 'A mUltiCased string', re.IGNORECASE)
print(m)

file = "Hello.py"
# 获取前缀（文件名称）
assert os.path.splitext(file)[0] == "Hello"
# 获取后缀（文件类型）
assert os.path.splitext(file)[-1] == ".py"
assert os.path.splitext(file)[-1][1:] == "py"
