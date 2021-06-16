from pcapng import FileScanner

with open(r'C:/dev/backup/炬视AI/rknn_post_02.pcapng', 'rb') as fp:
    scanner = FileScanner(fp)
    for block in scanner:
        print(block)