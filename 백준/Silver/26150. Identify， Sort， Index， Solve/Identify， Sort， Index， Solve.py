n = int(input())
puzzle = [list(input().split()) for _ in range(n)]
puzzle.sort(key=lambda x:int(x[1]))
ans = ""
for i in range(n):
    arr, num, idx = puzzle[i]
    ans += arr[int(idx)-1].upper()
print(ans)