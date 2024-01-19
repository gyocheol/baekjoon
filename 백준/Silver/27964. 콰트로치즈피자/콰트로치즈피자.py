n = int(input())
ingredient = list(input().split())
ans = "yummy"
if n < 4:
    ans = "sad"
else:
    d = {}
    for i in range(n):
        if ingredient[i][-6:] == "Cheese":
            try: d[ingredient[i]] += 1
            except: d[ingredient[i]] = 1
    if len(d) < 4:
        ans = "sad"
print(ans)