import sys

print((sys.argv))

names = {}

names = sys.stdin.readlines()

snames = ''
for name in names:
    snames += name

print(snames)

print('\nfinish.')