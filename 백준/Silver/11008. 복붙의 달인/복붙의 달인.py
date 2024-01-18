T = int(input())
for _ in range(T):
    p, s = input().split()
    c = p.count(s)
    print(len(p)-(c*len(s))+c)