# 다시 풀어보기
month, d, y, t = input().split(" ")
d = int(d[:-1])
y = int(y)
h, m = map(int, t.split(":"))
months_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
months_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 윤년일 때 2월에 +1
if not y % 400 or not y % 4 and y % 100:
    months_day[1] += 1
total = sum(months_day) * 24 * 60
now = (sum(months_day[:months_name.index(month)]) + d-1) * 24 * 60 + h * 60 + m

print(now/total*100)