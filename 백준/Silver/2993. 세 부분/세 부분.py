word = input()
n = len(word)
words = []
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            t = word[:j][::-1] + word[j:k][::-1] + word[k:][::-1]
            words.append(t)
print(min(words))