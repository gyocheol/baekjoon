import sys
input = sys.stdin.readline

def r(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
    
    
n = int(input())
if n != 0:
    arr = sorted([int(input()) for _ in range(n)], key=lambda x:x)
    j_avg = r(n * 0.15)
    if j_avg != 0:
        print(r(sum(arr[j_avg:-j_avg]) / (n-2*j_avg)))
    else:
        print(r(sum(arr) / n))
else:
    print(n)