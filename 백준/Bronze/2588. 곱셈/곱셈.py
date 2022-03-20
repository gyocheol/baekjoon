a = int(input())
b = input()

c = int(a) * int(b[-1])
d = int(a) * int(b[-2])
e = int(a) * int(b[-3])
f = int(a) * int(b[:])

print(c)
print(d)
print(e)
print(f)