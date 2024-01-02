months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month, day, year, time = input().split(" ")
day = day[:-1]
time, minute = time.split(":")
flag = False
total = 0
now = 0
m = 24*60 # 일을 분으로 변경

# 윤년 계산
year = int(year)
if not year % 400 or not year % 4 and year % 100:
    total = 366*m
    flag = True
else:
    total = 365*m

# 달 계산
now_month = months.index(month)
to = [1,3,5,7,8,10,12] # 31일
for i in range(now_month):
    if i+1 == 2:
        if flag:
            now += 29*m
        else:
            now += 28*m
    elif i+1 in to:
        now += 31*m
    else:
        now += 30*m

# 일 계산
now += (int(day)-1)*m

# 시,분 계산
now += int(time) * 60 + int(minute)

# 결과
print(now/total*100)
