# print(ord("z")-ord("a")) # 25
# print(ord("a")) # 97

for t in range(int(input())):
    test_case = input().lower()
    arr = [0] * 26
    for i in test_case:
        word = ord(i) - 97
        if 0 <= word < 26:
            arr[word] += 1
    print(f"Case {t+1}:", end=" ")
    ans = min(arr)
    if ans == 0:
        print("Not a pangram")
    elif ans == 1:
        print("Pangram!")
    elif ans == 2:
        print("Double pangram!!")
    else:
        print("Triple pangram!!!")
