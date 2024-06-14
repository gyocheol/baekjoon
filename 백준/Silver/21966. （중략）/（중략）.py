import sys
input = sys.stdin.readline

n = int(input())
S = input()
if n <= 25:
    print(S)
else:
    if len(S[11:-12].split(".")) < 2 or not S[11:-12].split(".")[1]:
        print(S[:11]+"..."+S[-12:])
    else:
        print(S[:9]+"......"+S[-11:])
