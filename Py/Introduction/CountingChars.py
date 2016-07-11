import sys
alpha = "abcdefghijklmnopqrstuvwxyz"
dic = {c:0 for c in alpha}

t = sys.stdin.read()
for s in t:
    s = s.lower()
    if s in alpha :
        dic[s] += 1

for key in sorted(dic):
    print("{} : {}".format(key,dic[key]))
