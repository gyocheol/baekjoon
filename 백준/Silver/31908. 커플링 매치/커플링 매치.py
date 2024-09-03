n = int(input())
d = {}

for _ in range(n):
    name, ring = map(str, input().split())
    if ring != "-":
        try: d[ring] += " " + name
        except: d[ring] = name
cnt = 0
ans = []
for k, v in d.items():
    if len(v.split()) == 2:
        cnt += 1
        ans.append(v)
print(cnt)
for i in range(cnt):
    print(ans[i])