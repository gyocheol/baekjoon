n = 1
ans = []

while n:
    n = int(input())
    if n == 0:
        break
    students = [input() for _ in range(n)]
    total = []

    for i in range(2*n-1):
        num = int(input().split()[0])
        if num in total:
            total.remove(num)
        else:
            total.append(num)
    for i in total:
        ans.append(students[i-1])
for i in range(len(ans)):
    print(i+1, ans[i])