a = input().upper()
b = list(set(a))
l = []

for i in b:
    cnt = a.count(i)
    l.append(cnt)
if l.count(max(l)) >= 2:
    print("?")
else :
    print(b[l.index(max(l))])