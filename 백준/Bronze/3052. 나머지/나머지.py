l = []
res = 0
for i in range(10):
    a = int(input())
    l.append(a%42)
for i in range(42):
    if i in l:
        res+=1
    else:
        pass
print(res)