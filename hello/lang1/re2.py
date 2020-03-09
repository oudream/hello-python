import re


def test0():
    m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')

    print(("m.string:", m.string))
    print(("m.re:", m.re))
    print(("m.pos:", m.pos))
    print(("m.endpos:", m.endpos))
    print(("m.lastindex:", m.lastindex))
    print(("m.lastgroup:", m.lastgroup))

    print(("m.group(1,2):", m.group(1, 2)))
    print(("m.groups():", m.groups()))
    print(("m.groupdict():", m.groupdict()))
    print(("m.start(2):", m.start(2)))
    print(("m.end(2):", m.end(2)))
    print(("m.span(2):", m.span(2)))
    print((r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3')))


def test1():
    a = re.compile(r"""\d +  # the integral part
                       \.    # the decimal point
                       \d *  # some fractional digits""", re.X)
    b = re.compile(r"\d+\.\d*")
    m = re.match(r'hello', 'hello world!')
    print((m.group()))

    
def test2():
    m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
    print(( m.group(0) ))
    

def test3():
    print ( '' )
    

def test4():
    s = 'http://www.aa.com http://www.ab.net/'
    m = re.match(r"(\S+) (\S+)", r"http://www.aa.com http://www.ab.net/")
    print(( m.string ))
    print(( m.group() ))

if __name__ == '__main__':
    test4()
    

