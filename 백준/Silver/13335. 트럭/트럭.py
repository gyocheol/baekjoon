from collections import deque

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))
bridge = deque([0]*w)
weight, time = 0, 0
while bridge:
    out = bridge.popleft()
    weight -= out

    if trucks:
        if weight + trucks[0] <= L:
            truck = trucks.popleft()
            bridge.append(truck)
            weight += truck
        else:
            bridge.append(0)
    time += 1

print(time)
