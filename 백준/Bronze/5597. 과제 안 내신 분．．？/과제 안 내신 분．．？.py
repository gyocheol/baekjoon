all = [i for i in range(1, 31)]

for _ in range(28):
    x = int(input())
    all.remove(x)

for i in range(2):
    print(all[i])