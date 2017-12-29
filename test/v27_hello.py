

# from __future__ import unicode_literals


str1 = '\'xxx\' is unicode?,'
str2 = 'u\'xxx\' is unicode?'
str3 = '\'xxx\' is str?'
str4 = 'b\'xxx\' is str?'

class Hello:
    pass

hello1 = Hello()

print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))
print(str4.__class__)
print(hello1.__class__)
print(hello1.__name__)
# print(str4.__name__)

# print '\'xxx\' is unicode?', isinstance('xxx', unicode)
# print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
# print '\'xxx\' is str?', isinstance('xxx', str)
# print 'b\'xxx\' is str?', isinstance(b'xxx', str)

