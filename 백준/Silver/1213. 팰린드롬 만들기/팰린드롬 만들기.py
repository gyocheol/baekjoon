import sys
from collections import Counter

name = sys.stdin.readline().rstrip()
cnt = Counter(name)
odd = 0
mid = ""
ans = ""

for k, v in sorted(cnt.items()):
    if v % 2:
        odd += 1
        mid += k

    for _ in range(v//2):
        ans += k

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(ans+mid+ans[::-1])