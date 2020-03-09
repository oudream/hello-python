# # Python模块学习——optparse - Jack.gao - 博客园
# # https://www.cnblogs.com/captain_jack/archive/2011/01/11/1933366.html
# Python 有两个内建的模块用于处理命令行参数：
#
# 一个是 getopt，《Deep in python》一书中也有提到，只能简单处理 命令行参数；
#
# 另一个是 optparse，它功能强大，而且易于使用，可以方便地生成标准的、符合Unix/Posix 规范的命令行说明。

import sys

from optparse import OptionParser

[...]
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()


if __name__ == '__main__':
    print((sys.argv))

