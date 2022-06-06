def d():
    l = []
    for i in range(1,10000):
        x = list(str(i))
        for j in x:
            i += int(j)
        l.append(i)

    for p in range(1,10000):
        if p not in l:
            print(p)
d()