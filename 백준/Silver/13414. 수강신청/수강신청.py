import sys

capacity, applicants = map(int, sys.stdin.readline().split())

# hash
d = {}
for i in range(1, applicants+1):
    student = sys.stdin.readline().rstrip()
    d[student] = i  # 자동으로 순서가 업데이트 됨!
# 들어온 순서(value) 기준 오름차순
students = sorted(d.items(), key=lambda item : item[1])

# 결과
for i in range(min(len(students), capacity)):
    print(students[i][0])