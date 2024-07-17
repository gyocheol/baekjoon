fibonacci = [0, 1, 1]
for i in range(3, 56):
    fibonacci.append(fibonacci[i-2]+fibonacci[i-1])
print(fibonacci[int(input())])