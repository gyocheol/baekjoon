n = input()
adj = [0] * 11

for i in n:
    if i == "9" or i == "6":
        if adj[9] >= adj[6]:
            adj[6] += 1
        else:
            adj[9] += 1
    else:
        adj[int(i)] += 1
print(max(adj))