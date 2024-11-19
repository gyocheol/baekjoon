import sys
input = sys.stdin.readline

start, end, stream = input().split()
start = int(start[:2])*60 + int(start[3:])
end = int(end[:2])*60 + int(end[3:])
stream = int(stream[:2])*60 + int(stream[3:])
ojm = set()
ans = 0

while True:
    try:
        time, name = input().split()
        time = int(time[:2])*60 + int(time[3:])
        if time <= start:
            ojm.add(name)
        elif end <= time <= stream:
            if name in ojm:
                ans += 1
                ojm.remove(name)
    except:
        break
print(ans)