l = []
for _ in range(9):
    l.append(int(input()))
total = sum(l)

for i in range(9):
    for j in range(i+1,9):
        if total == 100 + (l[i] + l[j]):
            num1, num2 = l[i], l[j]
            l.remove(num1)
            l.remove(num2)
            l.sort()

            for i in range(len(l)):
                print(l[i])
            break
    if len(l) < 9:
        break