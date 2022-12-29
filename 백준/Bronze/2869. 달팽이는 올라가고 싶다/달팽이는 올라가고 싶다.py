A, B, V = map(int, input().split())
if (V-B) % (A-B):
    print((V-B) // (A-B) + 1)
else:
    print((V - B) // (A - B))