import sys
input = sys.stdin.readline

def pooling_layer(arr, size):
    ans = [[0] * (size // 2) for i in range(size // 2)]

    for i in range(size // 2):
        for j in range(size // 2):
            candidates = [arr[2 * i][2 * j], arr[2 * i + 1][2 * j],
                          arr[2 * i][2 * j + 1], arr[2 * i + 1][2 * j + 1]]
            candidates.sort(reverse=True)
            ans[i][j] = candidates[1]

    return ans


n = int(input())
arr = []

for _ in range(n):
    l = list(map(int, input().split()))
    arr.append(l)

while n != 1:
    arr = pooling_layer(arr, n)
    n //= 2

print(arr[0][0])