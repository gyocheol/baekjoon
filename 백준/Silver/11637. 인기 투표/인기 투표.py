t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    if set(arr) == 1:
        print("no winner")
    else:
        max_v = max(arr)
        if arr.count(max_v) > 1:
            print("no winner")
        else:
            half = sum(arr) // 2
            if max_v > half:
                print("majority winner", arr.index(max_v)+1)
            else:
                print("minority winner", arr.index(max_v)+1)
