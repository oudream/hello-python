
class TestStr1:
    def decode1():
        str = "菜鸟教程";
        str_utf8 = str.encode("UTF-8")
        str_gbk = str.encode("GBK")
        print(str)
        print("UTF-8 编码：", str_utf8)
        print("GBK 编码：", str_gbk)
        print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
        print("GBK 解码：", str_gbk.decode('GBK','strict'))

testStr1 = TestStr1()
TestStr1.decode1()
