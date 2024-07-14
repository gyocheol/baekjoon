num = 0

for i in range(3):
    arr = input()
    try:
        arr = int(arr)
        num = arr + 3 - i
    except:
        pass

if not num % 3 and not num % 5:
    print("FizzBuzz")
elif not num % 3 and num % 5:
    print("Fizz")
elif num % 3 and not num % 5:
    print("Buzz")
else:
    print(num)
