# 병합 정렬
def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q) # 전반부
        merge_sort(A, q+1, r) # 후반부
        merge(A, p, q, r) # 병합

def merge(A, p, q, r):
    global cnt, ans
    i = p
    j = q+1
    tmp = []

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    while i <= q: # 왼쪽 배열 남은 것 채워넣기
        tmp.append(A[i])
        i += 1
    while j <= r: # 오른쪽 배열 남은 것 채워넣기
        tmp.append(A[j])
        j += 1

    i, t = p, 0
    while i <= r:
        A[i] = tmp[t]
        cnt += 1
        if cnt == k:
            ans = A[i]
            break
        i += 1
        t += 1


n, k = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
ans = -1
merge_sort(A, 0, n-1)
print(ans)