import os
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)

    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

def createDirByBookmark(fp):
    def read(fo):
        while True:
            line = fo.readline()
            if not line:
                break
            yield line

    parser = MyHTMLParser()

    if not os.path.exists(fp):
        print('don exists the path : ', fp)
        return
    try:
        f = open(fp, 'rb')
        if f is not None:
            for data in read(f):
                parser.feed(data.decode('utf-8'))
            f.close()
    except IOError as e:
        print(str(e))

def run():
    fp = '/ddd/oudream/bookmarks/chrome.bookmarks.html'
    createDirByBookmark(fp)

if __name__ == '__main__':
    run()
else:
    run()
