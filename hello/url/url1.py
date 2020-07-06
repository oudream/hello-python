from urllib.parse import urlparse

def hello1():
    url = 'https://192.168.5.29/web/goods/4285?goodsId=7202'
    parse = urlparse(url)
    print(parse)
    print(parse.path.startswith('/web/goods/'))
    print(parse.query.startswith('goodsId='))


if __name__ == '__main__':
    hello1()

