n = int(input())

han = 0
for i in range(1, n+1):
    l = list(map(int, str(i)))
    if i < 100:
        han += 1
    elif l[0]-l[1] == l[1]-l[2]:
        han += 1
print(han)