n, m = map(int, input().split())
flag = True
for _ in range(m):
    t = int(input())
    books = list(map(int, input().split()))
    for k in range(t-1):
        if books[k] < books[k+1]:
            flag = False
            break
    if not flag:
        break
print("Yes" if flag else "No")