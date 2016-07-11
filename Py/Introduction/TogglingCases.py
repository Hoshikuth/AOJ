t = input()
nt = ""
for i in range(len(t)):
    if t[i].islower() :
        nt += t[i].upper()
    elif t[i].isupper() :
        nt += t[i].lower()
    else :
        nt += t[i]

print(nt)
