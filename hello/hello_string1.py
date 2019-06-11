def decode1():
    str = "菜鸟教程";
    str_utf8 = str.encode("UTF-8")
    str_gbk = str.encode("GBK")
    print(str)
    print("UTF-8 编码：", str_utf8)
    print("GBK 编码：", str_gbk)
    print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'))
    print("GBK 解码：", str_gbk.decode('GBK', 'strict'))


# decode1()


def format1():
    # http://www.runoob.com/python/att-string-format.html
    print("{} {}".format("hello", "world"))  # 不设置指定位置，按默认顺序
    print("{1} {0} {1}".format("hello", "world"))  # 设置指定位置
    print("网站名：{name}, 地址 {url}".format(name="xx", url="www.xx.com"))
    # 通过字典设置参数
    site = {"name": "xx", "url": "www.xx.com"}
    print("网站名：{name}, 地址 {url}".format(**site))
    # 通过列表索引设置参数
    my_list = ['xx', 'www.xx.com']
    print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的
    # 数字格式化
    print("{:.2f}".format(3.1415926))


# format1()


def str1(ls1):
    ls1.append("a")


l1 = ['a']
str1(l1)
print(l1)
