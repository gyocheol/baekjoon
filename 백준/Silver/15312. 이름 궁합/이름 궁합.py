d = {"A":3, "B":2, "C":1, "D":2, "E":3, "F":3, "G":2, "H":3, "I":3, "J":2, "K":2, "L":1, "M":2, "N":2, "O":1, "P":2, "Q":2, "R":2, "S":1, "T":2, "U":1, "V":1, "W":1, "X":2, "Y":2, "Z":1}
a = list(input())
b = list(input())
n = len(a)
num = []
for i in range(n):
    num.append((d[a[i]]))
    num.append((d[b[i]]))
while len(num) > 2:
    total = []
    for i in range(len(num)-1):
        total.append((num[i]+num[i+1])%10)
    num = total

print("".join(map(str, num)))