import time


class D(object):

    def __init__(self, map):
        self.map = map

    def __setattr__(self, name, value):
        if name == 'map':
            object.__setattr__(self, name, value)
            return True
        print('set attr called ', name, value)
        self.map[name] = value

    def __getattr__(self, name):
        v = self.map[name]
        if isinstance(v, (dict)):
            return (DictObj(v))
        if isinstance(v, (list)):
            r = []
            for i in v:
                r.append(DictObj(i))
            return (r)
        else:
            return (self.map[name])

    def __getitem__(self, name):
        return (self.map[name])


if __name__ == '__main__':
    # json转换成字典
    import json

    # 实际上JSON就是Python中的字符串，所以在这里首先定义一个字符串充当从网络请求中得到的json
    json_obj = '{"key1":[1,2,3],"key2":"str2"}'
    # 注意json键值对的边界符只能用双引号
    t = json.loads(json_obj)

    # 字典转换成自定义对象
    model = D(t)
    print(model.key2)