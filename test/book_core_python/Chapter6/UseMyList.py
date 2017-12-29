# -*- coding:utf-8 -*-
# file: UseMyList.py
# 
import MyList				# 导入MyList模块
l = MyList.MyList(1,2,3,4,5)		# 调用MyList类实例化生成l对象
l.show()				# 调用show方法
l + 10					# 此处将调用__add__方法
l.show()				# 调用show方法
l * 2					# 此处将调用__add__方法
l.show()				# 调用show方法
print len(l)
l ** 3					# 此处将调用__add__方法
l.show()				# 调用show方法

