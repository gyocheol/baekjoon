vowels = ["a", "i", "y", "e", "o", "u"]
consonants = ["b", "k", "x", "z", "n", "h", "d", "c", "w", "g", "p", "v", "j", "q", "t", "s", "r", "l", "m", "f"]

while True:
    try:
        string = input()

        ans = ""
        for char in string:
            charisLower = True

            if char.isupper():
                charisLower = False
                char = char.lower()

            if char in vowels:
                changeChar = vowels[(vowels.index(char) + 3) % 6]
                ans += changeChar if charisLower else changeChar.upper()

            elif char in consonants:
                changeChar = consonants[(consonants.index(char) + 10) % 20]
                ans += changeChar if charisLower else changeChar.upper()

            else:
                ans += char
        print(ans)
    except:
        break