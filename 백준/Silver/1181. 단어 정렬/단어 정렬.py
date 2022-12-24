N = int(input())
arr = []
for _ in range(N):
    a = input()
    arr.append((a, len(a)))
arr = list(set(arr))
arr.sort(key=lambda x: (x[1], x[0]))

for i in range(len(arr)):
    print(arr[i][0])