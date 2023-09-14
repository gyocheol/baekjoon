n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    arr[i] = arr[i][1:]
    arr[i].sort(reverse=True)
    max_difference = 0
    for j in range(1, len(arr[i])):
        if max_difference < arr[i][j-1] - arr[i][j]:
            max_difference = arr[i][j-1] - arr[i][j]

    print(f"Class {i+1}")
    print(f"Max {max(arr[i])}, Min {min(arr[i])}, Largest gap {max_difference}")
