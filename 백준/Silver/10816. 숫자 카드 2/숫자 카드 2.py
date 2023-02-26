import sys
input = sys.stdin.readline

N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

dic = {}
for i in arr1:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for i in arr2:
    if i in dic:
        print(dic[i], end=" ")
    else:
        print(0, end=" ")