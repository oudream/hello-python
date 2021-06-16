import re

import yaml


# 类定义
class MatchConditionItem:
    @staticmethod
    def Contain(src, sub):
        return sub in src

    @staticmethod
    def UnContain(src, sub):
        return not (sub in src)

    # 定义基本属性
    operation = ''
    content = ''
    func = Contain

    # 定义构造方法
    def __init__(self, o, c):
        self.operation = o
        self.content = c
        self.func = MatchConditionItem.Contain if o == '@' else MatchConditionItem.UnContain

    def match(self, src):
        return self.func(src, self.content)


# 类定义
class MatchCondition:
    # 定义基本属性
    value = ''
    ms = []

    # 定义构造方法
    def __init__(self, value, ms):
        self.value = value
        self.ms = []
        if ms is None:
            self.ms.append(MatchConditionItem('@', value))
        else:
            for m in ms:
                self.ms.append(MatchConditionItem(m['o'], m['c']))

    def match(self, src):
        for m in self.ms:
            if not m.match(src):
                return False
        return True


# 类定义
class MatchClass:
    # 定义基本属性
    name = ''
    vcs = []

    # 定义构造方法
    def __init__(self, name, vcs):
        self.name = name
        self.vcs = []
        for vc in vcs:
            self.vcs.append(MatchCondition(vc['v'], vc.get('ms')))

    def match_value(self, src):
        for vc in self.vcs:
            if vc.match(src):
                return vc.value
        return ""


noneMatch = MatchClass("", [])
levelMatch = noneMatch
bayMatch = noneMatch
deviceMatch = noneMatch

with open("psm.yaml", encoding='utf-8') as file:
    data = yaml.safe_load(file)
    print(data)
    print(data['psm']['levels'])
    print(data['psm']['bays'])
    print(data['psm']['devices'])

    levelMatch = MatchClass("level", data['psm']['levels'])
    bayMatch = MatchClass("bay", data['psm']['bays'])
    deviceMatch = MatchClass("device", data['psm']['devices'])

    s1 = "2号主变110kV侧中性点2029接地隔离开关O相"
    r1 = levelMatch.match_value(s1)
    print("结果为：", r1)
    r1 = deviceMatch.match_value(s1)
    print("结果为：", r1)

    print(str(data['psm']['bays']).split(','))


def fetchCode(src):
    sl = ["220kV", "110kV", "35kV", "10kV"]
    s = src
    for s in sl:
        s = s.replace(s, '')
    res = r'([A-Za-z0-9]{2,})'
    mm = re.findall(res, s, re.I)
    if len(mm) > 0:
        return mm[0]
    else:
        return ''


def indexSS(src, ss):
    idx = -1
    l = -1
    for s in ss:
        n = src.find(s)
        if n >= 0:
            if n < idx or idx == -1:
                idx = n
                l = len(s)
    return idx, l


def fetchFunc(src):
    b, bl = indexSS(src, ["=3", "=2", "=1", "="])
    if b < 0: return ""
    e, el = indexSS(src, [" ", ",", "，"])
    if e < 0: e = len(src)
    return src[b + bl:e]


print(fetchFunc("=PT侧接地"))
print(fetchFunc("=2母线接地"))
