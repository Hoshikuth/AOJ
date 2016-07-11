import sys

s = ""
alpha = "abcdefghijklmnopqrstuvwxyz"
while True:
    try:
        s += sys.stdin.readline().lower()
    except EOFerror:
        break

for c in alpha:
    print("{} : {}".format(c,s.count(c)))
