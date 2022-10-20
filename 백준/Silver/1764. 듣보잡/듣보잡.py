N, M = map(int, input().split())
A = []
B = []
for _ in range(N):
    A.append(input())

for _ in range(M):
    B.append(input())

hap = sorted(list(set(A) & set(B)))
n = len(hap)
print(n)
for i in range(n):
    print(hap[i])