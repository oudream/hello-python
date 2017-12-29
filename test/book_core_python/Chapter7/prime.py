# -*- coding:utf-8 -*-
# file: prime.py
#
import math
# isprime函数判断一个整数是否为素数。
# 如果i能被2到i的平方根内的任意一个数整除，
# 则i不是素数，返回0，否则i是素数，返回1。
def isprime(i):
	for t in range( 2, int(math.sqrt(i)) + 1 ):
		if i % t == 0:			
			return 0	
		else:
			return 1
print '100~110之间的素数有：'
for i in range(100,110):
	if isprime(i):
		print i
