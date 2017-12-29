
def getNumber(fn):
    print(fn(10))

def line_conf():
    def line(x):
        return 2*x+1
    return line

getNumber(line_conf())
