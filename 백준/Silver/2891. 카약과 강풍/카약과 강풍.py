N, S, R = map(int, input().split())
broken = set(map(int, input().split()))
pair = set(map(int, input().split()))

inters = broken & pair
broken = list(broken-inters)
pair = list(pair-inters)
pair.sort()
for p in pair:
    if p-1 in broken:
        broken.remove(p - 1)
    elif p+1 in broken:
        broken.remove(p + 1)

print(len(broken))