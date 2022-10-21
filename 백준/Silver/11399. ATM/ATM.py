N = int(input())
arr = sorted(list(map(int, input().split())))
total = 0
for i in range(N):
    total += sum(arr[:i+1])
print(total)