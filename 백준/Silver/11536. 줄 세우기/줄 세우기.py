def comp(a, b):
    if a == b:
        return True
    else:
        return False

def increasing(arr):
    arr2 = sorted(arr)
    if comp(arr, arr2):
        return True

def decreasing(arr):
    arr2 = sorted(arr, reverse=True)
    if comp(arr, arr2):
        return True

arr = [input() for _ in range(int(input()))]

if increasing(arr):
    print("INCREASING")
elif decreasing(arr):
    print("DECREASING")
else:
    print("NEITHER")