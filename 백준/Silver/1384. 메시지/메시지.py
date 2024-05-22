group = 1
while True:
    n = int(input())
    if n == 0:
        break
    print(f"Group {group}")
    group += 1
    names, letters = [], []
    flag = True
    for i in range(n):
        students = input().split()
        names.append(students[0])
        letters.append(students[1:])
    for i in range(n):
        if "N" in letters[i]:
            for j in range(n-1):
                if letters[i][j] == "N":
                    print(f"{names[(n+i-1-j)%n]} was nasty about {names[i]}")
                    flag = False
    if flag:
        print("Nobody was nasty")
    print()