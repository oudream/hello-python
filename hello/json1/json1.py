import json


# 自定义对象
class C:
    key1 = list
    key2 = str
    key3 = int
    key4 = tuple

    def __init__(self, key1, key2, key3, key4):
        self.key1 = key1
        self.key2 = key2
        self.key3 = key3
        self.key4 = key4


# 实例化自定义类
c = C([1, 2, 3], 'str', 0, ('yuanzu', '元组'))

# json.dumps方法不能对自定义对象直接序列化,首先把自定义对象转换成字典

overdict = c.__dict__

# 此时就可以用json.dumps序列化了
result = json.dumps(overdict, ensure_ascii=False)
print(result)
print(type(result))