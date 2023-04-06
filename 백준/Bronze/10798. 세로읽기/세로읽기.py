arr = [list(input()) for _ in range(5)]
max_len = 0
for i in range(5):
    if max_len < len(arr[i]):
        max_len = len(arr[i])

ans = ''

for i in range(max_len):
    for j in range(5):
        try: ans += arr[j][i]
        except: pass

print(ans)