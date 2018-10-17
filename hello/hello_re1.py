import re


def hello0():
    m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')

    print("m.string:", m.string)
    print("m.re:", m.re)
    print("m.pos:", m.pos)
    print("m.endpos:", m.endpos)
    print("m.lastindex:", m.lastindex)
    print("m.lastgroup:", m.lastgroup)

    print("m.group(1,2):", m.group(1, 2))
    print("m.groups():", m.groups())
    print("m.groupdict():", m.groupdict())
    print("m.start(2):", m.start(2))
    print("m.end(2):", m.end(2))
    print("m.span(2):", m.span(2))
    print(r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3'))


def hello1():
    a = re.compile(r"""\d +  # the integral part
                       \.    # the decimal point
                       \d *  # some fractional digits""", re.X)
    b = re.compile(r"\d+\.\d*")
    m = re.match(r'hello', 'hello world!')
    print(m.group())


def hello2():
    m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
    print((m.group(0)))


def hello3():
    print('')


def hello4():
    s = 'http://www.aa.com http://www.ab.net/'
    m = re.match(r"(\S+) (\S+)", r"http://www.aa.com http://www.ab.net/")
    print((m.string))
    print((m.group()))

def hello5():
    import re

    content = '''
    <td>
    <a href="https://www.baidu.com/articles/zj.html" title="浙江省">浙江省主题介绍</a>
    <a href="https://www.baidu.com//articles/gz.html" title="贵州省">贵州省主题介绍</a>
    </td>
    '''

    # 获取<a href></a>之间的内容
    print(u'获取链接文本内容:')
    res = r'<a .*?>(.*?)</a>'
    mm = re.findall(res, content, re.S | re.M)
    for value in mm:
        print(value)

if __name__ == '__main__':
    hello5()


