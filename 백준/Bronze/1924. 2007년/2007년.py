day = 0
month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_the_week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, input().split())

for i in range(x-1):
    day += month_list[i]

idx = (day + y) % 7
print(day_of_the_week[idx])